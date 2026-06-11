#!/usr/bin/env python3
"""
optimize-images.py — Generate responsive image variants for every photo the
CSVs reference, so phones stop downloading ~3000px originals for small tiles.

Workflow stays simple for the artist: drop a file in images/, write one path in
a CSV. This script (run by deploy.bat) does the rest — it never asks you to
write srcset by hand.

What it does
------------
  • Reuses the validator's path collector (scripts/validate-csv.py) so it sees
    exactly the same set of referenced images.
  • For each original, writes resized variants ALONGSIDE it using a strict
    suffix convention:  name_w480.webp  name_w800.webp  name_w2000.webp  (+ .avif
    if pillow-avif-plugin / native AVIF is available, otherwise .jpg).
  • Widths: 480, 800, 2000 (BRIEF minimum is 800 + 2000). Never upscales — a
    width is skipped when it is >= the original's width.
  • Quality ~80. Idempotent: a variant already newer than its source is skipped.
  • Writes images/variants.json — the manifest the site reads at runtime to
    decide which <source>/srcset to emit (and to degrade to the plain original
    when an image has no variants yet).

Formats
-------
  • AVIF available  -> AVIF + WebP   (smallest first, per BRIEF)
  • AVIF NOT avail. -> WebP + JPEG   (and it says so loudly)
  The original file is always the final <img> fallback.

Exit codes: 0 on success (AVIF-missing is NOT a failure), 1 only if Pillow is
not installed at all.

Usage:
    python scripts/optimize-images.py
"""

import os
import sys
import json
import importlib.util

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
MANIFEST = os.path.join(ROOT, 'images', 'variants.json')

# Tunables — single source of truth for both the generated files and (via the
# manifest) the srcset the site emits. Change here, then re-run.
WIDTHS = [480, 800, 2000]
QUALITY = 80

# ── Pillow + AVIF detection ────────────────────────────────────────────
try:
    from PIL import Image
except ImportError:
    sys.stderr.write(
        'ERROR: Pillow is not installed. Responsive images cannot be generated.\n'
        '       Install it with:  pip install Pillow\n'
        '       (for AVIF too:    pip install Pillow pillow-avif-plugin)\n'
    )
    sys.exit(1)

AVIF_OK = False
try:
    import pillow_avif  # noqa: F401  (registers the AVIF plugin on import)
    AVIF_OK = True
except Exception:
    # Pillow 11.3+ ships native AVIF; detect that too.
    AVIF_OK = 'AVIF' in getattr(Image, 'SAVE', {})

# webp first (always), then the third format depending on AVIF availability.
FORMATS = ['avif', 'webp'] if AVIF_OK else ['webp', 'jpg']

# ── Reuse the validator's path collector ───────────────────────────────
_spec = importlib.util.spec_from_file_location(
    'validate_csv', os.path.join(os.path.dirname(__file__), 'validate-csv.py'))
_vc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_vc)
collect_image_paths = _vc.collect_image_paths

# ── Helpers ────────────────────────────────────────────────────────────
def variant_name(rel, w, fmt):
    """images/x/name.webp + (800,'webp') -> images/x/name_w800.webp"""
    stem, _ext = os.path.splitext(rel)
    return f'{stem}_w{w}.{fmt}'

def human(nbytes):
    mb = nbytes / (1024 * 1024)
    if mb >= 1:
        return f'{mb:.2f} MB'
    return f'{nbytes / 1024:.0f} KB'

def save_variant(im, dest_abs, fmt):
    """Encode one resized image. Returns bytes written."""
    if fmt == 'jpg':
        rgb = im.convert('RGB')  # JPEG has no alpha
        rgb.save(dest_abs, 'JPEG', quality=QUALITY, optimize=True, progressive=True)
    elif fmt == 'webp':
        im.save(dest_abs, 'WEBP', quality=QUALITY, method=6)
    elif fmt == 'avif':
        im.save(dest_abs, 'AVIF', quality=QUALITY)
    return os.path.getsize(dest_abs)

# ── Main ───────────────────────────────────────────────────────────────
def main():
    print('Optimizing images...')
    if AVIF_OK:
        print(f'  formats: AVIF + WebP   widths: {WIDTHS}   quality: {QUALITY}')
    else:
        print(f'  formats: WebP + JPEG   widths: {WIDTHS}   quality: {QUALITY}')
        print('  NOTE: AVIF skipped — pillow-avif-plugin not installed.')
        print('        For smaller files run:  pip install pillow-avif-plugin   then re-run.')

    rels = collect_image_paths(ROOT)
    if not rels:
        print('  No referenced images found — nothing to do.')
        return

    manifest = {}
    made = skipped = 0
    src_bytes = 0          # total size of the referenced originals
    variant_bytes = 0      # total size of all variants on disk (made or kept)
    mobile_orig = 0        # originals' bytes (for the representative saving line)
    mobile_w800 = 0        # the w800 webp bytes (representative phone payload)
    missing = []

    for rel in rels:
        src_abs = os.path.join(ROOT, rel.replace('/', os.sep))
        if not os.path.isfile(src_abs):
            missing.append(rel)
            continue
        try:
            with Image.open(src_abs) as im:
                im.load()
                ow, oh = im.size
                src_size = os.path.getsize(src_abs)
                src_bytes += src_size
                src_mtime = os.path.getmtime(src_abs)
                entry = {'w': ow, 'h': oh}
                for fmt in FORMATS:
                    widths_done = []
                    for w in WIDTHS:
                        if w >= ow:
                            continue  # never upscale
                        rel_variant = variant_name(rel, w, fmt)
                        dest_abs = os.path.join(ROOT, rel_variant.replace('/', os.sep))
                        if (os.path.isfile(dest_abs)
                                and os.path.getmtime(dest_abs) >= src_mtime):
                            skipped += 1
                            widths_done.append(w)
                            variant_bytes += os.path.getsize(dest_abs)
                            if fmt == 'webp' and w == 800:
                                mobile_w800 += os.path.getsize(dest_abs)
                                mobile_orig += src_size
                            continue
                        h = max(1, round(oh * w / ow))
                        resized = im.resize((w, h), Image.LANCZOS)
                        nbytes = save_variant(resized, dest_abs, fmt)
                        made += 1
                        widths_done.append(w)
                        variant_bytes += nbytes
                        if fmt == 'webp' and w == 800:
                            mobile_w800 += nbytes
                            mobile_orig += src_size
                    if widths_done:
                        entry[fmt] = widths_done
                # Only record images that actually got at least one variant.
                if any(f in entry for f in FORMATS):
                    manifest[rel] = entry
        except Exception as e:
            print(f'  WARN: could not process {rel}: {e}')

    # Write the manifest the site reads at runtime.
    os.makedirs(os.path.dirname(MANIFEST), exist_ok=True)
    with open(MANIFEST, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=0, sort_keys=True)
        f.write('\n')

    # ── Summary ────────────────────────────────────────────────────────
    print()
    print(f'  {len(manifest)} image(s) with variants | '
          f'{made} generated, {skipped} up-to-date (skipped)')
    print(f'  referenced originals: {human(src_bytes)} | '
          f'variants on disk: {human(variant_bytes)}')
    if mobile_orig:
        saved = mobile_orig - mobile_w800
        pct = (saved / mobile_orig * 100) if mobile_orig else 0
        print(f'  representative phone load (these originals vs their w800 WebP): '
              f'{human(mobile_orig)} -> {human(mobile_w800)} '
              f'({pct:.0f}% smaller)')
    print(f'  manifest: images/variants.json ({len(manifest)} entries)')
    if missing:
        print(f'  note: {len(missing)} referenced file(s) missing on disk '
              f'(run validate-csv.py): {missing[:3]}')

if __name__ == '__main__':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    main()
