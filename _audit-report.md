# Dependability Website Audit Report
**Date:** 2026-05-15  
**Auditor:** Subagent  
**Live site:** https://www.dependability.us  
**GitHub:** michaelbacotti/dependability-rebuild  

---

## Pages Audited: 18 total
- Root HTML: 12 pages (_template.html, about, commentary, contact, disclaimer, education, forecast, gold-as-a-store-of-value, index, methodology, privacy, strategies, tlt-new-bond-regime)
- Articles: 5 pages (2026-05-10-iv-crush-explained, 2026-05-12-market-outlook, 2026-05-13-research-themes, 2026-05-13-trump-china-summit, 2026-05-14-spacex-ipo-etf-exposure)

---

## ISSUES FOUND & FIXED

### ✅ FIXED — Missing Canonical Tags (14 pages)
**Problem:** Only `gold-as-a-store-of-value.html` had a canonical tag. All 5 articles and 10 other pages were missing it.

**Fixed:** Added `<link rel="canonical">` to all 14 pages:
- index.html, about.html, commentary.html, contact.html, disclaimer.html, education.html, forecast.html, methodology.html, privacy.html, strategies.html, tlt-new-bond-regime.html
- articles/2026-05-10-iv-crush-explained.html
- articles/2026-05-12-market-outlook.html
- articles/2026-05-13-research-themes.html
- articles/2026-05-13-trump-china-summit.html
- articles/2026-05-14-spacex-ipo-etf-exposure.html

### ✅ FIXED — Missing Hero Images (9 pages)
**Problem:** 9 pages had no image, which hurts AdSense performance and engagement for financial content.

**Fixed:** Generated and added hero images to all 9 pages:
- about.html → `articles/about-hero.png`
- commentary.html → `articles/commentary-hero.png`
- education.html → `articles/education-hero.png`
- forecast.html → `articles/forecast-hero.png`
- methodology.html → `articles/methodology-hero.png`
- privacy.html → `articles/privacy-hero.png`
- disclaimer.html → `articles/disclaimer-hero.png`
- contact.html → `articles/contact-hero.png`
- strategies.html → `articles/strategies-hero.png`

Images generated via OpenAI gpt-image-2 (professional financial research aesthetic).

### ✅ VERIFIED — AdSense Script
All 18 pages already had the AdSense script tag: `<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9312870448453345" crossorigin="anonymous">`

### ✅ VERIFIED — Internal Links
All internal links use consistent `/path` format. No broken links detected.

### ⚠️ STILL NEEDS WORK — Content Expansion (LOW PRIORITY)
These pages have ~800-900 words (borderline for AdSense competitive content):
- forecast.html: 918 words
- strategies.html: 881 words

The content is substantive but could be expanded with more specific data points, historical context, and actionable examples.

---

## SUMMARY
| Metric | Value |
|--------|-------|
| Pages audited | 18 |
| Canonical tags added | 14 |
| Hero images added | 9 |
| AdSense script present | 18/18 (100%) |
| Internal links | All consistent |
| Git commit | 9fe06f9 |
| Status | ✅ PUSHED to main |

---

## Notes
- Pages already had good canonical tags after `gold-as-a-store-of-value` was created — all others were missed
- Images are large (~2.5-3MB each) — may want to compress before production
- All article pages in `/articles/` already had hero images with the `.png` file alongside each `.html` file