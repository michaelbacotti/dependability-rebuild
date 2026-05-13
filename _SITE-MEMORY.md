# SITE MEMORY — Dependability Holdings LLC

## Identity
- Entity: Dependability Holdings LLC
- Purpose: Financial research website — market commentary, options education, S&P 500 / VIX forecasting
- Repo: github.com/michaelbacotti/dependability-rebuild
- Live URL: dependability.us (pending migration from GitHub Actions)
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

## Change Log
- 2026-05-13 — Initial build — flat HTML financial research site