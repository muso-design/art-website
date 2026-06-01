#!/usr/bin/env python3
"""
validate-csv.py — Pre-deploy CSV validator.

Checks:
  - works.csv: required fields (id, title, image), image files exist
  - settings.csv: required keys present
  - bio.csv: at least one bio paragraph
  - contact.csv: at least one contact item

Exits with code 1 and prints errors if validation fails.
Called by deploy.bat before pushing to GitHub.

Usage:
    python scripts/validate-csv.py
"""

import os
import sys
import csv
import io

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
        img = w.get('image', '')
        if img:
            img_path = os.path.join(BASE, img)
            if not os.path.exists(img_path):
                error(f'{label}: image file not found: {img}')
        else:
            # Already caught above — but warn without double-reporting
            pass

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

    # Warn about Google Fonts (GDPR violation)
    font_url = s.get('font_url', '')
    if 'googleapis.com' in font_url or 'fonts.google' in font_url:
        warn(
            'settings.csv font_url points to Google Fonts — GDPR violation!\n'
            '         Run: python scripts/download-fonts.py\n'
            '         Then clear font_url in settings.csv'
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
    photo = b.get('photo', '')
    if photo:
        photo_path = os.path.join(BASE, photo)
        if not os.path.exists(photo_path):
            error(f'bio.csv: portrait photo not found: {photo}')

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
