#!/usr/bin/env python3
"""
make-favicon.py — generate the favicon set from an "RC" monogram on the site's
dark brand colour. Regenerate any time by running:  python scripts/make-favicon.py

Outputs (site root): favicon.ico, favicon-32.png, apple-touch-icon.png, favicon.svg
To use a different mark, replace these files (keep the names) or edit TEXT/colours.
"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
BG   = (0x16, 0x15, 0x14)   # --home-nl-bg (dark hero)
FG   = (0xEC, 0xEB, 0xE8)   # dark-theme --text
TEXT = 'RC'
FONT = r'C:\Windows\Fonts\bahnschrift.ttf'   # geometric, Josefin-adjacent, legible small

def render(S):
    img = Image.new('RGB', (S, S), BG)
    d = ImageDraw.Draw(img)
    fs = int(S * 0.62)
    while fs > 6:
        f = ImageFont.truetype(FONT, fs)
        l, t, r, b = d.textbbox((0, 0), TEXT, font=f)
        if (r - l) <= S * 0.80 and (b - t) <= S * 0.72:
            break
        fs -= 2
    f = ImageFont.truetype(FONT, fs)
    l, t, r, b = d.textbbox((0, 0), TEXT, font=f)
    x = (S - (r - l)) / 2 - l
    y = (S - (b - t)) / 2 - t
    d.text((x, y), TEXT, font=f, fill=FG)
    return img

master = render(512)
master.resize((180, 180), Image.LANCZOS).save(os.path.join(ROOT, 'apple-touch-icon.png'))
master.resize((32, 32),  Image.LANCZOS).save(os.path.join(ROOT, 'favicon-32.png'))
master.save(os.path.join(ROOT, 'favicon.ico'), sizes=[(16, 16), (32, 32), (48, 48)])

svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">'
       '<rect width="512" height="512" fill="#161514"/>'
       '<text x="256" y="262" fill="#ecebe8" '
       'font-family="Bahnschrift,\'Segoe UI\',Josefin Sans,sans-serif" '
       'font-size="270" font-weight="500" text-anchor="middle" '
       'dominant-baseline="central">RC</text></svg>')
open(os.path.join(ROOT, 'favicon.svg'), 'w', encoding='utf-8').write(svg)

print('wrote favicon.ico, favicon-32.png, apple-touch-icon.png, favicon.svg')
