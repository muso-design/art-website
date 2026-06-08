# Self-hosted fonts

The site's font lives here as `.woff2` files, served from this folder (not from
Google's CDN). Self-hosting keeps it GDPR-safe — no visitor data is sent to Google.

`../fonts.css` lists the `@font-face` rules and `index.html` links it. Both the
woff2 files and `fonts.css` are generated automatically — don't edit by hand.

## Swap to a different font (one command)

```
python scripts/get-font.py "Josefin Sans"
```

Use any family name from https://fonts.google.com (exact spelling). The script:

1. downloads the woff2 files into this folder,
2. regenerates `../fonts.css`,
3. prints the value to put in `settings.csv`.

Then open `settings.csv` and set `font_family` to the printed value, e.g.

```
font_family,"Josefin Sans", sans-serif
```

That's it — deploy and the new font is live.

By default the script pulls normal 300/400/500/600 + italic 300/400 (what the
site uses). Edit `WEIGHTS` at the top of `scripts/get-font.py` to change that.

## Why self-hosted?

Linking a Google Fonts URL makes every visitor's browser hit fonts.googleapis.com,
which sends their IP to Google — ruled a GDPR violation for operators based in
Germany. Serving the files ourselves avoids that entirely.
