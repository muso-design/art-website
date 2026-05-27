// ═══════════════════════════════════════════════════════════════
//  SITE CONFIG — edit this file to update your site
//  Upload only this file to GitHub when making changes
// ═══════════════════════════════════════════════════════════════

const CONFIG = {

  // ── IDENTITY ──────────────────────────────────────────────
  name:     "Roman Chystakhovskyi",
  role:     "Sculptor",
  location: "Leipzig, Germany",
  year:     "2025",

  // ── CONTACT ───────────────────────────────────────────────
  email:     "your@email.com",
  instagram: "@yourhandle",
  instagramUrl: "https://instagram.com/yourhandle",

  // ── COLORS ────────────────────────────────────────────────
  colors: {
    background:  "#eceae5",   // page background
    surface:     "#e3e1db",   // grid item / card background
    surfaceHover:"#d6d3cc",   // hover state
    text:        "#1a1814",   // main text
    textMid:     "#6e6b64",   // secondary text
    textDim:     "#a09d96",   // labels, captions
    border:      "rgba(26,24,20,0.1)",
  },

  // ── TYPOGRAPHY ────────────────────────────────────────────
  fonts: {
    // Body & reading text
    bodySize:        "20px",     // bio paragraphs, series descriptions
    bodyLineHeight:  "1.88",

    // Grid
    gridTitleSize:   "22px",     // piece title under grid image
    gridSeriesSize:  "12px",     // series label under grid image

    // Works page — series names
    seriesNameSize:  "clamp(48px, 6vw, 80px)",

    // Lightbox
    lbTitleSize:     "34px",
    lbMetaSize:      "16px",

    // Navigation
    navNameSize:     "13px",
    navLinkSize:     "11px",

    // Labels (section headers, footers)
    labelSize:       "11px",
  },

  // ── SPACING ───────────────────────────────────────────────
  spacing: {
    gridGap:     "28px",   // gap between grid items
    gridPadding: "28px",   // padding around the grid
    pagePadding: "56px",   // left/right padding on all pages
  },

  // ── BIO TEXT ──────────────────────────────────────────────
  bio: [
    "Roman Chystakhovskyi is a figurative sculptor working at the threshold between physical and digital material. His practice explores the human body as a site of psychological tension — presence, vulnerability, and the weight of emotion made tangible in form.",
    "Trained at the National Academy of Fine Arts and Architecture in Kyiv, Roman brings a classical foundation to a contemporary sensibility. His sculptures are hand-built in polymer clay and cast in resin, each piece emerging from an extended process of observation and psychological excavation.",
    "His series Variants of Love — acquired by Vincent Van Dyke Effects — marked a defining moment in his fine art practice: an investigation into the forms love takes when it overwhelms, consumes, or dissolves the self.",
    "Alongside his sculpture practice, Roman works as a senior 3D character and creature artist with credits at Blizzard, NetEase, and Romero Games. He lives and works in Leipzig, Germany."
  ],

  bioDetails: [
    { label: "Born",       value: "1997, Ukraine" },
    { label: "Education",  value: "National Academy of Fine Arts and Architecture, Kyiv" },
    { label: "Based",      value: "Leipzig, Germany" },
    { label: "Collections",value: "Vincent Van Dyke Effects — Variants of Love" },
    { label: "Materials",  value: "Polymer clay, resin cast, bronze (forthcoming)" },
  ],

  // ── SERIES ────────────────────────────────────────────────
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

  // ── CONTACT PAGE TEXT ─────────────────────────────────────
  contactIntro: "For exhibition proposals, acquisition enquiries, or studio visits — get in touch.",

};

// ── Apply CSS variables from config ──────────────────────────
(function applyTheme() {
  const r = document.documentElement.style;
  const c = CONFIG.colors;
  const f = CONFIG.fonts;
  const s = CONFIG.spacing;

  r.setProperty('--bg',      c.background);
  r.setProperty('--bg2',     c.surface);
  r.setProperty('--bg3',     c.surfaceHover);
  r.setProperty('--text',    c.text);
  r.setProperty('--mid',     c.textMid);
  r.setProperty('--dim',     c.textDim);
  r.setProperty('--border',  c.border);

  r.setProperty('--body-size',        f.bodySize);
  r.setProperty('--body-lh',          f.bodyLineHeight);
  r.setProperty('--grid-title-size',  f.gridTitleSize);
  r.setProperty('--grid-series-size', f.gridSeriesSize);
  r.setProperty('--series-name-size', f.seriesNameSize);
  r.setProperty('--lb-title-size',    f.lbTitleSize);
  r.setProperty('--lb-meta-size',     f.lbMetaSize);
  r.setProperty('--nav-name-size',    f.navNameSize);
  r.setProperty('--nav-link-size',    f.navLinkSize);
  r.setProperty('--label-size',       f.labelSize);

  r.setProperty('--grid-gap',         s.gridGap);
  r.setProperty('--grid-padding',     s.gridPadding);
  r.setProperty('--page-padding',     s.pagePadding);
})();

// ── Render bio ────────────────────────────────────────────────
function renderBio() {
  const textEl = document.getElementById('bio-text');
  const asideEl = document.getElementById('bio-aside');
  if (textEl) {
    textEl.innerHTML = CONFIG.bio
      .map(p => `<p>${p}</p>`)
      .join('');
  }
  if (asideEl) {
    asideEl.innerHTML = CONFIG.bioDetails
      .map(d => `<div><dt>${d.label}</dt><dd>${d.value}</dd></div>`)
      .join('');
  }
}

// ── Render series ─────────────────────────────────────────────
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
}

// ── Render contact ────────────────────────────────────────────
function renderContact() {
  const intro = document.getElementById('contact-intro');
  const email = document.getElementById('contact-email');
  const ig    = document.getElementById('contact-ig');
  const loc   = document.getElementById('contact-loc');
  const foot  = document.querySelectorAll('.footer-name');
  const footl = document.querySelectorAll('.footer-loc');

  if (intro) intro.textContent = CONFIG.contactIntro;
  if (email) { email.textContent = CONFIG.email; email.href = 'mailto:' + CONFIG.email; }
  if (ig)    { ig.textContent = CONFIG.instagram; ig.href = CONFIG.instagramUrl; }
  if (loc)   loc.textContent = CONFIG.location;
  foot.forEach(el => el.textContent = '© ' + CONFIG.year + ' ' + CONFIG.name);
  footl.forEach(el => el.textContent = CONFIG.location);
}

// ── Render nav name ───────────────────────────────────────────
function renderNav() {
  document.querySelectorAll('.nav-name').forEach(el => el.textContent = CONFIG.name);
}

document.addEventListener('DOMContentLoaded', () => {
  renderNav();
  renderBio();
  renderSeries();
  renderContact();
});
