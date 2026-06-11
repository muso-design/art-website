#!/usr/bin/env python3
"""
validate-csv.py — Pre-deploy CSV validator.

Checks:
  - works.csv: required fields (id, title, image); image / hover_image /
    more_images files exist; dimensions carry a unit
  - settings.csv: required keys present; slideshow_N images exist
  - bio.csv: at least one bio paragraph; image_N / process_images files exist
  - contact.csv: at least one contact item
  - Every path field: forward slashes only (no backslashes), and the file is
    present on disk with the exact same case (GitHub Pages is case-sensitive)

Exits with code 1 and prints errors if validation fails.
Called by deploy.bat before pushing to GitHub.

Usage:
    python scripts/validate-csv.py
"""

import os
import sys
import csv
import io
import re

BASE = os.path.join(os.path.dirname(__file__), '..')

ERRORS = []
WARNINGS = []

def error(msg):
    ERRORS.append('  ERROR: ' + msg)

def warn(msg):
    WARNINGS.append('  WARN:  ' + msg)

# ── CSV parser (same semantics as the site's JS parseCSV) ──────────────
def load_kv(filepath):
    """Load a key-value CSV (settings/bio/contact). Returns dict."""
    kv = {}
    with open(filepath, newline='', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header row
        for row in reader:
            if not row:
                continue
            key = row[0].strip() if len(row) > 0 else ''
            if not key or key.startswith('#'):
                continue
            value = row[1].strip() if len(row) > 1 else ''
            kv[key] = value
    return kv

def load_objects(filepath):
    """Load an object-list CSV (works). Returns list of dicts."""
    rows = []
    with open(filepath, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row:
                continue
            first = next(iter(row.values()), '')
            if (first or '').startswith('#'):
                continue
            rows.append({k: (v or '').strip() for k, v in row.items()})
    return rows

# ── Path helpers ───────────────────────────────────────────────────────
PATH_SPLIT = re.compile(r'[|;\n\r]+')

def resolve_cased(rel):
    """Resolve a repo-relative path one segment at a time, checking exact case.
    Returns ('ok', None) | ('missing', None) | ('case', actual_path_on_disk).
    GitHub Pages is case-sensitive, so a wrong-case path 404s in production even
    though it resolves fine on a Windows/macOS filesystem."""
    cur = BASE
    for seg in [p for p in rel.split('/') if p not in ('', '.')]:
        try:
            entries = os.listdir(cur)
        except (FileNotFoundError, NotADirectoryError):
            return ('missing', None)
        if seg in entries:
            cur = os.path.join(cur, seg)
        else:
            lower = {e.lower(): e for e in entries}
            if seg.lower() in lower:
                actual = os.path.relpath(os.path.join(cur, lower[seg.lower()]), BASE)
                return ('case', actual.replace(os.sep, '/'))
            return ('missing', None)
    return ('ok', None)

def check_path_field(label, field, value, multi=False):
    """Validate an image-path field: no backslashes, and the file exists on disk
    with the exact same case. multi=True for cells holding several paths
    separated by | ; or line breaks (e.g. more_images, process_images)."""
    if not value:
        return
    if '\\' in value:
        error(f'{label}: backslash in {field} path — use forward slashes "/": {value.strip()!r}')
    parts = PATH_SPLIT.split(value) if multi else [value]
    for p in parts:
        p = p.strip().replace('\\', '/')
        if not p:
            continue
        status, actual = resolve_cased(p)
        if status == 'missing':
            error(f'{label}: {field} file not found on disk: {p}')
        elif status == 'case':
            error(f'{label}: {field} case mismatch (GitHub Pages is case-sensitive): '
                  f'{p}  ->  on disk it is {actual}')

# ── Suspicious-text checks ─────────────────────────────────────────────
_UNIT_RE = re.compile(r'(cm|mm|millimet|centimet|\bm\b|\bin\b|inch|ft|feet|["”″])', re.I)

def check_dimensions(label, dim):
    """Warn if a dimensions value has numbers but no unit (e.g. '25 × 15 × 7')."""
    if not dim:
        return
    if any(ch.isdigit() for ch in dim) and not _UNIT_RE.search(dim):
        warn(f'{label}: dimensions {dim!r} has no unit — add cm, mm, in, …')

# ── Validate works.csv ─────────────────────────────────────────────────
def validate_works():
    path = os.path.join(BASE, 'works.csv')
    if not os.path.exists(path):
        error('works.csv not found')
        return

    works = load_objects(path)
    if not works:
        warn('works.csv has no artwork rows')
        return

    required_fields = ['title', 'image']
    for i, w in enumerate(works, start=1):
        label = f"works.csv row {i} (id={w.get('id','?')!r}, title={w.get('title','?')!r})"
        for field in required_fields:
            if not w.get(field):
                error(f'{label}: missing required field "{field}"')
        check_path_field(label, 'image', w.get('image', ''))
        check_path_field(label, 'hover_image', w.get('hover_image', ''))
        check_path_field(label, 'more_images', w.get('more_images', ''), multi=True)
        check_dimensions(label, w.get('dimensions', ''))

# ── Validate settings.csv ──────────────────────────────────────────────
REQUIRED_SETTINGS = [
    'site_name', 'color_background', 'color_text',
    'font_family', 'slideshow_1',
]
def validate_settings():
    path = os.path.join(BASE, 'settings.csv')
    if not os.path.exists(path):
        error('settings.csv not found')
        return

    s = load_kv(path)
    for key in REQUIRED_SETTINGS:
        if not s.get(key):
            error(f'settings.csv: required key "{key}" is missing or empty')

    # Slideshow image paths (slideshow_1, slideshow_2, … — captions are skipped)
    for key, val in s.items():
        if re.fullmatch(r'slideshow_\d+', key):
            check_path_field('settings.csv', key, val)

    # Warn about Google Fonts (GDPR violation)
    font_url = s.get('font_url', '')
    if 'googleapis.com' in font_url or 'fonts.google' in font_url:
        warn(
            'settings.csv font_url points to Google Fonts — GDPR violation!\n'
            '         Self-host instead: python scripts/get-font.py "Font Name"\n'
            '         Then clear font_url and set font_family in settings.csv'
        )

    # Warn about placeholder email
    if 'your@email.com' in str(s):
        warn('settings.csv still contains placeholder email "your@email.com"')

# ── Validate bio.csv ───────────────────────────────────────────────────
def validate_bio():
    path = os.path.join(BASE, 'bio.csv')
    if not os.path.exists(path):
        error('bio.csv not found')
        return
    b = load_kv(path)
    if not b.get('bio_1'):
        warn('bio.csv: no bio_1 paragraph found')
    check_path_field('bio.csv', 'photo', b.get('photo', ''))
    for key, val in b.items():
        if re.fullmatch(r'image_\d+', key):
            check_path_field('bio.csv', key, val)
    check_path_field('bio.csv', 'process_images', b.get('process_images', ''), multi=True)

# ── Validate contact.csv ───────────────────────────────────────────────
def validate_contact():
    path = os.path.join(BASE, 'contact.csv')
    if not os.path.exists(path):
        error('contact.csv not found')
        return
    c = load_kv(path)
    if not c.get('item_label_1'):
        warn('contact.csv: no contact items found')
    # Warn about placeholder values
    for key, val in c.items():
        if 'your@email.com' in val or 'yourhandle' in val:
            warn(f'contact.csv: {key} still contains a placeholder value')
            break

# ── Run all validators ─────────────────────────────────────────────────
def main():
    # Make stdout robust to non-ASCII (× in dimensions, accented filenames) so
    # the validator never crashes on a legacy Windows code page during deploy.
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    print('Validating CSV files...')
    validate_works()
    validate_settings()
    validate_bio()
    validate_contact()

    if WARNINGS:
        print()
        for w in WARNINGS:
            print(w)

    if ERRORS:
        print()
        for e in ERRORS:
            print(e)
        print()
        print(f'Validation FAILED — {len(ERRORS)} error(s). Fix the issues above before deploying.')
        sys.exit(1)
    else:
        print(f'Validation passed ({len(WARNINGS)} warning(s)).')

if __name__ == '__main__':
    main()
