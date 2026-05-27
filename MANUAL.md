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
