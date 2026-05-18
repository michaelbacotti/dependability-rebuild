# Dependability.us Homepage Template

Exact structure of dependability.us homepage as of 2026-05-18.

## Structure

```
<body>
  <div id="site-utility"></div>        ← nav.js injects utility bar
  <div id="site-nav"></div>           ← nav.js injects main nav

  <main>

    <!-- HERO SECTION -->
    <section class="hero-section">
      <div class="hero-grid">

        <!-- LEFT: Featured Article (2/3 width) -->
        <div class="hero-featured">
          <div class="category-label">MARKET COMMENTARY</div>
          <div class="date-text">May 17, 2026</div>
          <h2><a href="/oil-paradox-energy-dominance">The Oil Paradox: ...</a></h2>
          <div class="article-header-image">
            <img src="/articles/oil-paradox-energy-dominance.png" alt="..." style="width:100%;display:block;">
          </div>
          <p>Description text...</p>
          <a href="/oil-paradox-energy-dominance" class="accent-link" style="font-weight:600;">Read More &#8594;</a>
        </div>

        <!-- RIGHT: Latest Sidebar (1/3 width) -->
        <div class="hero-sidebar">
          <h3>LATEST</h3>
          <div class="sidebar-article">
            <div class="category-label">MARKET COMMENTARY</div>
            <div class="date-text">May 17, 2026</div>
            <h4><a href="/inflation-measurement-modern-economy">Inflation in a Modern Economy...</a></h4>
          </div>
          ...5 sidebar articles total...
        </div>

      </div>
    </section>

    <!-- MARKET COMMENTARY SECTION -->
    <section>
      <div class="section-header">
        <h2>MARKET COMMENTARY</h2>
        <a href="/commentary" class="explore-link">Explore &#8594;</a>
      </div>
      <div class="card-grid">
        <div class="article-card">...</div>
        <div class="article-card">...</div>
        <div class="article-card">...</div>
      </div>
    </section>

    <!-- EDUCATION SECTION -->
    <section>
      <div class="section-header">
        <h2>EDUCATION</h2>
        <a href="/education" class="explore-link">Explore &#8594;</a>
      </div>
      <div class="card-grid">
        <div class="article-card education-card">...</div>
        <div class="article-card education-card">...</div>
        <div class="article-card education-card">...</div>
      </div>
    </section>

  </main>

  <!-- AdSense -->
  <div style="margin:2rem 0;padding:.75rem;background:var(--surface);border-radius:var(--radius);text-align:center;">
    <ins class="adsbygoogle" ...></ins>
  </div>
  <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>

  <!-- STATIC FOOTER (no JS dependency) -->
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
```

## Key CSS Classes

- `.hero-section` — full-width hero block
- `.hero-grid` — 2-column grid (featured 2/3 + sidebar 1/3), gap: 32px
- `.hero-featured` — left hero column with category-label, date-text, h2, image, excerpt, accent-link
- `.hero-sidebar` — right column, h3 "LATEST", 5× sidebar-article blocks
- `.sidebar-article` — category-label + date-text + h4 link
- `.section-header` — h2 + explore-link (right-aligned)
- `.card-grid` — 3-column grid of article cards
- `.article-card` — category-label + date-text + h3 + excerpt paragraph
- `.education-card` — same as article-card but darker/education styling
- `.main-footer` — footer container, max-width 1200px, padding 40px 24px
- `.footer-grid` — 4-column grid (brand + 3 nav columns)
- `.footer-brand h4` — accent color (--color-accent), 1.25rem serif
- `.footer-nav h5` — uppercase, 0.75rem, letter-spacing 0.1em
- `.footer-bottom` — border-top, padding-top 24px, copyright + disclaimer

## Critical Rules

1. **Static footer only** — no footer.js, no JS dependency for footer rendering
2. **4-column footer grid** — brand + Research + Company + Legal
3. **Hero is 2/3 + 1/3 grid** — NOT equal columns
4. **Hero-featured has image** — `.article-header-image` with `width:100%;display:block`
5. **Card grids are 3-across** — 3 equal columns
6. **No duplicate disclaimers** — static footer already contains disclaimer
7. **AdSense between main and footer** — always
8. **nav.js loaded AFTER footer** — `<script src="/nav.js"></script>` at end of body

## nav.js Structure

nav.js injects:
- `#site-utility` — top utility bar (links like "About", "Contact" or empty)
- `#site-nav` — main navigation bar

nav.js does NOT touch the footer.

## CSS Variables (style.css)

```
--max-width: 1200px
--font-heading: Georgia, serif
--font-body: system-ui, -apple-system, sans-serif
--color-accent: #7c8e6e (green-gray)
--color-text: #333
--color-text-muted: #666
--color-border: #e0e0e0
--color-surface: #fff
```

## How to Recreate from Scratch

1. Create `index.html` with exact structure above
2. Update hero-featured article to most recent article
3. Update sidebar articles to 5 most recent
4. Update Market Commentary card-grid to 3 most recent articles in that section
5. Update Education card-grid to 3 most recent education articles
6. Insert AdSense block between `</main>` and `<div id="site-footer">`
7. Copy static footer HTML (NOT footer.js)
8. Load nav.js at end of body

## Current Hero Article (2026-05-18)
- Title: "The Oil Paradox: How America Became Both Master and Prisoner of Its Own Energy Dominance"
- Image: `/articles/oil-paradox-energy-dominance.png`
- Category: MARKET COMMENTARY
- Date: May 17, 2026