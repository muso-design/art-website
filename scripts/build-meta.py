#!/usr/bin/env python3
"""
build-meta.py — bake the SEO / link-sharing tags from settings.csv into the
STATIC <head> of index.html (title, description, OpenGraph, Twitter, canonical,
JSON-LD). Run by deploy.bat.

Why: search engines and chat apps that DON'T run JavaScript (Bing, DuckDuckGo,
WhatsApp, iMessage, Slack, LinkedIn, …) only read the static HTML. The site's JS
already updates these per page, but crawlers/scrapers need them baked in.

Settings used: site_name, site_role, site_description, og_image. SITE_URL is read
from index.html. The share image (og_image) is converted to a 1200×630 JPEG
(share-safe) automatically, whatever format you provide.
"""
import os, re, csv, sys, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
HTML = os.path.join(ROOT, 'index.html')
OG_W, OG_H = 1200, 630

def load_settings():
    kv = {}
    with open(os.path.join(ROOT, 'settings.csv'), newline='', encoding='utf-8-sig') as f:
        for row in csv.reader(f):
            if len(row) >= 2 and row[0].strip() and not row[0].strip().startswith('#'):
                kv[row[0].strip()] = row[1].strip()
    return kv

def esc(s):
    return (str(s).replace('&', '&amp;').replace('<', '&lt;')
            .replace('>', '&gt;').replace('"', '&quot;'))

def ensure_share_jpg(src_rel):
    """Convert/crop the share image to a 1200×630 JPEG. Returns the .jpg rel path."""
    stem, _ext = os.path.splitext(src_rel)
    out_rel = stem + '.jpg'
    src = os.path.join(ROOT, src_rel.replace('/', os.sep))
    out = os.path.join(ROOT, out_rel.replace('/', os.sep))
    if not os.path.isfile(src):
        print(f'  WARN: og_image not found on disk: {src_rel}')
        return out_rel
    try:
        from PIL import Image
        with Image.open(src) as im:
            im = im.convert('RGB')
            if im.size != (OG_W, OG_H):
                sw, sh = im.size
                scale = max(OG_W / sw, OG_H / sh)
                im = im.resize((round(sw * scale), round(sh * scale)), Image.LANCZOS)
                nw, nh = im.size
                left, top = (nw - OG_W) // 2, (nh - OG_H) // 2
                im = im.crop((left, top, left + OG_W, top + OG_H))
            im.save(out, 'JPEG', quality=88, optimize=True, progressive=True)
        print(f'  share image: {src_rel} -> {out_rel} ({OG_W}x{OG_H})')
    except Exception as e:
        print(f'  WARN: could not build share JPEG ({e}); using {src_rel} as-is')
        return src_rel
    return out_rel

def main():
    s = load_settings()
    html = open(HTML, encoding='utf-8').read()

    m = re.search(r"const SITE_URL='([^']+)'", html)
    site_url = (m.group(1) if m else '').rstrip('/')

    name = (s.get('site_name') or 'Roman Chystakhovskyi').strip()
    role = (s.get('site_role') or 'Sculptor').strip()
    title = f'{name} — {role}'
    desc = (s.get('site_description') or f'Portfolio of {name}.').strip()
    og_src = (s.get('og_image') or 'images/og-image.jpg').strip().lstrip('/')

    img_rel = ensure_share_jpg(og_src)
    img_url = f'{site_url}/{img_rel}'
    home_url = f'{site_url}/'
    et, ed, en = esc(title), esc(desc), esc(name)

    subs = [
        (r'(<title>)[^<]*(</title>)', et),
        (r'(<meta name="description" content=")[^"]*(")', ed),
        (r'(id="og-title"[^>]*content=")[^"]*(")', et),
        (r'(id="og-description"[^>]*content=")[^"]*(")', ed),
        (r'(id="og-url"[^>]*content=")[^"]*(")', esc(home_url)),
        (r'(id="og-image"[^>]*content=")[^"]*(")', esc(img_url)),
        (r'(id="og-image-alt"[^>]*content=")[^"]*(")', et),
        (r'(id="tw-title"[^>]*content=")[^"]*(")', et),
        (r'(id="tw-description"[^>]*content=")[^"]*(")', ed),
        (r'(id="tw-image"[^>]*content=")[^"]*(")', esc(img_url)),
        (r'(id="link-canonical"[^>]*href=")[^"]*(")', esc(home_url)),
        (r'(property="og:site_name" content=")[^"]*(")', en),
    ]
    n = 0
    for pat, val in subs:
        html, c = re.subn(pat, lambda mo, v=val: mo.group(1) + v + mo.group(2), html, count=1)
        n += c

    # JSON-LD Person — keep name/jobTitle/url/description in sync.
    def ld_repl(mo):
        try:
            data = json.loads(mo.group(2))
            data['name'] = name; data['jobTitle'] = role
            data['url'] = home_url; data['description'] = desc
            return mo.group(1) + json.dumps(data, ensure_ascii=False) + mo.group(3)
        except Exception:
            return mo.group(0)
    html = re.sub(r'(<script type="application/ld\+json" id="ld-json">)(.*?)(</script>)',
                  ld_repl, html, count=1, flags=re.S)

    open(HTML, 'w', encoding='utf-8').write(html)
    print(f'  baked SEO/share meta from settings.csv ({n} tags). title: {title!r}')

if __name__ == '__main__':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    main()
