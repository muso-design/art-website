# Self-hosted fonts

Place Cormorant Garamond woff2 files here. Required files:

| File | Weight | Style |
|------|--------|-------|
| `CormorantGaramond-Light.woff2`       | 300 | normal |
| `CormorantGaramond-Regular.woff2`     | 400 | normal |
| `CormorantGaramond-Medium.woff2`      | 500 | normal |
| `CormorantGaramond-LightItalic.woff2` | 300 | italic |
| `CormorantGaramond-Italic.woff2`      | 400 | italic |

## How to download

Run the download script once (requires Python 3):

```
python scripts/download-fonts.py
```

This downloads from the Google Fonts API and saves files here.
After running, commit the woff2 files to the repo — they are
served from GitHub Pages, not from Google's servers.

## Why self-hosted?

Embedding a Google Fonts URL triggers a request to fonts.googleapis.com
on every page load. That request sends the visitor's IP address to Google —
a GDPR violation under German law for operators based in Germany.
Self-hosting eliminates this entirely.
