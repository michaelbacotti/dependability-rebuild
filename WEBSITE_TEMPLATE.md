# Dependability.us — Website Template & Style Documentation

_This document is the canonical reference for rebuilding dependability.us from scratch or adding new pages in the correct format. Everything you need to know is here._

---

## Table of Contents

1. [Site Structure](#1-site-structure)
2. [Page Template (Standard HTML Shell)](#2-page-template-standard-html-shell)
3. [CSS Reference](#3-css-reference)
4. [Nav Structure](#4-nav-structure)
5. [Footer Structure](#5-footer-structure)
6. [AdSense Block](#6-adsense-block)
7. [Article Page Structure](#7-article-page-structure)
8. [Non-Article Page Structure](#8-non-article-page-structure)
9. [Homepage Structure](#9-homepage-structure)
10. [Content Section Structure](#10-content-section-structure)
11. [Full CSS — style.css](#11-full-css--stylecss)

---

## Important Rules

- **Nav is static HTML embedded in each page** — NOT loaded via nav.js. nav.js is loaded at the end of `<body>` and injects content into `#site-utility` and `#site-nav` divs, but the divs themselves appear directly in each page's HTML.
- **Footer is static HTML embedded in each page** — NOT footer.js. The full `<div id="site-footer">...</div>` block appears in every page.
- **AdSense script tag** goes in `<head>`, the ins block goes between `</main>` and `<div id="site-footer">`.
- **Only article pages** have `.article-header-image` divs. Other pages should NOT have them.
- **nav.js and footer.js** are loaded at the end of `<body>`, but the page structure must contain the empty `#site-utility`, `#site-nav`, and `#site-footer` divs.

---

## 1. Site Structure

```
dependability-rebuild/
├── index.html                  # Homepage
├── about.html                  # About page
├── contact.html                # Contact page
├── disclaimer.html             # Investment disclaimer
├── education.html              # Education hub
├── forecast.html              # S&P 500 & VIX forecast
├── commentary.html             # Market commentary hub
├── strategies.html             # Options strategies hub
├── methodology.html            # Methodology page
├── privacy.html                # Privacy policy (legal)
├── terms.html                  # Terms of service (legal)
├── gold-as-a-store-of-value.html  # Article (education)
├── inflation-measurement-modern-economy.html  # Article
├── oil-paradox-energy-dominance.html         # Article
├── tlt-new-bond-regime.html                    # Article
├── articles/
│   ├── 2026-05-10-iv-crush-explained.html
│   ├── 2026-05-12-market-outlook.html
│   ├── 2026-05-13-research-themes.html
│   ├── 2026-05-13-trump-china-summit.html
│   ├── 2026-05-14-spacex-ipo-etf-exposure.html
│   ├── *.png                    # Article hero images
│   └── education-hero.png etc.  # Category hero images
├── style.css                   # Single stylesheet for entire site
├── nav.js                       # Injects utility bar + tab nav
├── footer.js                    # (present but not used for static footer)
├── favicon.svg
├── site.webmanifest
├── apple-touch-icon.png
├── android-chrome-192x192.png
├── android-chrome-512x512.png
├── ads.txt
├── sitemap.xml
├── _HOMEPAGE_TEMPLATE.md       # Homepage structure reference
├── _adsense.txt                 # AdSense HTML snippet
├── _template.html               # Blank page template
├── TONE.md                      # Voice and style guide
└── package.json
```

### File Naming Conventions

- **Top-level pages:** `index.html`, `about.html`, `contact.html`, `disclaimer.html`, `education.html`, `forecast.html`, `commentary.html`, `strategies.html`, `methodology.html`, `privacy.html`, `terms.html`
- **Article pages:** kebab-case, date-prefixed or descriptive phrase: `gold-as-a-store-of-value.html`, `inflation-measurement-modern-economy.html`, `oil-paradox-energy-dominance.html`, `articles/2026-05-14-spacex-ipo-etf-exposure.html`
- **Images:** matching the article name with `.png` extension, stored in `/articles/`

---

## 2. Page Template (Standard HTML Shell)

Copy this exact structure for any new page:

```html
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>PAGE TITLE | Dependability Holdings LLC</title>
 <meta name="description" content="PAGE DESCRIPTION — one clear sentence.">
 <link rel="stylesheet" href="/style.css">
 <link rel="icon" type="image/svg+xml" href="/favicon.svg">
 <link rel="canonical" href="https://dependability.us/PAGE-SLUG">
 <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9312870448453345" crossorigin="anonymous"></script>
</head>
<body>

 <div id="site-utility"></div>
 <div id="site-nav"></div>

 <main>
  <!-- PAGE CONTENT GOES HERE -->
 </main>

 <div style="margin:2rem 0;padding:.75rem;background:var(--surface);border-radius:var(--radius);text-align:center;">
 <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-9312870448453345" data-ad-slot="7590828986" data-ad-format="auto" data-full-width-responsive="true"></ins>
 </div>
 <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>

 <div id="site-footer">
  <div class="main-footer">
   <div class="footer-grid">
    <div class="footer-brand">
     <h4>Dependability Holdings LLC</h4>
     <p>Independent financial research and market analysis. Our work focuses on options market dynamics, volatility regimes, and macro-driven positioning.</p>
    </div>
    <div class="footer-nav">
     <h5>Research</h5>
     <ul>
      <li><a href="/forecast.html">S&amp;P 500 &amp; VIX Forecast</a></li>
      <li><a href="/commentary.html">Market Commentary</a></li>
      <li><a href="/education.html">Options Education</a></li>
      <li><a href="/strategies.html">Options Strategies</a></li>
     </ul>
    </div>
    <div class="footer-nav">
     <h5>Company</h5>
     <ul>
      <li><a href="/about.html">About</a></li>
      <li><a href="/methodology.html">Methodology</a></li>
      <li><a href="/contact.html">Contact</a></li>
     </ul>
    </div>
    <div class="footer-nav">
     <h5>Legal</h5>
     <ul>
      <li><a href="/privacy.html">Privacy Policy</a></li>
      <li><a href="/terms.html">Terms of Service</a></li>
      <li><a href="/disclaimer.html">Investment Disclaimer</a></li>
     </ul>
    </div>
   </div>
   <div class="footer-bottom">
    <p>&copy; 2026 Dependability Holdings LLC. All rights reserved.</p>
    <p>For informational purposes only. Not investment advice. See our <a href="/methodology.html">full disclosures</a>.</p>
   </div>
  </div>
 </div>

 <script src="/nav.js"></script>

</body>
</html>
```

### Key elements in order:

1. `<!DOCTYPE html>` + `<html lang="en">`
2. `<head>` with: charset, viewport, title, meta description, style.css link, favicon, canonical link, AdSense script
3. `<body>` with: `#site-utility`, `#site-nav` divs (empty, nav.js fills them)
4. `<main>` — page-specific content
5. AdSense block (between `</main>` and `<div id="site-footer">`)
6. Static footer HTML (NOT footer.js)
7. `<script src="/nav.js"></script>` — loaded AFTER footer

---

## 3. CSS Reference

### CSS Variables (`:root`)

```css
:root {
 --color-bg: #ffffff;
 --color-text: #1a1a1a;
 --color-accent: #c8001e;
 --color-utility-bg: #111111;
 --color-utility-text: #ffffff;
 --color-category: #666666;
 --color-date: #888888;
 --color-border: #e0e0e0;
 --font-heading: Georgia, serif;
 --font-body: system-ui, -apple-system, Inter, sans-serif;
 --max-width: 1200px;
 --nav-height: 48px;
 --utility-height: 40px;
}
```

### Key Classes

| Class | Purpose |
|---|---|
| `.container` | Centered max-width wrapper, `padding: 0 24px` |
| `.page-content` | Standard content area, `padding: 48px 24px`, max-width 1200px |
| `.article-page` | Article layout, `max-width: 800px`, `padding: 48px 24px` |
| `.article-header` | Article header block with category, title, meta |
| `.article-header-image` | Hero image container — `width: min(100%, 720px)`, `aspect-ratio: 2/1` |
| `.article-body` | Main article content, `font-size: 1.0625rem`, `line-height: 1.8` |
| `.hero` | (also `.hero-section`) — full-width homepage hero block |
| `.page-hero` | Non-article page hero — centered text, `padding: 48px 24px` |
| `.section-header` | Section title row — `h2` left + `explore-link` right |
| `.card-grid` | 3-column grid for article cards, `gap: 24px` |
| `.article-card` | Card in card-grid, top border accent |
| `.article-card.education-card` | Card with neutral top border (not accent) |
| `.sidebar-article` | Sidebar list item — `category-label` + `date-text` + `h4` link |
| `.feature-grid` | 2-column grid for feature cards on forecast page |
| `.feature-card` | Card with top accent border and padding |
| `.main-footer` | Footer container, `max-width: 1200px`, `padding: 40px 24px` |
| `.footer-grid` | 4-column grid (brand + 3 nav cols) |
| `.footer-brand` | Brand column — `h4` in accent color, description paragraph |
| `.footer-nav` | Nav column — `h5` uppercase label + `<ul>` |
| `.footer-bottom` | Bottom bar — copyright and disclaimer, centered |
| `.ad-slot` | AdSense wrapper (inline style in practice) |
| `.share-bar` | Social sharing row — label + share buttons |
| `.category-label` | Small uppercase label, `letter-spacing: 0.1em`, color: `--color-category` |
| `.date-text` | Date stamp, `font-size: 0.8125rem`, color: `--color-date` |
| `.accent-link` | Link with `--color-accent` color |
| `.legal-body` | Legal page content — `max-width: 720px`, `font-size: 1rem`, `line-height: 1.8` |
| `.page-header` | Legal page header — `h1` + `page-date`, border-bottom |
| `.contact-body` | Contact page content wrapper |
| `.contact-form` | Flex column form layout |
| `.form-group` | Label + input/textarea stacked |
| `.btn-primary` | Red background button |
| `.info-box` | Dark background callout box |
| `.disclaimer` | Article disclaimer block at bottom |
| `.resource-cards` | 2-column layout for resource callout boxes inside articles |
| `.resource-card` | Individual resource card inside article |
| `.edu-section` | Education section wrapper |
| `.edu-grid` | 2-column education card grid |
| `.edu-card` | Individual education card |
| `.methodology-content` | Methodology page content, `max-width: 800px` |
| `.page-hero` | Hero for hub pages (forecast, commentary, education) |

### Max-widths

- Site max-width: `1200px` (via `--max-width` variable and `.container`)
- Article content: `800px`
- Legal content: `720px`
- Contact form: `500px`
- Article hero image: `min(100%, 720px)`, aspect-ratio `2 / 1`

### Padding/Margin Patterns

- Section padding: `48px 24px` (hero), `48px 24px` (page-content)
- Card grid padding: `0 24px 48px`
- Section header padding: `32px 24px 16px`
- Article body paragraph spacing: `margin-bottom: 1.25rem`
- Footer inner padding: `40px 24px`

---

## 4. Nav Structure

**nav.js** injects into two divs that exist (empty) in every page's HTML:

```html
<div id="site-utility"></div>  <!-- nav.js fills this -->
<div id="site-nav"></div>       <!-- nav.js fills this -->
```

nav.js produces:

**Row 1 — Top Black Bar:**
```html
<nav class="top-bar">
  <a href="/" class="top-wordmark">DEPENDABILITY</a>
  <span class="top-tagline">Independent market research and options analysis</span>
  <div class="top-links">
    <a href="/about.html">About</a>
    <a href="/methodology.html">Methodology</a>
    <a href="/about.html#contact">Contact</a>
  </div>
</nav>
```

**Row 2 — Section Tab Bar:**
```html
<div class="tab-bar">
  <div class="tab-bar-inner">
    <a href="/index.html">Overview</a>
    <a href="/forecast.html">Forecast</a>
    <a href="/commentary.html">Market Commentary</a>
    <a href="/education.html">Education</a>
    <a href="/strategies.html">Options Strategies</a>
  </div>
</div>
```

nav.js also adds `.active` class to the tab matching the current pathname.

---

## 5. Footer Structure

The footer is **static HTML** in every page — NOT loaded via JS. Copy this exactly:

```html
<div id="site-footer">
  <div class="main-footer">
   <div class="footer-grid">
    <div class="footer-brand">
     <h4>Dependability Holdings LLC</h4>
     <p>Independent financial research and market analysis. Our work focuses on options market dynamics, volatility regimes, and macro-driven positioning.</p>
    </div>
    <div class="footer-nav">
     <h5>Research</h5>
     <ul>
      <li><a href="/forecast.html">S&amp;P 500 &amp; VIX Forecast</a></li>
      <li><a href="/commentary.html">Market Commentary</a></li>
      <li><a href="/education.html">Options Education</a></li>
      <li><a href="/strategies.html">Options Strategies</a></li>
     </ul>
    </div>
    <div class="footer-nav">
     <h5>Company</h5>
     <ul>
      <li><a href="/about.html">About</a></li>
      <li><a href="/methodology.html">Methodology</a></li>
      <li><a href="/contact.html">Contact</a></li>
     </ul>
    </div>
    <div class="footer-nav">
     <h5>Legal</h5>
     <ul>
      <li><a href="/privacy.html">Privacy Policy</a></li>
      <li><a href="/terms.html">Terms of Service</a></li>
      <li><a href="/disclaimer.html">Investment Disclaimer</a></li>
     </ul>
    </div>
   </div>
   <div class="footer-bottom">
    <p>&copy; 2026 Dependability Holdings LLC. All rights reserved.</p>
    <p>For informational purposes only. Not investment advice. See our <a href="/methodology.html">full disclosures</a>.</p>
   </div>
  </div>
</div>
```

---

## 6. AdSense Block

The AdSense block appears **between `</main>` and `<div id="site-footer">`** on every page.

```html
<div style="margin:2rem 0;padding:.75rem;background:var(--surface);border-radius:var(--radius);text-align:center;">
 <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-9312870448453345" data-ad-slot="7590828986" data-ad-format="auto" data-full-width-responsive="true"></ins>
 </div>
 <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
```

The AdSense **script tag** (`<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9312870448453345" crossorigin="anonymous"></script>`) goes in `<head>`.

---

## 7. Article Page Structure

Use `gold-as-a-store-of-value.html` as the template. Articles have:
- `.article-page` wrapper (max-width: 800px)
- `.article-header` with category-label, h1, article-meta
- `.article-header-image` div with `<img>` — **only articles have this**
- `.article-body` with the actual content

### Article Page Shell:

```html
<main>
  <div class="article-page">

   <div class="article-header">
    <div class="category-label">EDUCATION / MACRO</div>
    <h1>Article Title Here</h1>
    <div class="article-meta">May 15, 2026 &nbsp;|&nbsp; Dependability Research Desk</div>
   </div>

   <div class="article-header-image">
    <img src="/articles/ARTICLE-SLUG.png" alt="Alt text" style="width:100%;display:block;">
   </div>

   <div class="article-body">

    <!-- Article content: paragraphs, h2, h3, lists, etc. -->

    <div class="disclaimer">
     <strong>Disclaimer:</strong> This research is for informational purposes only...
    </div>

    <div class="share-bar">
     <span class="share-label">Share</span>
     <a class="share-btn share-x" href="#" target="_blank" rel="noopener" aria-label="Share on X">
      <svg ...><!-- X/Twitter icon --></svg>
     </a>
     <a class="share-btn share-facebook" href="#" target="_blank" rel="noopener" aria-label="Share on Facebook">
      <svg ...><!-- Facebook icon --></svg>
     </a>
     <a class="share-btn share-linkedin" href="#" target="_blank" rel="noopener" aria-label="Share on LinkedIn">
      <svg ...><!-- LinkedIn icon --></svg>
     </a>
     <button class="share-btn share-copy" aria-label="Copy link" onclick="navigator.clipboard.writeText(window.location.href).then(()=>{this.querySelector('.copy-label').textContent='Copied!';setTimeout(()=>{this.querySelector('.copy-label').textContent='Copy'},2000)})">
      <svg ...><!-- Copy icon --></svg>
      <span class="copy-label">Copy</span>
     </button>
    </div>
    <script>
    document.querySelectorAll(".share-x, .share-facebook, .share-linkedin").forEach(function(el) {
     var url = encodeURIComponent(window.location.href);
     var title = encodeURIComponent(document.title);
     if (el.classList.contains("share-x")) el.href = "https://x.com/intent/tweet?url=" + url + "&text=" + title;
     if (el.classList.contains("share-facebook")) el.href = "https://www.facebook.com/sharer/sharer.php?u=" + url;
     if (el.classList.contains("share-linkedin")) el.href = "https://www.linkedin.com/sharing/share-offsite/?url=" + url;
    });
    </script>

   </div>
  </div>
</main>
```

### Inside `.article-body`:

- `<p>` — `font-size: 1.0625rem`, `line-height: 1.8`, `margin-bottom: 1.25rem`
- `<h2>` — `font-size: 1.5rem`, `margin-top: 2rem`, `margin-bottom: 1rem`
- `<h3>` — `font-size: 1.25rem`, `margin-top: 1.5rem`, `margin-bottom: 0.75rem`
- `<ul>` / `<ol>` — `margin-bottom: 1.25rem`, `padding-left: 1.5rem`
- `<li>` — `margin-bottom: 0.5rem`
- `<strong>` — `font-weight: 600`
- `.disclaimer` — `margin-top: 3rem`, `padding-top: 1.5rem`, `border-top: 1px solid var(--color-border)`, `font-size: 0.8125rem`, `color: #888888`
- `.info-box` — dark background callout: `background:var(--color-utility-bg)`, `border:1px solid var(--color-accent)`, `padding:20px`
- `.resource-cards` — 2-column grid: `display:grid;grid-template-columns:repeat(2,1fr);gap:20px`
- `.share-bar` — social share row at bottom of article

---

## 8. Non-Article Page Structure

Use `privacy.html`, `terms.html`, or `contact.html` as templates. These pages use:

### Legal Page (privacy.html, terms.html, disclaimer.html):

```html
<main class="page-content">
  <div class="container">
   <header class="page-header">
    <p class="category-label">Legal</p>
    <h1>Page Title</h1>
    <p class="page-date">Effective: May 13, 2026</p>
   </header>
   <div class="legal-body">
    <!-- h2 sections, paragraphs, lists -->
   </div>
  </div>
</main>
```

**Key:** These pages do NOT have `.article-header-image` divs.

### Hub/Content Page (forecast.html, commentary.html, education.html, strategies.html):

```html
<main>
  <div class="page-hero">
    <h1>Page Title</h1>
    <p>Page description paragraph.</p>
  </div>
  <div class="page-content">
    <!-- page-specific content -->
  </div>
</main>
```

### About Page:

```html
<main>
  <div class="page-hero">
    <h1>About Dependability Holdings LLC</h1>
    <p>Tagline.</p>
  </div>
  <div class="page-content">
    <div class="article-page" style="max-width:800px;margin:0 auto;padding:48px 24px;">
      <!-- h2 sections with inline styles for headings -->
    </div>
  </div>
</main>
```

### Contact Page:

```html
<main class="page-content">
  <div class="container">
   <header class="page-header">
    <p class="category-label">Get in Touch</p>
    <h1>Contact</h1>
   </header>
   <div class="contact-body">
    <!-- paragraphs, h2 sections, ul lists -->
    <div class="contact-form-section">
     <h2>Send a Message</h2>
     <form class="contact-form" action="#" method="post">
      <div class="form-group">
       <label for="name">Name</label>
       <input type="text" id="name" name="name" placeholder="Your full name" required>
      </div>
      <div class="form-group">
       <label for="email">Email Address</label>
       <input type="email" id="email" name="email" placeholder="you@example.com" required>
      </div>
      <div class="form-group">
       <label for="subject">Subject</label>
       <input type="text" id="subject" name="subject" placeholder="What is this regarding?">
      </div>
      <div class="form-group">
       <label for="message">Message</label>
       <textarea id="message" name="message" rows="6" placeholder="Your message..." required></textarea>
      </div>
      <button type="submit" class="btn-primary">Send Message</button>
     </form>
    </div>
    <p class="contact-note">We aim to respond to all inquiries within 2–3 business days.</p>
   </div>
  </div>
</main>
```

---

## 9. Homepage Structure

Reference: `_HOMEPAGE_TEMPLATE.md` in the project root.

The homepage (`index.html`) is built from these sections in order:

### Hero Section

```html
<section class="hero-section">
  <div class="hero-grid">

   <!-- LEFT: Featured Article (2/3 width) -->
   <div class="hero-featured">
    <div class="category-label">MARKET COMMENTARY</div>
    <div class="date-text">May 17, 2026</div>
    <h2><a href="/oil-paradox-energy-dominance">Article Title</a></h2>
    <div class="article-header-image">
     <img src="/articles/SLUG.png" alt="Alt text" style="width:100%;display:block;">
    </div>
    <p>Excerpt text...</p>
    <a href="/SLUG" class="accent-link" style="font-weight:600;">Read More &#8594;</a>
   </div>

   <!-- RIGHT: Latest Sidebar (1/3 width) -->
   <div class="hero-sidebar">
    <h3>LATEST</h3>
    <div class="sidebar-article">
     <div class="category-label">CATEGORY</div>
     <div class="date-text">Date</div>
     <h4><a href="/URL">Article Title</a></h4>
    </div>
    <!-- repeat 5 times -->
   </div>

  </div>
</section>
```

### Section Blocks (Market Commentary, Education, etc.)

Each section:
```html
<section>
  <div class="section-header">
    <h2>SECTION NAME</h2>
    <a href="/SECTION" class="explore-link">Explore &#8594;</a>
  </div>
  <div class="card-grid">
    <div class="article-card">...</div>
    <div class="article-card">...</div>
    <div class="article-card">...</div>
  </div>
</section>
```

**⚠️ EXACTLY 3 cards per section** — never 2 or 4. A 3-column grid with fewer cards leaves blank space; with 4 cards it wraps to 2+2 which looks uneven. Always show exactly 3.

Education cards use `.article-card education-card` (neutral top border). Market Commentary uses standard `.article-card` (accent top border).

---

## 10. Content Section Structure

### Category Labels

- `MARKET COMMENTARY` — articles in the market commentary section
- `EDUCATION` or `EDUCATION / MACRO` — education articles
- `FORECAST` — forecast content
- `Legal` — legal pages
- `Get in Touch` — contact page

### Date Formatting

- Display: `May 17, 2026` (full month name, day, year)
- In article meta: `May 15, 2026 &nbsp;|&nbsp; Dependability Research Desk`

### Article Card Structure

```html
<div class="article-card [education-card]">
  <div class="category-label">CATEGORY</div>
  <div class="date-text">Date</div>
  <h3><a href="/URL">Article Title</a></h3>
  <p>Excerpt text...</p>
</div>
```

### Article Filename Pattern

- Use kebab-case: `gold-as-a-store-of-value.html`
- Images match: `/articles/gold-as-a-store-of-value.png`
- Hero images should be `aspect-ratio: 2/1` at display time

---

## 11. Full CSS — style.css

The complete stylesheet follows. This is the only CSS file for the entire site.

```css
/* ================================================
 Dependability Holdings LLC — Main Stylesheet
 Single file for entire site. All styles here.
 ================================================ */

/* 1. CSS Variables */
:root {
 --color-bg: #ffffff;
 --color-text: #1a1a1a;
 --color-accent: #c8001e;
 --color-utility-bg: #111111;
 --color-utility-text: #ffffff;
 --color-category: #666666;
 --color-date: #888888;
 --color-border: #e0e0e0;
 --font-heading: Georgia, serif;
 --font-body: system-ui, -apple-system, Inter, sans-serif;
 --max-width: 1200px;
 --nav-height: 48px;
 --utility-height: 40px;
}

/* 2. Reset & Base */
*, *::before, *::after {
 box-sizing: border-box;
 margin: 0;
 padding: 0;
}

html {
 font-size: 16px;
 -webkit-text-size-adjust: 100%;
}

body {
 font-family: var(--font-body);
 color: var(--color-text);
 background-color: var(--color-bg);
 line-height: 1.6;
 min-height: 100vh;
 display: flex;
 flex-direction: column;
}

main {
 flex: 1;
}

a {
 color: var(--color-accent);
 text-decoration: none;
}

a:hover {
 text-decoration: underline;
}

img {
 max-width: 100%;
 height: auto;
}

/* 3. Typography */
h1, h2, h3, h4, h5, h6 {
 font-family: var(--font-heading);
 color: var(--color-text);
 line-height: 1.25;
}

h1 { font-size: 2.5rem; }
h2 { font-size: 2rem; }
h3 { font-size: 1.5rem; }
h4 { font-size: 1.25rem; }

p {
 margin-bottom: 1rem;
}

small, .small {
 font-size: 0.875rem;
}

.category-label {
 font-size: 0.75rem;
 text-transform: uppercase;
 letter-spacing: 0.1em;
 color: var(--color-category);
 font-weight: 600;
}

.date-text {
 font-size: 0.8125rem;
 color: var(--color-date);
}

.accent-link {
 color: var(--color-accent);
 font-weight: 500;
}

/* Row 1: Top Black Bar */
.top-bar {
 background-color: #111111;
 height: var(--utility-height);
 line-height: var(--utility-height);
 display: flex;
 align-items: center;
 justify-content: space-between;
 padding: 0 24px;
 position: relative;
}

.top-wordmark {
 font-size: 0.9375rem;
 font-weight: 700;
 letter-spacing: 0.05em;
 color: #ffffff;
 text-decoration: none;
 white-space: nowrap;
 flex-shrink: 0;
}

.top-tagline {
 position: absolute;
 left: 50%;
 transform: translateX(-50%);
 color: rgba(255,255,255,0.7);
 font-size: 11px;
 font-weight: 300;
 letter-spacing: 0.05em;
 white-space: nowrap;
}

.top-links {
 display: flex;
 gap: 20px;
 flex-shrink: 0;
}

.top-links a {
 font-size: 0.8125rem;
 color: #cccccc;
 text-decoration: none;
}

.top-links a:hover { color: #ffffff; }

@media (max-width: 768px) {
 .top-tagline { display: none; }
}

/* Row 2: Section Tab Bar */
.tab-bar {
 max-width: var(--max-width);
 margin: 0 auto;
 padding: 0 24px;
 display: flex;
 align-items: center;
 justify-content: space-between;
 gap: 0;
}

.nav-left {
 display: flex;
 align-items: center;
 gap: 0;
 flex-shrink: 0;
}

.nav-logo {
 font-size: 0.875rem;
 font-weight: 700;
 letter-spacing: 0.08em;
 color: var(--color-text);
 text-decoration: none;
 padding: 14px 0;
 white-space: nowrap;
}

.nav-logo:hover {
 color: var(--color-accent);
}

.nav-descriptor {
 color: rgba(255,255,255,0.8);
 font-size: 11px;
 font-weight: 300;
 letter-spacing: 0.05em;
 margin: 0 2rem 0 1.5rem;
 white-space: nowrap;
 color: #888888;
}

.nav-right {
 display: flex;
 gap: 0;
 overflow-x: auto;
 -webkit-overflow-scrolling: touch;
}

.tab-bar-inner {
 display: flex;
 flex-direction: row;
 align-items: center;
 gap: 0;
}

.tab-bar-inner a {
 display: inline-block;
 padding: 14px 20px;
 font-size: 0.875rem;
 font-weight: 500;
 color: var(--color-text);
 text-decoration: none;
 border-bottom: 3px solid transparent;
 transition: color 0.2s, border-color 0.2s;
 white-space: nowrap;
}

.tab-bar-inner a:hover {
 color: var(--color-accent);
}

.tab-bar-inner a.active {
 color: var(--color-accent);
 border-bottom-color: var(--color-accent);
}

@media (max-width: 768px) {
 .nav-descriptor { display: none; }
}

/* 6. Container */
.container {
 max-width: var(--max-width);
 margin: 0 auto;
 padding: 0 24px;
}

/* 7. Homepage — Hero Section */
.hero-section {
 border-bottom: 1px solid var(--color-border);
}

.hero-grid {
 display: grid;
 grid-template-columns: 2fr 1fr;
 gap: 0;
 max-width: var(--max-width);
 margin: 0 auto;
}

.hero-featured {
 padding: 48px 48px 48px 24px;
 border-right: 1px solid var(--color-border);
}

.hero-featured .category-label {
 margin-bottom: 8px;
}

.hero-featured .date-text {
 margin-bottom: 12px;
}

.hero-featured h2 {
 font-size: 2rem;
 margin-bottom: 16px;
}

.hero-featured p {
 color: #333333;
 margin-bottom: 20px;
 line-height: 1.7;
}

.hero-sidebar {
 padding: 48px 24px 48px 48px;
}

.hero-sidebar h3 {
 font-size: 0.75rem;
 text-transform: uppercase;
 letter-spacing: 0.1em;
 color: var(--color-category);
 font-weight: 600;
 margin-bottom: 20px;
}

.sidebar-article {
 padding: 16px 0;
 border-bottom: 1px solid var(--color-border);
}

.sidebar-article:last-child {
 border-bottom: none;
}

.sidebar-article .category-label {
 margin-bottom: 4px;
}

.sidebar-article .date-text {
 margin-bottom: 4px;
}

.sidebar-article h4 {
 font-size: 1rem;
 font-family: var(--font-body);
}

.sidebar-article h4 a {
 color: var(--color-text);
 text-decoration: none;
}

.sidebar-article h4 a:hover {
 color: var(--color-accent);
}

/* 8. Section Headers */
.section-header {
 display: flex;
 justify-content: space-between;
 align-items: baseline;
 padding: 32px 24px 16px;
 max-width: var(--max-width);
 margin: 0 auto;
}

.section-header h2 {
 font-size: 0.75rem;
 text-transform: uppercase;
 letter-spacing: 0.1em;
 color: var(--color-category);
 font-weight: 600;
 font-family: var(--font-body);
}

.section-header .explore-link {
 font-size: 0.875rem;
 color: var(--color-accent);
 font-weight: 500;
}

/* 9. Card Grids */
.card-grid {
 display: grid;
 grid-template-columns: repeat(3, 1fr);
 gap: 24px;
 max-width: var(--max-width);
 margin: 0 auto;
 padding: 0 24px 48px;
}

.article-card {
 border-top: 3px solid var(--color-accent);
 padding-top: 20px;
 background: #ffffff;
}

.article-card.education-card {
 border-top-color: var(--color-border);
}

.article-card .category-label {
 margin-bottom: 8px;
}

.article-card .date-text {
 margin-bottom: 10px;
}

.article-card h3 {
 font-size: 1.125rem;
 margin-bottom: 12px;
}

.article-card h3 a {
 color: var(--color-text);
 text-decoration: none;
}

.article-card h3 a:hover {
 color: var(--color-accent);
}

.article-card p {
 font-size: 0.9375rem;
 color: #555555;
 line-height: 1.6;
}

/* 10. Footer */
#site-footer {
 background-color: #ffffff;
 border-top: 1px solid var(--color-border);
 margin-top: auto;
}

.main-footer {
 max-width: var(--max-width);
 margin: 0 auto;
 padding: 40px 24px;
}

.footer-grid {
 display: grid;
 grid-template-columns: 1.5fr 1fr 1fr;
 gap: 40px;
}

.footer-brand h4 {
 font-family: var(--font-heading);
 font-size: 1.25rem;
 color: var(--color-accent);
 margin-bottom: 12px;
}

.footer-brand p {
 font-size: 0.875rem;
 color: #666666;
 line-height: 1.6;
 text-align: left;
}

.footer-nav h5 {
 font-size: 0.75rem;
 text-transform: uppercase;
 letter-spacing: 0.1em;
 color: var(--color-category);
 font-weight: 600;
 margin-bottom: 16px;
 font-family: var(--font-body);
}

.footer-nav ul {
 list-style: none;
}

.footer-nav li {
 margin-bottom: 8px;
}

.footer-nav a {
 font-size: 0.875rem;
 color: #666666;
 text-decoration: none;
}

.footer-nav a:hover {
 color: var(--color-accent);
}

.footer-legal {
 font-size: 0.75rem;
 color: #999999;
 line-height: 1.5;
}

.footer-legal p {
 margin-bottom: 8px;
}

.footer-bottom {
 max-width: var(--max-width);
 margin: 0 auto;
 padding: 24px 24px 0;
 border-top: 1px solid var(--color-border);
 margin-top: 24px;
}

.footer-bottom p {
 font-size: 0.8125rem;
 color: #999999;
 text-align: center;
}

/* 11. Page Layouts (Forecast, Commentary, Education, About) */
.page-hero {
 border-bottom: 1px solid var(--color-border);
 padding: 48px 24px;
 text-align: left;
}

.page-hero h1 {
 font-size: 2.25rem;
 margin-bottom: 16px;
 text-align: center;
}

.page-hero p {
 font-size: 1.0625rem;
 color: #555555;
 max-width: 680px;
 margin: 0 auto;
}

.page-hero .hero-blurb {
 font-size: 1rem;
 color: #666666;
 margin-top: 20px;
 border-top: 1px solid var(--color-border);
 padding-top: 20px;
 margin-bottom: 0;
 text-align: left;
 max-width: 680px;
 margin-left: auto;
 margin-right: auto;
}

.page-content {
 padding: 48px 24px;
 max-width: var(--max-width);
 margin: 0 auto;
}

/* 12. Feature Cards (Forecast page) */
.feature-grid {
 display: grid;
 grid-template-columns: repeat(2, 1fr);
 gap: 24px;
 margin-top: 32px;
}

.feature-card {
 border: 1px solid var(--color-border);
 border-top: 3px solid var(--color-accent);
 padding: 28px;
}

.feature-card h3 {
 font-size: 1.125rem;
 margin-bottom: 12px;
}

.feature-card p {
 font-size: 0.9375rem;
 color: #555555;
 margin-bottom: 16px;
}

.feature-card .card-meta {
 font-size: 0.8125rem;
 color: var(--color-date);
 margin-bottom: 12px;
}

/* 13. Article Page */
.article-page {
 max-width: 800px;
 margin: 0 auto;
 padding: 48px 24px;
}

.article-page .article-header {
 margin-bottom: 32px;
 padding-bottom: 24px;
 border-bottom: 1px solid var(--color-border);
}

.article-page .category-label {
 margin-bottom: 12px;
}

.article-page h1 {
 font-size: 2rem;
 margin-bottom: 16px;
 line-height: 1.25;
}

.article-page .article-meta {
 font-size: 0.875rem;
 color: var(--color-date);
 margin-bottom: 24px;
}

.article-page .article-body {
 font-size: 1.0625rem;
 line-height: 1.8;
 color: #222222;
}

.article-page .article-body h2 {
 font-size: 1.5rem;
 margin-top: 2rem;
 margin-bottom: 1rem;
}

.article-page .article-body h3 {
 font-size: 1.25rem;
 margin-top: 1.5rem;
 margin-bottom: 0.75rem;
}

.article-page .article-body p {
 margin-bottom: 1.25rem;
}

.article-page .article-body ul,
.article-page .article-body ol {
 margin-bottom: 1.25rem;
 padding-left: 1.5rem;
}

.article-page .article-body li {
 margin-bottom: 0.5rem;
}

.article-page .article-body strong {
 font-weight: 600;
 color: var(--color-text);
}

.article-page .article-body .disclaimer {
 margin-top: 3rem;
 padding-top: 1.5rem;
 border-top: 1px solid var(--color-border);
 font-size: 0.8125rem;
 color: #888888;
 line-height: 1.5;
}

/* 14. Education Sections */
.edu-section {
 margin-bottom: 48px;
}

.edu-section h2 {
 font-size: 1.5rem;
 margin-bottom: 20px;
 padding-bottom: 12px;
 border-bottom: 1px solid var(--color-border);
}

.edu-grid {
 display: grid;
 grid-template-columns: repeat(2, 1fr);
 gap: 20px;
}

.edu-card {
 padding: 24px;
 border: 1px solid var(--color-border);
}

.edu-card h3 {
 font-size: 1.0625rem;
 margin-bottom: 10px;
}

.edu-card p {
 font-size: 0.9375rem;
 color: #555555;
}

/* 15. Methodology page */
.methodology-content {
 max-width: 800px;
 margin: 0 auto;
}

.methodology-content h2 {
 font-size: 1.5rem;
 margin-top: 2rem;
 margin-bottom: 1rem;
}

.methodology-content p {
 font-size: 1.0625rem;
 line-height: 1.8;
 margin-bottom: 1.25rem;
}

/* 16. Buttons / CTAs */
.btn {
 display: inline-block;
 padding: 10px 24px;
 background-color: var(--color-accent);
 color: #ffffff;
 font-size: 0.9375rem;
 font-weight: 500;
 text-decoration: none;
 border: none;
 cursor: pointer;
 transition: background-color 0.2s;
}

.btn:hover {
 background-color: #a00018;
 text-decoration: none;
 color: #ffffff;
}

/* 17. Utilities */
.text-center {
 text-align: center;
}

.mt-0 { margin-top: 0; }
.mb-0 { margin-bottom: 0; }

/* 18. Responsive */
@media (max-width: 900px) {
 .hero-grid {
  grid-template-columns: 1fr;
 }
 .hero-featured {
  border-right: none;
  border-bottom: 1px solid var(--color-border);
  padding: 32px 24px;
 }
 .hero-sidebar {
  padding: 32px 24px;
 }
 .card-grid {
  grid-template-columns: repeat(2, 1fr);
 }
 .footer-grid {
  grid-template-columns: 1fr 1fr;
 }
 .feature-grid {
  grid-template-columns: 1fr;
 }
 .edu-grid {
  grid-template-columns: 1fr;
 }
}

@media (max-width: 600px) {
 h1 { font-size: 1.875rem; }
 h2 { font-size: 1.5rem; }
 .hero-featured h2 { font-size: 1.5rem; }
 .card-grid {
  grid-template-columns: 1fr;
 }
 .footer-grid {
  grid-template-columns: 1fr;
 }
 .tab-bar-inner {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 0;
}

.tab-bar-inner a {
  padding: 12px 14px;
  font-size: 0.8125rem;
 }
 .section-header {
  padding: 24px 16px 12px;
 }
 .card-grid {
  padding: 0 16px 32px;
 }
 .container {
  padding: 0 16px;
 }
 .page-content {
  padding: 32px 16px;
 }
}

/* Financial header image */
.article-header-image {
 width: min(100%, 720px);
 aspect-ratio: 2 / 1;
 overflow: hidden;
 margin: 1.5rem 0;
 border: 1px solid #e0e0e0;
}
.article-header-image img {
 width: 100%;
 height: 100%;
 object-fit: cover;
 object-position: center;
 display: block;
}

/* Contact page */
.contact-body {
 max-width: 680px;
}

.contact-body p {
 font-size: 1rem;
 line-height: 1.7;
 margin-bottom: 1rem;
}

.contact-form-section {
 margin-top: 2.5rem;
}

.contact-form-section h2 {
 font-size: 1.5rem;
 margin-bottom: 1.5rem;
}

.contact-form {
 display: flex;
 flex-direction: column;
 gap: 1.25rem;
 max-width: 500px;
}

.form-group {
 display: flex;
 flex-direction: column;
 gap: 0.5rem;
}

.form-group label {
 font-size: 0.875rem;
 font-weight: 500;
 color: var(--color-text);
}

.form-group input,
.form-group textarea {
 padding: 10px 14px;
 border: 1px solid var(--color-border);
 font-size: 1rem;
 font-family: var(--font-body);
 color: var(--color-text);
 background: var(--color-bg);
 border-radius: 4px;
 transition: border-color 0.2s;
}

.form-group input:focus,
.form-group textarea:focus {
 outline: none;
 border-color: var(--color-accent);
}

.form-group textarea {
 resize: vertical;
 min-height: 120px;
}

.btn-primary {
 display: inline-block;
 background: var(--color-accent);
 color: #ffffff;
 padding: 12px 28px;
 font-size: 0.9375rem;
 font-weight: 600;
 border: none;
 cursor: pointer;
 align-self: flex-start;
 transition: background 0.2s;
}

.btn-primary:hover {
 background: #a0001a;
}

.contact-note {
 margin-top: 2rem;
 font-size: 0.875rem;
 color: var(--color-date);
}

/* Legal pages */
.page-header {
 margin-bottom: 2.5rem;
 padding-bottom: 1.5rem;
 border-bottom: 1px solid var(--color-border);
}

.page-header h1 {
 font-size: 2.25rem;
 margin-bottom: 0.75rem;
}

.page-date {
 font-size: 0.875rem;
 color: var(--color-date);
}

.legal-body {
 max-width: 720px;
}

.legal-body p {
 font-size: 1rem;
 line-height: 1.8;
 margin-bottom: 1.25rem;
 color: #222222;
}

.legal-body h2 {
 font-size: 1.375rem;
 margin-top: 2.25rem;
 margin-bottom: 0.875rem;
 color: var(--color-text);
}

.legal-body h3 {
 font-size: 1.125rem;
 margin-top: 1.5rem;
 margin-bottom: 0.625rem;
}

.legal-body ul {
 margin-bottom: 1.25rem;
 padding-left: 1.5rem;
}

.legal-body li {
 font-size: 1rem;
 line-height: 1.7;
 margin-bottom: 0.5rem;
 color: #222222;
}

.disclaimer-lead {
 font-size: 1.0625rem !important;
 color: var(--color-text) !important;
 border-left: 4px solid var(--color-accent);
 padding-left: 1rem;
 margin-bottom: 2rem !important;
}

/* Tools note */
.tools-note {
 margin-top: 2rem;
 padding: 1rem 1.25rem;
 background: #f8f8f8;
 border: 1px solid var(--color-border);
 border-left: 3px solid var(--color-accent);
 font-size: 0.9375rem;
 color: #444444;
 line-height: 1.6;
}

.tools-note a {
 color: var(--color-accent);
 font-weight: 500;
}

/* Share bar */
.share-bar { display: flex; align-items: center; gap: 10px; margin: 40px 0 32px; padding: 16px 0; border-top: 1px solid #e8e4dd; border-bottom: 1px solid #e8e4dd; }
.share-label { font-size: 11px; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: #999; margin-right: 4px; }
.share-btn { display: inline-flex; align-items: center; gap: 5px; padding: 7px 12px; border-radius: 4px; font-size: 12px; text-decoration: none; border: 1px solid #cc0000; background: transparent; cursor: pointer; font-family: inherit; color: #cc0000; transition: opacity 0.15s; }
.share-btn:hover { opacity: 0.7; }
```

---

_This document was generated from the dependability.us codebase. Last updated: 2026-05-18. For voice and tone guidance, see `TONE.md` in the project root._