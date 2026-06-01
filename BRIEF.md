# Site requirements — non-negotiable baseline

Roman Chystakhovskyi portfolio site. Static HTML/CSS/JS, no build step,
CSV-driven content, deployed via GitHub Pages, primary audience is galleries
and collectors. Read this file before every change. If a change would break
any item below, it is wrong even if it works visually.

## Architecture rules
- Single `index.html` with CSS and JS inline (no bundlers, no npm dependencies)
- Content driven by `settings.csv`, `works.csv`, `bio.csv`, `contact.csv`
- Image files live in `/images/`, fonts in `/fonts/`, helper scripts in `/scripts/`
- Deployment: `deploy.bat` (git add + commit + push). GitHub Pages serves the repo.
- Hash routing (`/#/works`, `/#/bio`, `/#/works/<slug>`). No server-side routing.

## Legal (German jurisdiction — Roman is a Freiberufler in Leipzig)
- `impressum.html` page linked from footer, complete per § 5 DDG
- `datenschutz.html` page linked from footer
- All fonts self-hosted from `/fonts/` — no external Google Fonts requests
- No third-party scripts without a corresponding privacy policy entry
- No cookies set unless they are strictly necessary

## SEO + social sharing
- Static `<title>` and `<meta name="description">` in HTML — must be valid even
  if JavaScript fails to run
- OpenGraph: og:title, og:description, og:image, og:url, og:type, og:site_name
- Twitter Card: twitter:card (summary_large_image), twitter:image, twitter:title,
  twitter:description
- Canonical link tag per page state
- JSON-LD `Person` schema in `<head>`, plus `VisualArtwork` schema for individual
  works when on a piece detail route
- `robots.txt` and `sitemap.xml` in repo root
- Branded `404.html`

## Site identity
- Full favicon set: `favicon.ico`, `favicon.svg`, `favicon-32.png`,
  `apple-touch-icon.png` (180×180)
- `site.webmanifest` with name, icons, theme_color
- `<meta name="theme-color">` matching site background
- `og-image.png` at 1200×630 in `/images/`

## Performance
- All `<img>` tags have `width` and `height` attributes (prevents CLS)
- Hero / first-paint image uses `<link rel="preload" as="image">`
- Images served via `<picture>` with AVIF + WebP + JPEG fallback
- At least two sizes per image (800w for mobile, 2000w for desktop) via srcset
- Lighthouse score ≥ 90 on Performance, Accessibility, Best Practices, SEO

## Accessibility
- Visible `:focus-visible` styles on all interactive elements
- Skip-to-content link as the first focusable element on every page
- Exactly one `<h1>` per page state; no skipped heading levels
- All animations respect `@media (prefers-reduced-motion: reduce)`
- Color contrast meets WCAG AA (4.5:1 body text, 3:1 large text)
- `<noscript>` fallback explains the site requires JavaScript

## Resilience
- CSV validator script runs before deploy and fails on missing required fields
  or missing image files
- Image optimization script runs before deploy and produces AVIF + WebP +
  responsive sizes from a `/images/raw/` source folder
- Broken-image fallback: if an artwork image 404s in production, show a neutral
  placeholder, not the browser's broken-image icon

## Browser support
- Chrome / Edge / Safari / Firefox — last 2 major versions
- iOS Safari — last 2 versions
- Mobile Chrome / Samsung Internet — last 2 versions
- No IE11

## Forbidden
- npm dependencies or build steps without explicit prior approval
- Google Fonts loaded from `fonts.googleapis.com` (GDPR violation in DE)
- Google Analytics, Meta Pixel, or any tracking that requires a cookie banner
- Cookie banners unless legally required
- Right-click disabling on images
- Replacing CSV-driven content with hardcoded HTML
- Adding `<form>` elements that POST anywhere without a privacy policy update
