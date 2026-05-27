# Site Manual — Roman Chystakhovskyi Portfolio

Everything is controlled from **config.js**.
After any change: save the file → upload to GitHub → site updates in ~30 seconds.
You never need to touch the HTML files.

---

## How to upload a change

1. Go to your GitHub repo
2. Click `config.js`
3. Click the pencil icon (Edit)
4. Make your change
5. Click **Commit changes**

Or: edit locally in any text editor, then drag the file into the repo page.

---

## Adding a new work

Find the `works: [` section in config.js. Copy this block and fill it in:

```js
{
  image:      "images/your-file.jpg",   // put the photo in your images/ folder
  title:      "Piece Title",
  year:       "2024",
  medium:     "Polymer clay, resin cast",
  dimensions: "40 × 30 cm",
  series:     "Réflexions",             // must match a series name exactly, or leave ""
  edition:    "Edition 1 of 8",         // leave "" if not applicable
  status:     "available",              // "available" | "sold" | "nfs"
  price:      "€1,800",                 // only shown if lightbox.showPrice is true
  order:      5,                        // controls position in grid (lower = first)
},
```

**To upload the image:** go to your GitHub repo → Add file → Upload files → drag your JPEGs in → commit.
Put all images in an `images/` folder. Recommended size: 2000px on the longest side, JPEG at 80% quality.
Use squoosh.app to compress before uploading.

---

## Changing text sizes

Find the `typography:` section. Each element has its own `size` property:

```js
gridTitle:  { size: "22px", ... }   // piece title under grid image
seriesName: { size: "clamp(48px, 6vw, 80px)", ... }  // huge series names
bioText:    { size: "20px", ... }   // bio paragraphs
```

Change the number. `clamp(min, preferred, max)` = responsive size that scales with screen width.

---

## Changing text style (weight, italic, spacing)

Each typography block has:

```js
weight:    400,         // 300 thin | 400 normal | 500 medium
italic:    true,        // true = italic | false = normal
spacing:   "0.01em",    // letter-spacing. "0em" = none
transform: "none",      // "uppercase" | "none"
```

Example — make bio text non-italic and heavier:
```js
bioText: {
  size:      "20px",
  weight:    500,
  italic:    false,   // ← changed
  spacing:   "0em",
  transform: "none",
},
```

---

## Changing colors

Find the `colors:` section:

```js
colors: {
  background:   "#eceae5",  // main page background
  surface:      "#e3e1db",  // grid cards
  text:         "#1a1814",  // primary text
  textMid:      "#6e6b64",  // descriptions, meta text
  textDim:      "#a09d96",  // labels, captions
  ...
}
```

Use any CSS color: hex (`#1a1814`), rgb (`rgb(26,24,20)`), or named (`white`, `black`).

---

## Changing grid layout

```js
grid: {
  columns:     3,        // 2 or 3 columns
  aspectRatio: "1/1",    // "1/1" square | "4/5" portrait | "16/9" landscape
  sortBy:      "manual", // "manual" | "year-desc" | "year-asc" | "series"
  showSeries:  true,     // show/hide the series section on Works page
  showAllWorks:true,     // show/hide the all works grid
},
```

---

## Changing spacing

```js
spacing: {
  pagePadding:     "56px",  // left/right margin on all pages
  gridGap:         "28px",  // gap between grid items
  gridPadding:     "28px",  // padding around the grid
  gridCardPadding: "20px",  // space between image and text inside each card
  sectionGap:      "64px",  // space between sections on a page
},
```

---

## Hero slideshow

```js
hero: {
  slides: [
    { image: "images/too_much.jpg", caption: "Too Much, 2024" },
    { image: "images/another.jpg",  caption: "Another Piece, 2023" },
    { image: "",                    caption: "" },  // empty = skip this slide
  ],
  interval:   5500,   // time between slides in milliseconds (5500 = 5.5 seconds)
  transition: 2000,   // fade duration in milliseconds
},
```

Add as many slides as you want. Empty image slots are skipped automatically.

---

## Updating bio text

```js
bio: {
  paragraphs: [
    "First paragraph text here.",
    "Second paragraph text here.",
    // add more paragraphs as needed
  ],
  details: [
    { label: "Born",      value: "1997, Ukraine" },
    { label: "Education", value: "National Academy..." },
    // add or remove rows as needed
  ],
},
```

---

## Updating series

```js
series: [
  {
    name:        "Réflexions",
    meta:        "Ongoing — Polymer clay",
    description: "Description text here.",
  },
  // add or reorder series here — order here = order on the Works page
],
```

---

## Updating contact info

```js
contact: {
  email:        "your@email.com",
  instagram:    "@yourhandle",
  instagramUrl: "https://instagram.com/yourhandle",
  intro:        "For exhibition proposals...",
},
```

---

## Showing/hiding lightbox fields

```js
lightbox: {
  showYear:       true,
  showMedium:     true,
  showDimensions: true,
  showEdition:    true,
  showStatus:     true,   // shows Available / Sold / NFS
  showPrice:      false,  // set to true when ready to sell
},
```

---

## Enabling prices / shop

1. Set `lightbox: { showPrice: true }`
2. Add prices to each work: `price: "€1,800"`
3. Set status: `status: "available"` — shows green "Available" label in lightbox

Payment checkout integration comes later and requires additional setup.

---

## Hiding a page from navigation

```js
nav: {
  showWorks:   true,
  showBio:     false,   // ← hides Bio from nav
  showContact: true,
},
```

The page still exists at its URL, it just won't appear in the menu.

---

## SEO (search engines + link previews)

```js
seo: {
  titleFormat:  "{page} — Roman Chystakhovskyi",
  titleHome:    "Roman Chystakhovskyi — Sculptor",
  description:  "Figurative sculptor working in polymer clay and resin. Based in Leipzig, Germany.",
  ogImage:      "images/og-cover.jpg",   // shown when sharing your URL on social media
  ogImageAlt:   "Roman Chystakhovskyi — Sculptor",
},
```

For `ogImage`: create a 1200×630px JPEG of your best piece and upload it as `images/og-cover.jpg`.

---

## File structure in your GitHub repo

```
index.html       landing page
works.html       works + series
bio.html         bio
contact.html     contact
style.css        all visual styles
config.js        ← everything you edit lives here
MANUAL.md        this file
images/
  too_much.jpg   your photos go here
  og-cover.jpg   social media preview image
```

---

## Quick reference — most common changes

| What                        | Where in config.js              |
|-----------------------------|----------------------------------|
| Add a new piece             | `works: [` → copy a block        |
| Change bio text             | `bio.paragraphs`                 |
| Change email/instagram      | `contact.email` / `.instagram`   |
| Make text bigger            | `typography.X.size`              |
| Make text non-italic        | `typography.X.italic: false`     |
| Change background color     | `colors.background`              |
| Change grid to 2 columns    | `grid.columns: 2`                |
| Change grid to portrait     | `grid.aspectRatio: "4/5"`        |
| Reorder series              | drag blocks in `series: [`       |
| Hide a page from nav        | `nav.showBio: false`             |
| Show prices in lightbox     | `lightbox.showPrice: true`       |
| Add a hero slide            | `hero.slides: [` → add a block   |
