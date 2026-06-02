# SITE MEMORY — Dependability Holdings LLC

## Identity
- Entity: Dependability Holdings LLC
- Purpose: Financial research website — market commentary, options education, S&P 500 / VIX forecasting
- Repo: github.com/michaelbacotti/dependability-rebuild
- Live URL: dependability.us (Cloudflare Pages)
- Staging URL: dependability-rebuild.pages.dev
- Architecture: Flat HTML — see skills/website-flat-html.md

## Color Palette (Approved 2026-05-13)
- Background: #ffffff (white)
- Primary text: #1a1a1a
- Brand accent / headings / links: #c8001e (deep red)
- Header bar / nav: #111111 (near-black) with white text
- Category label: #666666 (small-caps gray)
- Dividers / borders: #e0e0e0
- Date / metadata: #888888
- CTA buttons: #c8001e bg + white text

## Typography
- Headings: Georgia, serif
- Body: system-ui, -apple-system, Inter, sans-serif
- Links and accent text: #c8001e

## File Roles
- `/style.css` — ALL styles. Never edit during routine content updates.
- `/nav.js` — Top utility bar + category tab bar. Edit here to change nav on all pages.
- `/footer.js` — Site-wide footer. Edit here to change footer on all pages.
- `/_template.html` — Base for new pages. Copy it, never edit or serve it.
- `/articles/` — Dated article files, one per post.

## Critical Rules
- All paths to style.css, nav.js, footer.js must start with `/`
- No build step. No Hugo. No GitHub Actions.
- Scripts go at end of body, after the div containers they populate
- Always verify live in browser after every deploy — not just curl

## Correct Article Template (CANONICAL)
Use `articles/_ARTICLE_TEMPLATE.html` as the reference for all new articles. It contains:
- Share bar with X/Facebook/LinkedIn/Copy buttons + JavaScript for dynamic URL injection
- Disclaimer block
- Full footer (main-footer with footer-grid, footer-nav, footer-bottom)
- Correct AdSense placement: ins unit + push script AFTER the article closes, BEFORE nav.js
- nav.js loaded BEFORE the site-footer div (not after)

## Footer Disclosure (STANDARD — identical on every article page)
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
     <li><a href="/forecast">S&amp;P 500 &amp; VIX Forecast</a></li>
     <li><a href="/commentary">Market Commentary</a></li>
     <li><a href="/education">Market Education</a></li>   <!-- label changed from Options Education -->
     <li><a href="/strategies">Options Strategies</a></li>
    </ul>
   </div>
   <div class="footer-nav">
    <h5>Company</h5>
    <ul>
     <li><a href="/about">About</a></li>
     <li><a href="/methodology">Methodology</a></li>
     <li><a href="/contact">Contact</a></li>
    </ul>
   </div>
   <div class="footer-nav">
    <h5>Legal</h5>
    <ul>
     <li><a href="/privacy">Privacy Policy</a></li>
     <li><a href="/terms">Terms of Service</a></li>
     <li><a href="/disclaimer">Investment Disclaimer</a></li>
    </ul>
   </div>
  </div>
  <div class="footer-bottom">
   <p>&copy; 2026 Dependability Holdings LLC. All rights reserved.</p>
   <p>For informational purposes only. Not investment advice. See our <a href="/methodology">full disclosures</a>.</p>
  </div>
 </div>
</div>
```

## Share Buttons (STANDARD — identical on every article page)
```html
<div class="share-bar">
 <span class="share-label">Share</span>
 <a class="share-btn share-x" href="#" target="_blank" rel="noopener" aria-label="Share on X">...</a>
 <a class="share-btn share-facebook" href="#" target="_blank" rel="noopener" aria-label="Share on Facebook">...</a>
 <a class="share-btn share-linkedin" href="#" target="_blank" rel="noopener" aria-label="Share on LinkedIn">...</a>
 <button class="share-btn share-copy" ...>Copy</button>
</div>
<script>
document.querySelectorAll('.share-x, .share-facebook, .share-linkedin').forEach(function(el) {
 var url = encodeURIComponent(window.location.href);
 var title = encodeURIComponent(document.title);
 if (el.classList.contains('share-x')) el.href = 'https://x.com/intent/tweet?url=' + url + '&text=' + title;
 if (el.classList.contains('share-facebook')) el.href = 'https://www.facebook.com/sharer/sharer.php?u=' + url;
 if (el.classList.contains('share-linkedin')) el.href = 'https://www.linkedin.com/sharing/share-offsite/?url=' + url;
});
</script>
```

## Disclaimer Block (STANDARD — identical on every article page)
```html
<div class="disclaimer">
 <strong>Disclaimer:</strong> This research is for informational purposes only and does not constitute investment advice. Options trading involves substantial risk of loss. Dependability Holdings LLC has no positions in the securities mentioned. Past performance is not indicative of future results.
</div>
```

## Article Page HTML Structure (correct order)
1. `<head>` — meta, title, canonical, OG tags, CSS (including .share-bar styles), AdSense script
2. `<body>` → `#site-utility` → `#site-nav` → `<main>`
3. Inside `<main>`: `.article-page` → `.article-header` → `.article-header-image` → `.article-body`
4. End of `.article-body`: disclaimer → share-bar → inline JS
5. `</main>`
6. AdSense ins unit → `(adsbygoogle = ...).push({})`
7. `<script src="/nav.js"></script>`
8. `#site-footer` with full inline footer (NOT relying on footer.js — use inline HTML)
9. `</body></html>`

## Key Rules
- NEVER use `footer.js` for article pages — the inline footer is the standard
- NEVER omit share bar or disclaimer from any article
- NEVER put nav.js AFTER the footer — it must be BEFORE the footer
- NEVER put the AdSense ins unit inside `.article-body` — it goes after `</main>`
- Footer nav "Research" link for Market Education section: label is `Market Education`, href is `/education`

## Change Log
- 2026-05-13 — Initial build — flat HTML financial research site
- 2026-05-23 — Added canonical article template, share bar standards, footer disclosure standards, article structure rules. Rebranded "Options Education" → "Market Education".
## Forecast — MD Source of Truth (Added 2026-05-26)

**Source of truth:** `entities/dependability/content/forecasts/` (MD files)
**Build script:** `entities/dependability/dependability-may26/build.py`
**Output:** `entities/dependability/website/forecast.html`
**Pipeline:** `content/forecasts/*.md` → `build.py` → `website/forecast.html` → push → CF Pages

### MD File Format
Each forecast is a dated `.md` file in `content/forecasts/`:
```
---
date: 2026-05-22
title: "S&P 500 Forecast — May 22, 2026"
description: "..."
category: FORECAST
archived: true   ← only for older forecasts (not current)
---

## [H2 Title for Bull Case Box]

[narrative paragraphs and ### subsections]

___

<!-- TARGET_GRID -->
| CURRENT | 7,473 | SPX · May 22, 2026 |
| 1 MONTH | 7,600 | +1.7% |
| 3 MONTH | 7,700 | +3.0% |
| YEAR-END 2026 | 7,700 | +3.0% base case |

___

<!-- WALL_STREET_CONSENSUS -->
| Firm | Target | Change |
| Goldman Sachs | 7,600 | +1.3% |
...

___

<!-- VOLATILITY_CONTEXT -->
| Metric | Value | Note |
| VIX (Current) | ~18–20 | Elevated but stabilizing |
...

___

### CARD: [Descriptive h3 title]

**Updated:** May 22, 2026

[card body text]

### CARD: [Next card h3 title]
**Date:** May 22, 2026
...
```

### Key Rules
- **Most recent non-archived MD** → becomes the live `forecast.html` (featured on the site)
- **Archived MDs** (with `archived: true` in front matter) → compact archive cards at bottom of forecast.html
- **Card categories** are fixed in build.py: HOW WE FORECAST, OPTIONS FRAMEWORK, MARKET COMMENTARY, KEY RISKS — do NOT change these; they are the category labels
- **`### CARD:` headings** are the h3 titles — these should be descriptive (e.g., "Our Methodology", "Positioning for the Outlook")
- **`___` separators** mark the boundary between narrative and structured data blocks
- **`<!-- TARGET_GRID -->`, `<!-- WALL_STREET_CONSENSUS -->`, `<!-- VOLATILITY_CONTEXT -->`** delimit the three structured data tables
- After editing MD files: `cd entities/dependability/dependability-may26 && python3 build.py`, then push `website/forecast.html`
- Deploy: push `entities/dependability/website/` → GitHub → CF Pages auto-deploys

### Weekly Update Process
1. Copy current forecast MD: `cp content/forecasts/2026-05-22.md content/forecasts/2026-05-29.md`
2. Edit the new file — update `date:`, `title:`, target values, narrative commentary, card dates
3. Run: `cd entities/dependability/dependability-may26 && python3 build.py`
4. Push: `cd entities/dependability/website && git add forecast.html && git commit && git push`
5. Old forecast → add `archived: true` to its front matter

## Homepage Card Layout Rule (added 2026-06-01)

**Each homepage card-grid section shows EXACTLY 3 article cards.**
- 3-column grid (`.card-grid`) with 4 cards wraps to 2+2 — visually wrong
- Template (`WEBSITE_TEMPLATE.md`) now documents this explicitly
- If fewer than 3 articles exist in a category, either: (a) wait until 3 exist, or (b) use a placeholder card that links to the hub page
- If more than 3 articles exist, pick the 3 most recent

Current homepage card sections:
- Hero sidebar: exactly 5 sidebar-article blocks (not card-grid)
- FORECASTS & OPTIONS STRATEGIES: exactly 3 article-card blocks ✓ (fixed 2026-06-01)
- EDUCATION: exactly 3 article-card education-card blocks

## Build & Deploy
- Edit HTML source in `entities/dependability/website/`
- Commit and push to `github.com/michaelbacoti/dependability-rebuild`
- Deploy via CF Pages or run `workflows/dependability/forecast-update.lobster` for full deploy
