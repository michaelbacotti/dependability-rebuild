# PROJECT_INDEX — Dependability (dependability.us)

> Signalhouse — Market & Regime Intelligence
> Last updated: 2026-07-05

## Purpose & Audience

Dependability is a living signal hub for macro markets, regimes, and options overlays. It publishes recurring structured notes (daily market notes, weekly regime reports, evergreen explainers) that build an audience of self-directed investors. The Signalhouse treats market data as intelligence to be interpreted, not just reported.

**Audience:** Self-directed investors, options traders, macro thinkers who appreciate structured regime analysis. Educational focus — not personal investment advice.

---

## Live-Site Paths

```
entities/dependability/website/   ← dependability-rebuild GitHub repo
  signalhouse/                    ← Signalhouse content (ALLOWED WRITE PATH)
    daily/                         ← daily market notes
    weekly/                        ← weekly regime reports
    evergreen/                     ← concept explainers
    drafts/                        ← draft notes awaiting review
  articles/                        ← ALLOWED WRITE PATH
```

**Protected (do not edit without explicit human approval):**
- `about/`, `contact/`, `disclaimer/`, `privacy/`, `commentary/`
- `build.py`, `_template*`, nav files
- Home page, sitemap, robots.txt

---

## Core Content Lanes

### Daily Market Notes (3x/week)
- Summary of what changed (macro, rates, volatility, sector rotation)
- Key chart levels
- Notable events list
- Filename format: `YYYY-MM-DD.md`

### Weekly Regime Reports
- Macro regime assessment (inflation, growth, policy, liquidity, breadth)
- Sector and factor rotation
- Volatility regime
- Option overlay observations

### Evergreen Explainers
- Concepts: term structure, gamma, skew, realized vs. implied volatility, etc.
- Updated when regimes change or thinking is refined

---

## Monetization

| Method | Where |
|--------|-------|
| AdSense | Daily notes, weekly reports, evergreen pages |
| OptionStrat affiliate | `?ref=ventureprise` on ALL OptionStrat links in signalhouse content |

**⚠️ OptionStrat Affiliate Rule (MANDATORY):**
Every link to OptionStrat from any dependability.us/signalhouse page MUST include `?ref=ventureprise`.
Example: `https://optionstrat.com/ventureprise` or `https://optionstrat.com/build?ref=ventureprise`

---

## Key Files

- **Forecast cron:** card `99ff0c15`, runs 5pm ET (already running)
- **OptionStrat affiliate:** `?ref=ventureprise` on all OptionStrat links
- PS Ledger: `memory/ledgers/dependability-holding-llc/profit-share-ledger.md`

---

## Status & Pending Tasks

- [x] Forecast cron running (card `99ff0c15`, 5pm ET)
- [ ] LIP-06: Weekly template review + OptionStrat enforcement on all existing signalhouse pages
- [ ] LIP-06: OptionStrat affiliate scan — check all existing pages for missing `?ref=ventureprise`
- [ ] Evergreen library organization

---

## Related Documents

- `Reports/LIVING_INTELLIGENCE_PROPERTIES.md` — Dependability section
- `Reports/LIVING_INTELLIGENCE_IMPLEMENTATION.md` — §4.4 (OptionStrat integration)
- `entities/dependability/website/PROJECT_PLAYBOOK.md`
- `skills/dependability.signalhouse` — skill proposal (pending approval)
- Existing skill: `skills/dependability-content-publishing/SKILL.md`

## Source

Wiki synthesis: `wiki/main/syntheses/living-intelligence-properties-strategy.md`
