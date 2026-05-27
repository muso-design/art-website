// ═══════════════════════════════════════════════════════════════════════════
//  config.js — Roman Chystakhovskyi Portfolio
//  Everything you need to manage your site is in this file.
//  After any change: save → upload to GitHub → done.
// ═══════════════════════════════════════════════════════════════════════════


const CONFIG = {


  // ─────────────────────────────────────────────────────────────────────────
  //  IDENTITY
  // ─────────────────────────────────────────────────────────────────────────
  name:     "Roman Chystakhovskyi",
  role:     "Sculptor",
  location: "Leipzig, Germany",
  year:     "2025",


  // ─────────────────────────────────────────────────────────────────────────
  //  SEO — affects search engines and link previews (Instagram, email, etc.)
  // ─────────────────────────────────────────────────────────────────────────
  seo: {
    titleFormat:   "{page} — Roman Chystakhovskyi",  // {page} = Works, Bio, etc.
    titleHome:     "Roman Chystakhovskyi — Sculptor",
    description:   "Figurative sculptor working in polymer clay and resin. Based in Leipzig, Germany.",
    ogImage:       "images/og-cover.jpg",  // image shown when sharing your URL (1200x630px recommended)
    ogImageAlt:    "Roman Chystakhovskyi — Sculptor",
  },


  // ─────────────────────────────────────────────────────────────────────────
  //  NAVIGATION
  // ─────────────────────────────────────────────────────────────────────────
  nav: {
    // Set to false to hide a page from the nav entirely
    showWorks:   true,
    showBio:     true,
    showContact: true,
  },


  // ─────────────────────────────────────────────────────────────────────────
  //  COLORS
  // ─────────────────────────────────────────────────────────────────────────
  colors: {
    background:        "#eceae5",  // main page background
    surface:           "#e3e1db",  // grid cards, series blocks
    surfaceHover:      "#d6d3cc",  // hover state on cards
    text:              "#1a1814",  // primary text
    textMid:           "#6e6b64",  // secondary text (descriptions, meta)
    textDim:           "#a09d96",  // labels, captions, footer
    border:            "rgba(26,24,20,0.1)",

    // Lightbox
    lightboxBackground:"#eceae5",  // can differ from page bg

    // Grid hover overlay (darkens image on hover)
    gridHoverColor:    "rgba(26,24,20,0.07)",

    // Nav on hero (light = visible over dark photo)
    heroNavColor:      "#f0ede8",
    heroNavOpacity:    "0.5",      // opacity of nav links over hero
  },


  // ─────────────────────────────────────────────────────────────────────────
  //  TYPOGRAPHY
  //  Sizes: any CSS value — "16px", "1.2rem", "clamp(14px, 2vw, 20px)"
  //  Weight: 300 (thin), 400 (normal), 500 (medium), 600 (semibold)
  //  Italic: true / false
  //  Transform: "uppercase" / "none"
  //  Spacing: letter-spacing in em, e.g. "0.1em" — use "0em" for none
  // ─────────────────────────────────────────────────────────────────────────
  typography: {

    nav: {
      nameSize:      "13px",
      nameWeight:    500,
      nameItalic:    false,
      nameSpacing:   "0.2em",
      nameTransform: "uppercase",

      linkSize:      "11px",
      linkWeight:    500,
      linkItalic:    false,
      linkSpacing:   "0.22em",
      linkTransform: "uppercase",
    },

    // Piece title below grid image
    gridTitle: {
      size:      "22px",
      weight:    400,
      italic:    true,
      spacing:   "0.01em",
      transform: "none",
    },

    // Series label below grid title (e.g. "Variants of Love")
    gridSeries: {
      size:      "12px",
      weight:    500,
      italic:    false,
      spacing:   "0.18em",
      transform: "uppercase",
    },

    // Huge series names on the Works page
    seriesName: {
      size:      "clamp(48px, 6vw, 80px)",
      weight:    400,
      italic:    true,
      spacing:   "0.01em",
      transform: "none",
    },

    // Series description text on Works page
    seriesBody: {
      size:      "18px",
      weight:    400,
      italic:    false,
      spacing:   "0em",
      transform: "none",
    },

    // Bio paragraphs
    bioText: {
      size:      "20px",
      weight:    400,
      italic:    true,
      spacing:   "0em",
      transform: "none",
    },

    // Bio aside details (Born, Education, etc.)
    bioDetail: {
      size:      "17px",
      weight:    400,
      italic:    true,
      spacing:   "0em",
      transform: "none",
    },

    // Lightbox title (piece name)
    lightboxTitle: {
      size:      "34px",
      weight:    400,
      italic:    true,
      spacing:   "0em",
      transform: "none",
    },

    // Lightbox metadata (year, medium, dimensions)
    lightboxMeta: {
      size:      "16px",
      weight:    400,
      italic:    false,
      spacing:   "0.04em",
      transform: "none",
    },

    // All small section labels, footer, captions
    label: {
      size:      "11px",
      weight:    500,
      italic:    false,
      spacing:   "0.26em",
      transform: "uppercase",
    },

    // Contact page body text
    contactText: {
      size:      "20px",
      weight:    400,
      italic:    true,
      spacing:   "0em",
      transform: "none",
    },

    // Contact links (email, instagram)
    contactLink: {
      size:      "18px",
      weight:    400,
      italic:    true,
      spacing:   "0em",
      transform: "none",
    },
  },


  // ─────────────────────────────────────────────────────────────────────────
  //  SPACING
  // ─────────────────────────────────────────────────────────────────────────
  spacing: {
    pagePadding:     "56px",   // left/right margin on all pages
    gridGap:         "28px",   // gap between grid items
    gridPadding:     "28px",   // padding around the grid
    gridCardPadding: "20px",   // padding inside card, between image and title
    sectionGap:      "64px",   // gap between page sections
  },


  // ─────────────────────────────────────────────────────────────────────────
  //  GRID
  // ─────────────────────────────────────────────────────────────────────────
  grid: {
    columns:     3,             // 2 or 3
    aspectRatio: "1/1",         // "1/1" square | "4/5" portrait | "16/9" landscape
    sortBy:      "manual",      // "manual" | "year-desc" | "year-asc" | "series"
    showSeries:  true,          // show series section on Works page
    showAllWorks:true,          // show all works grid below series
  },


  // ─────────────────────────────────────────────────────────────────────────
  //  HERO (landing page slideshow)
  //  Add images to your images/ folder, then list them here.
  //  Each slide needs: image path and caption.
  // ─────────────────────────────────────────────────────────────────────────
  hero: {
    slides: [
      { image: "images/too_much.jpg",  caption: "Too Much, 2024" },
      { image: "",                     caption: "" },  // replace with your image
      { image: "",                     caption: "" },  // replace with your image
    ],
    interval:      5500,   // milliseconds between slides
    transition:    2000,   // fade duration in milliseconds
  },


  // ─────────────────────────────────────────────────────────────────────────
  //  LIGHTBOX
  // ─────────────────────────────────────────────────────────────────────────
  lightbox: {
    showYear:       true,
    showMedium:     true,
    showDimensions: true,
    showEdition:    true,   // e.g. "Edition 3 of 8"
    showStatus:     true,   // Available / Sold / NFS
    showPrice:      false,  // set to true when you're ready to sell
  },


  // ─────────────────────────────────────────────────────────────────────────
  //  FOOTER
  // ─────────────────────────────────────────────────────────────────────────
  footer: {
    show:        true,
    leftText:    "",       // leave empty to auto-generate "© 2025 Roman Chystakhovskyi"
    rightText:   "",       // leave empty to use location from identity above
  },


  // ─────────────────────────────────────────────────────────────────────────
  //  CONTACT
  // ─────────────────────────────────────────────────────────────────────────
  contact: {
    email:        "your@email.com",
    instagram:    "@yourhandle",
    instagramUrl: "https://instagram.com/yourhandle",
    intro:        "For exhibition proposals, acquisition enquiries, or studio visits — get in touch.",
  },


  // ─────────────────────────────────────────────────────────────────────────
  //  BIO
  // ─────────────────────────────────────────────────────────────────────────
  bio: {
    paragraphs: [
      "Roman Chystakhovskyi is a figurative sculptor working at the threshold between physical and digital material. His practice explores the human body as a site of psychological tension — presence, vulnerability, and the weight of emotion made tangible in form.",
      "Trained at the National Academy of Fine Arts and Architecture in Kyiv, Roman brings a classical foundation to a contemporary sensibility. His sculptures are hand-built in polymer clay and cast in resin, each piece emerging from an extended process of observation and psychological excavation.",
      "His series Variants of Love — acquired by Vincent Van Dyke Effects — marked a defining moment in his fine art practice: an investigation into the forms love takes when it overwhelms, consumes, or dissolves the self.",
      "Alongside his sculpture practice, Roman works as a senior 3D character and creature artist with credits at Blizzard, NetEase, and Romero Games. He lives and works in Leipzig, Germany.",
    ],
    details: [
      { label: "Born",        value: "1997, Ukraine" },
      { label: "Education",   value: "National Academy of Fine Arts and Architecture, Kyiv" },
      { label: "Based",       value: "Leipzig, Germany" },
      { label: "Collections", value: "Vincent Van Dyke Effects — Variants of Love" },
      { label: "Materials",   value: "Polymer clay, resin cast, bronze (forthcoming)" },
    ],
  },


  // ─────────────────────────────────────────────────────────────────────────
  //  SERIES
  //  Order here = order on the Works page.
  // ─────────────────────────────────────────────────────────────────────────
  series: [
    {
      name:        "Réflexions",
      meta:        "Ongoing — Polymer clay",
      description: "An inward turn — studies of the self in states of stillness, introspection, and quiet dissolution. Forms that hold their breath.",
    },
    {
      name:        "Songs",
      meta:        "Ongoing — Polymer clay",
      description: "Figures suspended in resonance — bodies as instruments, gestures as melody. Each piece a posture caught mid-phrase.",
    },
    {
      name:        "Variants of Love",
      meta:        "2022–2024 — Acquired by VVDE",
      description: "An investigation into the forms love takes when it overwhelms, consumes, or dissolves the self. The series that defined a turning point.",
    },
  ],


  // ─────────────────────────────────────────────────────────────────────────
  //  WORKS
  //  This is your full portfolio. Add a new block for each piece.
  //
  //  image:      path to your file, e.g. "images/too_much.jpg"
  //  title:      piece name
  //  year:       e.g. "2024"
  //  medium:     e.g. "Polymer clay, resin cast"
  //  dimensions: e.g. "60 × 60 cm"
  //  series:     must match exactly a name in the series list above,
  //              or leave "" for standalone works
  //  edition:    e.g. "Edition 1 of 8" — leave "" if not applicable
  //  status:     "available" | "sold" | "nfs" (not for sale)
  //  price:      e.g. "€2,400" — only shown if lightbox.showPrice is true
  //  order:      number — controls manual sort order (lower = first)
  // ─────────────────────────────────────────────────────────────────────────
  works: [
    {
      image:      "images/too_much.jpg",
      title:      "Too Much",
      year:       "2024",
      medium:     "Polymer clay, resin cast",
      dimensions: "60 × 60 cm",
      series:     "Variants of Love",
      edition:    "",
      status:     "sold",
      price:      "",
      order:      1,
    },

    // ── Add your pieces below, copy the block above ──
    {
      image:      "",
      title:      "Title",
      year:       "",
      medium:     "",
      dimensions: "",
      series:     "",
      edition:    "",
      status:     "available",
      price:      "",
      order:      2,
    },
    {
      image:      "",
      title:      "Title",
      year:       "",
      medium:     "",
      dimensions: "",
      series:     "",
      edition:    "",
      status:     "available",
      price:      "",
      order:      3,
    },
    {
      image:      "",
      title:      "Title",
      year:       "",
      medium:     "",
      dimensions: "",
      series:     "",
      edition:    "",
      status:     "available",
      price:      "",
      order:      4,
    },
  ],


};  // ← end of CONFIG — don't delete this


// ═══════════════════════════════════════════════════════════════════════════
//  INTERNALS — you don't need to touch anything below this line
// ═══════════════════════════════════════════════════════════════════════════

(function applyTheme() {
  const r = document.documentElement.style;
  const c = CONFIG.colors;
  const t = CONFIG.typography;
  const s = CONFIG.spacing;
  const g = CONFIG.grid;

  // Colors
  r.setProperty('--bg',              c.background);
  r.setProperty('--bg2',             c.surface);
  r.setProperty('--bg3',             c.surfaceHover);
  r.setProperty('--text',            c.text);
  r.setProperty('--mid',             c.textMid);
  r.setProperty('--dim',             c.textDim);
  r.setProperty('--border',          c.border);
  r.setProperty('--lb-bg',           c.lightboxBackground);
  r.setProperty('--grid-hover',      c.gridHoverColor);
  r.setProperty('--hero-nav',        c.heroNavColor);
  r.setProperty('--hero-nav-opacity',c.heroNavOpacity);

  // Typography helper
  function applyType(prefix, obj) {
    r.setProperty(`--${prefix}-size`,      obj.size);
    r.setProperty(`--${prefix}-weight`,    obj.weight);
    r.setProperty(`--${prefix}-italic`,    obj.italic ? 'italic' : 'normal');
    r.setProperty(`--${prefix}-spacing`,   obj.spacing);
    r.setProperty(`--${prefix}-transform`, obj.transform);
  }
  applyType('nav-name',    t.nav);
  applyType('nav-link',    { size: t.nav.linkSize, weight: t.nav.linkWeight,
                             italic: t.nav.linkItalic, spacing: t.nav.linkSpacing,
                             transform: t.nav.linkTransform });
  applyType('grid-title',  t.gridTitle);
  applyType('grid-series', t.gridSeries);
  applyType('series-name', t.seriesName);
  applyType('series-body', t.seriesBody);
  applyType('bio-text',    t.bioText);
  applyType('bio-detail',  t.bioDetail);
  applyType('lb-title',    t.lightboxTitle);
  applyType('lb-meta',     t.lightboxMeta);
  applyType('label',       t.label);
  applyType('contact-text',t.contactText);
  applyType('contact-link',t.contactLink);

  // Spacing
  r.setProperty('--page-padding',      s.pagePadding);
  r.setProperty('--grid-gap',          s.gridGap);
  r.setProperty('--grid-padding',      s.gridPadding);
  r.setProperty('--grid-card-padding', s.gridCardPadding);
  r.setProperty('--section-gap',       s.sectionGap);

  // Grid
  r.setProperty('--grid-columns',      g.columns);
  r.setProperty('--grid-aspect',       g.aspectRatio);
})();


function _sortWorks(works) {
  const s = CONFIG.grid.sortBy;
  if (s === 'year-desc') return [...works].sort((a,b) => (b.year||0) - (a.year||0));
  if (s === 'year-asc')  return [...works].sort((a,b) => (a.year||0) - (b.year||0));
  if (s === 'series')    return [...works].sort((a,b) => a.series.localeCompare(b.series));
  return [...works].sort((a,b) => (a.order||99) - (b.order||99));
}

function _statusLabel(status) {
  if (status === 'sold') return '<span class="status sold">Sold</span>';
  if (status === 'nfs')  return '<span class="status nfs">Not for sale</span>';
  return '<span class="status available">Available</span>';
}

function renderNav() {
  document.querySelectorAll('.nav-name').forEach(el => el.textContent = CONFIG.name);
  const n = CONFIG.nav;
  ['works','bio','contact'].forEach(page => {
    const link = document.querySelector(`.nav-links a[href="${page}.html"]`);
    if (link) link.style.display = n['show' + page.charAt(0).toUpperCase() + page.slice(1)] ? '' : 'none';
  });
}

function renderSeries() {
  const el = document.getElementById('series-rows');
  if (!el) return;
  el.innerHTML = CONFIG.series.map(s => `
    <div class="series-row">
      <h3>${s.name}</h3>
      <span class="series-meta">${s.meta}</span>
      <p>${s.description}</p>
    </div>
  `).join('');
  const section = document.getElementById('series-section');
  if (section) section.style.display = CONFIG.grid.showSeries ? '' : 'none';
}

function renderWorks() {
  const el = document.getElementById('grid');
  if (!el) return;
  const sorted = _sortWorks(CONFIG.works);
  el.style.gridTemplateColumns = `repeat(${CONFIG.grid.columns}, 1fr)`;
  el.innerHTML = sorted.map((w, i) => `
    <div class="grid-item"
      data-title="${w.title}"
      data-year="${w.year}"
      data-medium="${w.medium}"
      data-dimensions="${w.dimensions}"
      data-series="${w.series}"
      data-edition="${w.edition}"
      data-status="${w.status}"
      data-price="${w.price}"
      data-index="${i}"
    >
      ${w.image
        ? `<img class="grid-thumb" src="${w.image}" alt="${w.title}" />`
        : `<div class="grid-placeholder"><span>image</span></div>`
      }
      <div class="grid-meta">
        <div class="title">${w.title}</div>
        ${w.series ? `<div class="series">${w.series}</div>` : ''}
      </div>
    </div>
  `).join('');
  const allSection = document.getElementById('all-works-section');
  if (allSection) allSection.style.display = CONFIG.grid.showAllWorks ? '' : 'none';
}

function renderBio() {
  const textEl  = document.getElementById('bio-text');
  const asideEl = document.getElementById('bio-aside');
  if (textEl)  textEl.innerHTML  = CONFIG.bio.paragraphs.map(p => `<p>${p}</p>`).join('');
  if (asideEl) asideEl.innerHTML = CONFIG.bio.details.map(d =>
    `<div><dt>${d.label}</dt><dd>${d.value}</dd></div>`).join('');
}

function renderContact() {
  const set = (id, val) => { const el = document.getElementById(id); if (el) el.textContent = val; };
  const setHref = (id, href) => { const el = document.getElementById(id); if (el) el.href = href; };
  set('contact-intro', CONFIG.contact.intro);
  set('contact-email', CONFIG.contact.email);
  setHref('contact-email', 'mailto:' + CONFIG.contact.email);
  set('contact-ig', CONFIG.contact.instagram);
  setHref('contact-ig', CONFIG.contact.instagramUrl);
  set('contact-loc', CONFIG.location);
}

function renderFooter() {
  const c = CONFIG.footer;
  const left  = c.leftText  || `© ${CONFIG.year} ${CONFIG.name}`;
  const right = c.rightText || CONFIG.location;
  document.querySelectorAll('.footer-name').forEach(el => el.textContent = left);
  document.querySelectorAll('.footer-loc').forEach(el  => el.textContent = right);
  if (!c.show) document.querySelectorAll('footer').forEach(el => el.style.display = 'none');
}

function renderHero() {
  const container = document.getElementById('slideshow');
  if (!container) return;
  const slides = CONFIG.hero.slides.filter(s => s.image);
  if (!slides.length) return;
  container.innerHTML = slides.map((s, i) => `
    <div class="slide${i===0?' active':''}">
      <img src="${s.image}" alt="${s.caption}" />
    </div>
  `).join('');
  const caps = slides.map(s => s.caption);
  const capEl = document.getElementById('cap');
  const slideEls = Array.from(container.querySelectorAll('.slide'));
  if (capEl) capEl.textContent = caps[0] || '';
  let cur = 0;
  if (slideEls.length > 1) {
    setInterval(() => {
      slideEls[cur].classList.remove('active');
      cur = (cur + 1) % slideEls.length;
      slideEls[cur].classList.add('active');
      if (capEl) capEl.textContent = caps[cur] || '';
    }, CONFIG.hero.interval);
  }
}

function renderLightboxItem(el) {
  const lb = CONFIG.lightbox;
  const d  = el.dataset;
  document.getElementById('lb-title').textContent = d.title || '';

  const meta = document.getElementById('lb-meta');
  if (!meta) return;
  let html = '';
  if (lb.showYear      && d.year)       html += `<span>${d.year}</span>`;
  if (lb.showMedium    && d.medium)     html += `<span>${d.medium}</span>`;
  if (lb.showDimensions&& d.dimensions) html += `<span>${d.dimensions}</span>`;
  if (lb.showEdition   && d.edition)    html += `<span>${d.edition}</span>`;
  if (lb.showStatus    && d.status)     html += _statusLabel(d.status);
  if (lb.showPrice     && d.price)      html += `<span class="price">${d.price}</span>`;
  meta.innerHTML = html;

  const series = document.getElementById('lb-series');
  if (series) series.textContent = d.series || '';
}

document.addEventListener('DOMContentLoaded', () => {
  renderNav();
  renderSeries();
  renderWorks();
  renderBio();
  renderContact();
  renderFooter();
  renderHero();
});
