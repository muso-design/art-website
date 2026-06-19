# Site Manual — Roman Chystakhovskyi Portfolio

The site is one HTML file (`index.html`) driven by four spreadsheet files.
You never need to touch `index.html`. Everything is controlled from the CSV files.

After any change: save the CSV → run `deploy.bat` → site updates on GitHub in ~30 seconds.
To preview locally: double-click `serve.bat`, then open http://localhost:8080.

---

## File overview

| File | What it controls |
|---|---|
| `settings.csv` | Colors, fonts, sizes, spacing, slideshow images, site name |
| `works.csv` | Every artwork — one row per piece |
| `bio.csv` | Bio page text, paragraphs, portrait photo, details sidebar |
| `contact.csv` | Contact page intro text and contact list items |
| `images/` | All your image files go here |
| `serve.bat` | Double-click to start a local preview server |
| `deploy.bat` | Double-click to push changes to GitHub (site goes live) |

---

## How to open and edit a CSV

Open any `.csv` file in **Excel** or **Google Sheets** (drag and drop it).
- The `key` column tells the site what setting this is — **never rename it**
- The `value` column is the one you edit
- The `description` column explains what each setting does — read it, but you don't have to touch it
- Any row whose key starts with `#` is a comment — it's ignored by the site and is there just to help you navigate the file

**Important when saving from Excel:** Save As → CSV UTF-8 (Comma delimited). Not "CSV (MS-DOS)" or "CSV (Macintosh)".

---

## Adding an artwork

1. Open `works.csv` in your spreadsheet app
2. Add a new row at the bottom (or wherever you want it to appear — order in the file = order on site)
3. Fill in the columns:

| Column | What to write |
|---|---|
| `id` | Any unique code for yourself, not shown on site. E.g. `002` |
| `title` | Artwork title |
| `series` | Series name — leave empty if none |
| `year` | Year created |
| `material` | E.g. `Polymer clay, resin cast` |
| `dimensions` | E.g. `40 × 30 × 28 cm` |
| `description` | Optional longer text shown in the lightbox. Can be multiple sentences. |
| `image` | Path to the image. E.g. `images/mywork.webp` |
| `available` | `Available` / `Sold` / `NFS` / `On loan` — or leave empty |

4. Put the image file in the `images/` folder
5. Save the CSV and run `deploy.bat`

**Image tips:** WebP or JPEG, 2000px on the longest side, 80% quality. Use [squoosh.app](https://squoosh.app) to compress before uploading.

---

## Adding a slideshow image (home page)

Open `settings.csv`. Find the `slideshow_1` row — it already has the first image.
To add more slides, fill in `slideshow_2`, `slideshow_3`, etc.
To add a caption under a slide, fill in `slideshow_caption_1`, `slideshow_caption_2`, etc.
To remove a slide, delete the row or clear the value.

**Two slideshow touches** (in `settings.csv`, on/off with `yes` / `no`):
- `slideshow_hint` (default `yes`) — a faint `‹ ›` hint on the first slide showing it can be swiped. It disappears for good after the first swipe, arrow, or auto-advance.
- `slideshow_caption_links` (default `yes`) — if a slide's caption matches an artwork title, the caption becomes a link that opens that piece. Captions that don't match a work stay plain text.

The home page scrolls down past the slideshow to a dark section that pairs your **name + © line + email/Instagram icons** (taken from `contact.csv`) on the left with a **newsletter signup** on the right. The signup uses the same `newsletter_*` settings as the Contact page — set `newsletter_action` to your provider's form URL (or `/subscribe` for local testing) to make it submit. Until then the form shows a friendly "not live yet" note. Knobs in `settings.csv`:
- `home_newsletter` (default `yes`) — show that whole bottom block on the home page. `no` hides it and keeps home a single screen.
- `newsletter_collect_name` (default `yes`) — also ask for the subscriber's name (so you know how to address them). `no` = email only. `newsletter_name_field` sets the field name your provider expects (often `name` or `first_name`).
- `newsletter_gradient_height` (default `34vh`) — how tall the fade is where the photo blends into the newsletter section (taller = softer).
- `nav_blur` (default `14px`) — frosted-glass blur behind the top nav bar, including over the home photo. `0px` turns it off. (Desktop only — off on phones.)
- `nav_blur_height` (default `110px`) — how far down that blur reaches; it feathers out softly at the bottom (no hard edge), so taller = a longer fade.

---

## Changing colors

Open `settings.csv`. Find the `# COLORS` section. Change the value in the `color_*` rows.
Any valid CSS color works:
- Hex: `#eceae5`
- RGB: `rgb(236, 234, 229)`
- Named: `white`, `black`, `ivory`

---

## Changing font

Open `settings.csv`. Find the `# FONT` section.

**To use a Google Font:**
1. Go to [fonts.google.com](https://fonts.google.com)
2. Pick a font → "Get font" → "Get embed code" → copy the `<link>` href URL
3. Paste that URL into `font_url`
4. Copy the CSS family string (e.g. `"Playfair Display", serif`) into `font_family`

**To use system fonts** — clear `font_url` and set `font_family` to:
`system-ui, -apple-system, sans-serif`

**`font_family` vs `font_family_display`** — `font_family` is the main font used everywhere; `font_family_display` is a second "display" font used *only* for the big name in the top-left and the artwork title in the lightbox (it's set to Cormorant Garamond, which is already self-hosted). Leave `font_family_display` empty to use the main font everywhere instead.

**Self-hosting a new font** (so no data goes to Google — required in Germany): run `python scripts/get-font.py "Font Name"`, then set `font_family` to what it prints. This swaps the *main* font; the display font (Cormorant) is preserved automatically.

---

## Changing font sizes

Open `settings.csv`. Find the `# FONT SIZES` section.
Change the value of any `font_size_*` row. Use `px` units. Examples:
- `18px` — smaller
- `24px` — larger
- `clamp(16px, 2vw, 22px)` — responsive (scales with screen width)

---

## Changing spacing

Open `settings.csv`. Find the `# SPACING` section.
- `spacing_page_padding` — left/right margin on all pages
- `spacing_grid_gap` — space between artwork cards

---

## Changing works grid columns

Open `settings.csv`. Find `grid_columns`. Set it to `2` or `3`.
On mobile the grid automatically reduces to fewer columns regardless.

---

## Series (grouping works)

Each artwork's `series` (in `works.csv`) groups it. When you have **two or more
different series**, an **All / <series> …** filter bar appears at the top of the
Works page automatically — built from whatever series you've typed, in the order
they first appear. Clicking a series shows just those pieces (and the next/prev
arrows inside a piece stay within that series).

- Spell a series the **same way every time** so pieces group together (e.g. always `Variants of love`).
- With only one series it stays a single grid (no bar).
- Turn the bar off entirely with `series_filter` = `no` in `settings.csv`.

---

## Analytics & Search Console

- **Cloudflare Web Analytics** (cookieless, GDPR-friendly — no consent banner): in your Cloudflare dashboard → Web Analytics → your site, copy the token from the snippet (`data-cf-beacon='{"token":"…"}'`) and paste just that token into `cloudflare_analytics_token` in `settings.csv`. Empty = off. The privacy policy already discloses it.
- **Google Search Console** is verified by a meta tag already in the page — nothing to set. In Search Console, submit your sitemap once: `sitemap.xml`.

---

## Link preview image

The picture shown when your site is shared (WhatsApp, iMessage, X, etc.) is
`images/og-image.jpg`, 1200×630. To change it, replace that file (keep the same
name and size). JPG/PNG is safest — some apps don't render WebP previews.

---

## Motion & animation

Open `settings.csv`, `# MOTION` section. Three on/off knobs (`yes` / `no`):

- `motion_reveal` (default `yes`) — artworks and lightbox images fade and gently lift in as they scroll into view.
- `motion_route_fade` (default `yes`) — pages cross-fade when you switch between Works / Bio / Contact.
- `motion_kenburns` (default `no`) — a slow drifting zoom on the home slideshow photos. Set to `yes` to try it.

Two finishing touches are always on (no setting needed): nav links draw an underline on hover and on the current page, and the artwork viewer fades open and closed.

**Accessibility:** every animation above turns itself off automatically for visitors who have "reduce motion" enabled in their device settings — nothing for you to do.

---

## Updating bio text

Open `bio.csv`. Find the `bio_1`, `bio_2`, etc. rows. Edit the values.
To add a new paragraph, add a new row: key = `bio_5` (or the next number), value = your text.
To remove a paragraph, delete the row or clear the value.

**Portrait photo:** Set the `photo` key to the path of your portrait image, e.g. `images/portrait.webp`.

**Details sidebar** (Born, Education, etc.): Edit `detail_label_N` and `detail_value_N` rows.
Add more by continuing the sequence: `detail_label_6` / `detail_value_6`, etc.

---

## Updating contact info

Open `contact.csv`.
- `intro` — the sentence at the top of the contact page
- `item_label_N` — label on the left (e.g. `Email`)
- `item_value_N` — text on the right (e.g. `roman@example.com`)
- `item_link_N` — optional URL; use `mailto:roman@example.com` for email, `https://…` for links

To add a contact row, add rows `item_label_4`, `item_value_4`, `item_link_4` (continue the number).

---

## Writing long text in a cell

If your text contains a **comma**, wrap the whole cell in double quotes:
`"For exhibition proposals, acquisition enquiries, or studio visits."`

If your text contains a **double quote**, write it as two quotes inside the wrapper:
`"He said ""yes"" to the commission."`

Excel and Google Sheets handle this automatically when you type directly into a cell.

---

## Responsive images (automatic — nothing to do)

Your photos are large (great for quality), but a phone doesn't need the full-size
file to show a small thumbnail. So every time you run `deploy.bat`, the site
automatically makes smaller versions of each image (480, 800 and 2000px wide) and
serves the right size for each visitor's screen. A phone ends up loading a ~20 KB
thumbnail instead of a 1.4 MB original — the gallery opens almost instantly.

**What you do: nothing.** Keep working exactly as before — drop a file in
`images/`, write its path in the CSV. The rest is handled for you.

A few things worth knowing:
- The smaller versions are saved next to your originals with names like
  `mywork_w800.webp`. **Don't delete them and don't list them in any CSV** —
  they're managed automatically. (A list of them lives in `images/variants.json`,
  which is also generated for you.)
- If you add a new image and preview it *before* deploying, it still shows
  correctly — just at full size until `deploy.bat` builds the smaller versions.
- Want the very smallest files (AVIF format)? Once, in a terminal, run
  `pip install pillow-avif-plugin` — then every future deploy adds AVIF on top
  automatically. Until then the site uses WebP + JPEG, which is already a big win.

---

## Deploying to GitHub (making the site live)

1. Double-click `deploy.bat`
2. Type a short commit message when prompted (or press Enter for the default)
3. The site updates on GitHub in about 30 seconds

---

## Quick reference

| Goal | File | What to change |
|---|---|---|
| Add an artwork | `works.csv` | New row with image path and details |
| Add a slideshow image | `settings.csv` | `slideshow_2`, `slideshow_3`, … |
| Change site name | `settings.csv` | `site_name` |
| Change background color | `settings.csv` | `color_background` |
| Change body font size | `settings.csv` | `font_size_body` |
| Change font | `settings.csv` | `font_url` + `font_family` |
| Change grid to 2 columns | `settings.csv` | `grid_columns` → `2` |
| Edit bio paragraphs | `bio.csv` | `bio_1`, `bio_2`, … |
| Add a detail row (bio) | `bio.csv` | `detail_label_N` + `detail_value_N` |
| Change contact email | `contact.csv` | `item_value_1` + `item_link_1` |
| Add a contact row | `contact.csv` | `item_label_4`, `item_value_4`, `item_link_4` |
