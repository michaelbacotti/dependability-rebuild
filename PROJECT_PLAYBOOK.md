# PROJECT_PLAYBOOK — Dependability Signalhouse (dependability.us)

> How to work in the Dependability Signalhouse
> Last updated: 2026-07-05

---

## Daily Market Note Workflow

1. **Check data sources.** Identify safe, TOS-compliant public sources:
   - Free macro dashboards (FRED, Yahoo Finance, etc.)
   - ETF websites for fund flows
   - Economic calendars for scheduled releases
   - Central bank statements / Fed communications

2. **Draft note** using `templates/signalhouse_daily_template.md`:
   - Date in filename: `signalhouse/daily/YYYY-MM-DD.md`
   - Sections: "What changed", "Key levels", "Notable events"
   - Keep it structured, scannable, 300–600 words
   - Link to OptionStrat with `?ref=ventureprise` when showing payoff diagrams or strategy builders

3. **Save draft** to `signalhouse/drafts/YYYY-MM-DD-draft.md`

4. **Review and move** to `signalhouse/daily/YYYY-MM-DD.md` when ready

5. **Rebuild:** Run `build.py` from `entities/dependability/website/` to regenerate HTML

---

## Weekly Regime Report Workflow

1. **Gather data for the week:**
   - Major macro data releases and surprises
   - Fed / central bank communications
   - Equity, bond, commodity, and volatility market behavior
   - Sector and factor performance
   - Options market structure (volatility term structure, skew)

2. **Draft report** using `templates/signalhouse_weekly_template.md`:
   - Filename: `signalhouse/weekly/YYYY-WXX.md` (week number)
   - Sections: "Regime assessment", "Key changes", "Sector/factor rotation", "Vol regime", "Option overlay observations"
   - 600–1000 words

3. **Save to:** `signalhouse/weekly/YYYY-WXX.md`

4. **OptionStrat links:** Always include `?ref=ventureprise` on any OptionStrat URL

---

## Evergreen Explainer Workflow

1. **Pick a concept** that hasn't been covered or needs updating (term structure, gamma, skew, realized vs. implied vol, etc.)

2. **Draft** using `templates/signalhouse_evergreen_template.md`:
   - Explain the concept clearly for a self-directed investor
   - Include a concrete example or chart reference
   - Link to OptionStrat for interactive tools (`?ref=ventureprise`)
   - Keep it authoritative, not promotional

3. **Save to:** `signalhouse/evergreen/[concept-slug].md`

4. **Human review recommended** before publishing evergreen content (it has a longer shelf life = higher stakes if wrong)

---

## ⚠️ OptionStrat Affiliate Enforcement (MANDATORY)

**Rule:** Every OptionStrat link in signalhouse content MUST end with `?ref=ventureprise`.

**Example links:**
- ✅ `https://optionstrat.com/ventureprise`
- ✅ `https://optionstrat.com/build?ref=ventureprise`
- ❌ `https://optionstrat.com/` (missing ref parameter)
- ❌ `https://optionstrat.com/build` (missing ref parameter)

**How to check:**
```bash
grep -r "optionstrat.com" entities/dependability/website/signalhouse/ --include="*.md"
# Any link without ?ref=ventureprise needs fixing
```

**LIP-06 task:** Run this check across all existing signalhouse pages and fix any missing `?ref=ventureprise` parameters.

---

## Templates to Use

| Template | Location | Use for |
|----------|----------|---------|
| `signalhouse_daily_template.md` | `entities/dependability/website/templates/` | Daily market notes |
| `signalhouse_weekly_template.md` | `entities/dependability/website/templates/` | Weekly regime reports |
| `signalhouse_evergreen_template.md` | `entities/dependability/website/templates/` | Evergreen concept explainers |

---

## Approval Workflow

| Action | Who approves |
|--------|-------------|
| Daily note publication | Agent can publish (existing cron handles) |
| New evergreen explainer | Human review recommended |
| Major updates to existing evergreen | Human review recommended |
| OptionStrat link check / fix | Agent can act autonomously |
| Changes to home page, nav, legal, disclaimer | Human required |
| Bulk (>10 pages at once) | Human review first |

---

## Quality Bar

- Daily notes: structured, factual, no hype, no investment advice
- Weekly reports: analytical, opinionated where appropriate, connects dots
- Evergreen: accurate definitions, clear examples, lasting value
- OptionStrat links: always with `?ref=ventureprise`

---

## Reference

- Implementation §4.4 (OptionStrat integration — MANDATORY READ)
- `Reports/LIVING_INTELLIGENCE_PROPERTIES.md` — Dependability section
- `entities/dependability/website/PROJECT_INDEX.md`
- `skills/dependability.signalhouse` — skill proposal (pending approval)
