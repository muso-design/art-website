#!/usr/bin/env python3
"""
download-fonts.py — Download Cormorant Garamond woff2 files from Google Fonts
and save them to /fonts/ for self-hosting.

Usage:
    python scripts/download-fonts.py

Requires: Python 3.6+ (no third-party packages needed)
"""

import os
import re
import urllib.request
import sys

FONTS_DIR = os.path.join(os.path.dirname(__file__), '..', 'fonts')

# Google Fonts API URL for Cormorant Garamond weights/styles needed by this site
GOOGLE_FONTS_URL = (
    'https://fonts.googleapis.com/css2'
    '?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400'
    '&display=swap'
)

# Map Google's internal font names to our file naming convention
# Adjust if the downloaded CSS uses different descriptor strings
NAME_MAP = {
    ('cormorant garamond', '300', 'normal'): 'CormorantGaramond-Light',
    ('cormorant garamond', '400', 'normal'): 'CormorantGaramond-Regular',
    ('cormorant garamond', '500', 'normal'): 'CormorantGaramond-Medium',
    ('cormorant garamond', '300', 'italic'): 'CormorantGaramond-LightItalic',
    ('cormorant garamond', '400', 'italic'): 'CormorantGaramond-Italic',
}

# Pretend to be a modern browser so Google Fonts returns woff2 URLs
HEADERS = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/124.0.0.0 Safari/537.36'
    )
}

def fetch(url, headers=None):
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()

def parse_font_faces(css_text):
    """Extract @font-face blocks and parse their properties."""
    faces = []
    for block in re.findall(r'@font-face\s*\{([^}]+)\}', css_text, re.S):
        props = {}
        for line in block.split(';'):
            m = re.match(r'\s*([\w-]+)\s*:\s*(.+)', line.strip())
            if m:
                props[m.group(1).strip()] = m.group(2).strip().strip('"\'')
        if 'src' in props:
            url_m = re.search(r"url\(['\"]?([^'\")\s]+)['\"]?\)", props['src'])
            if url_m:
                props['_url'] = url_m.group(1)
        faces.append(props)
    return faces

def main():
    os.makedirs(FONTS_DIR, exist_ok=True)

    print('Fetching font CSS from Google Fonts...')
    try:
        css = fetch(GOOGLE_FONTS_URL, HEADERS).decode('utf-8')
    except Exception as e:
        print(f'ERROR: Could not fetch font CSS: {e}')
        sys.exit(1)

    faces = parse_font_faces(css)
    if not faces:
        print('ERROR: No @font-face blocks found in CSS response.')
        sys.exit(1)

    print(f'Found {len(faces)} @font-face declarations.')
    downloaded = 0
    skipped = 0

    for face in faces:
        family = face.get('font-family', '').lower().strip('"\'')
        weight = face.get('font-weight', '400')
        style  = face.get('font-style', 'normal')
        url    = face.get('_url', '')

        key = (family, weight, style)
        filename = NAME_MAP.get(key)

        if not filename:
            print(f'  SKIP (unknown variant): family={family} weight={weight} style={style}')
            skipped += 1
            continue

        dest = os.path.join(FONTS_DIR, filename + '.woff2')
        if os.path.exists(dest):
            print(f'  EXISTS: {filename}.woff2')
            skipped += 1
            continue

        print(f'  Downloading {filename}.woff2 ...')
        try:
            data = fetch(url, HEADERS)
            with open(dest, 'wb') as f:
                f.write(data)
            print(f'    Saved {len(data)//1024} KB')
            downloaded += 1
        except Exception as e:
            print(f'    ERROR downloading {url}: {e}')

    print(f'\nDone. {downloaded} downloaded, {skipped} skipped.')
    if downloaded > 0:
        print('\nNext steps:')
        print('  1. Commit the woff2 files: git add fonts/ && git commit -m "Add self-hosted fonts"')
        print('  2. Update font_url in settings.csv to empty (fonts now load from /fonts/)')
        print('  3. Run deploy.bat to push to GitHub Pages')

if __name__ == '__main__':
    main()
