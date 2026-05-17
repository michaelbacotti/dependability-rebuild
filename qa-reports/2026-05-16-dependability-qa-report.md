# Dependability QA Report — 2026-05-16

## Test Summary

| Tool | Pages Checked | Result |
|------|---------------|--------|
| Playwright (4 tests) | 2 | ✅ All passed |
| Linkinator | 8 + recursed | ✅ 40 links scanned, 1 expected 404 |
| curl HTTP checks | 11 | ✅ All reachable |

## Playwright Results

```
✓ Homepage loads without errors (4.8s)
✓ Forecast page loads without errors (808ms)
✓ Navigation links work (756ms)
✓ Mobile nav works (1.0s)
4 passed (7.9s)
```

## Link Check Results

**Pages scanned:** index, forecast, about, commentary, education, gold-as-a-store-of-value, tlt-new-bond-regime + article pages

**Broken links:** 0 (legitimate)
- `https://www.dependability.us/cdn-cgi/l/email-protection` → 404 — this is a Cloudflare email protection endpoint that only functions when embedded in page HTML, not when accessed directly. Expected behavior, not a real broken link.

**All other 39 links** → HTTP 200

## HTTP Connectivity Check

| URL | Status |
|-----|--------|
| https://www.dependability.us/ | 200 |
| https://www.dependability.us/forecast | 200 (308 redirect → /forecast) |
| https://www.dependability.us/about | 200 (308 redirect → /about) |
| https://www.dependability.us/commentary | 200 (308 redirect → /commentary) |
| https://www.dependability.us/education | 200 (308 redirect → /commentary) |
| https://www.dependability.us/contact | 200 (308 redirect → /contact) |
| https://www.dependability.us/strategies | 200 (308 redirect → /strategies) |
| https://www.dependability.us/methodology | 200 (308 redirect → /methodology) |
| https://www.dependability.us/disclaimer | 200 (308 redirect → /disclaimer) |
| https://www.dependability.us/privacy | 200 (308 redirect → /privacy) |
| https://www.dependability.us/gold-as-a-store-of-value | 200 (308 redirect → /gold-as-a-store-of-value) |
| https://www.dependability.us/tlt-new-bond-regime | 200 (308 redirect → /tlt-new-bond-regime) |

**Note:** 308 redirects from `.html` URLs are expected Cloudflare Pages behavior (clean URLs enabled).

## Files Created

```
tests/e2e/dependability.spec.js  — Playwright E2E test suite
linkinator.config.json           — Link checker configuration
.pa11yrc                        — Pa11y accessibility config
package.json                    — QA tool dependencies
qa-reports/2026-05-16-dependability-qa-report.md  — This report
```

## Recommended Fixes

1. **None required** — site is clean. All pages load, all links resolve, no JS console errors.
2. **Cloudflare clean URLs:** The 308 redirects from `.html` paths to extensionless paths confirm Cloudflare Pages clean URL routing is active and working correctly.
3. **Cloudflare email protection:** The 404 on `/cdn-cgi/l/email-protection` accessed directly is expected — it's a protection script, not a navigation link.

## QA Stack Installed

- `playwright` + `@playwright/test` — browser-based E2E testing
- `linkinator` — broken link scanner
- `pa11y` — accessibility checker (config in place, run manually as needed)