#!/usr/bin/env python3
"""
scan-images.py — Turn a FOLDER of photos into a ready-to-paste list for an
artwork's `more_images` cell in works.csv.

Workflow:
  1. Make a folder per artwork inside images/, e.g.  images/too_much/
  2. Drop all the photos for that piece into it.
  3. Run this script. Copy the printed line into the artwork's more_images cell.

Usage:
    python scripts/scan-images.py            # every subfolder of images/
    python scripts/scan-images.py too_much   # just images/too_much/

Ordering: NATURAL by the number in the filename (foo-2, foo-9, foo-10, foo-11).
To reorder, just rename the files (change the number). Output uses forward
slashes so it works on the web. No files are modified.
"""
import os
import re
import sys

BASE = os.path.join(os.path.dirname(__file__), '..')
IMG = os.path.join(BASE, 'images')
EXTS = ('.jpg', '.jpeg', '.png', '.webp', '.avif', '.gif')


def natkey(name):
    """Natural sort key: 'foo-10' sorts after 'foo-9'."""
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r'(\d+)', name)]


def list_folder(folder):
    path = os.path.join(IMG, folder)
    if not os.path.isdir(path):
        print(f'  (no such folder: images/{folder})')
        return
    files = [f for f in os.listdir(path) if f.lower().endswith(EXTS)]
    files.sort(key=natkey)
    if not files:
        print(f'  (no images in images/{folder})')
        return
    paths = [f'images/{folder}/{f}' for f in files]
    print(f'\n=== images/{folder}  ({len(paths)} images) ===')
    print('Paste this into the more_images cell for the artwork:\n')
    print(' | '.join(paths))


def main():
    if not os.path.isdir(IMG):
        print('No images/ folder found.')
        sys.exit(1)
    args = [a.strip('/\\') for a in sys.argv[1:]]
    if args:
        for a in args:
            list_folder(a)
        return
    subs = [d for d in os.listdir(IMG) if os.path.isdir(os.path.join(IMG, d))]
    subs.sort(key=natkey)
    if not subs:
        print('No subfolders inside images/.')
        print('Make one per artwork (e.g. images/too_much/), drop photos in, then re-run.')
        return
    for d in subs:
        list_folder(d)


if __name__ == '__main__':
    main()
