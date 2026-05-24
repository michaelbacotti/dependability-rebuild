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