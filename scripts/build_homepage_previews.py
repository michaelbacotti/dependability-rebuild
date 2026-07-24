#!/usr/bin/env python3
"""
build_homepage_previews.py — Rebuild the homepage morning/afternoon preview sections.

Replaces the hardcoded <article-card> blocks in /index.html with auto-generated
previews from the latest 3 morning analysis (commentary/YYYY-MM-DD/) and the
latest 3 afternoon forecasts (forecast/YYYY-MM-DD/) on disk.

DOCTRINE (per Mike 2026-07-24 15:22 ET):
- Homepage morning section: 3 cards, newest first
- Homepage afternoon section: 3 cards, newest first
- Title style: short, clean — "Morning Update — <Date>" / "Afternoon Market Commentary — <Date>"
- Preview paragraph: ~280 chars from the article's lead paragraph (italic for morning,
  meta description for afternoon) — drops the data dump noise from the preview
- Card layout matches the existing article-card div pattern (date, label, title, paragraph)
- Featured hero + sidebar are NOT touched by this script (those are deep-dive evergreens)

The script uses the article's H1 + first lead paragraph as the clean preview,
stripping the long noisy H2 (which keeps the data dump for the full article body).

Idempotent: re-running produces the same output. Run after every cron publish.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from datetime import date, datetime

WEBSITE = Path(__file__).resolve().parent.parent  # entities/dependability/website
HOMEPAGE = WEBSITE / "index.html"
COMMENTARY = WEBSITE / "commentary"
FORECAST = WEBSITE / "forecast"

# Skip weekly forecasts in the afternoon preview rotation — they're a separate weekly slot
SKIP_DATE_SUFFIX = ("-weekly",)


def list_morning_dates(n: int = 3) -> list[str]:
    """Return the n most recent ISO dates (YYYY-MM-DD) that have a commentary/{date}/index.html."""
    if not COMMENTARY.exists():
        return []
    dates: list[str] = []
    for child in sorted(COMMENTARY.iterdir(), reverse=True):
        if not child.is_dir():
            continue
        if not child.name[:10].count("-") == 2:
            continue  # skip 'archive', 'index.html', etc.
        if (child / "index.html").exists():
            dates.append(child.name[:10])
            if len(dates) >= n:
                break
    return dates


def list_afternoon_dates(n: int = 3) -> list[str]:
    """Return the n most recent ISO dates (YYYY-MM-DD) that have a forecast/{date}/index.html,
    excluding weekly forecasts."""
    if not FORECAST.exists():
        return []
    dates: list[str] = []
    for child in sorted(FORECAST.iterdir(), reverse=True):
        if not child.is_dir():
            continue
        if not child.name[:10].count("-") == 2:
            continue
        if any(child.name.endswith(suf) for suf in SKIP_DATE_SUFFIX):
            continue
        if (child / "index.html").exists():
            dates.append(child.name[:10])
            if len(dates) >= n:
                break
    return dates


def extract_first_paragraph(html: str, prefer_italic: bool = False) -> str:
    """Extract a clean lead paragraph from the article body.

    If prefer_italic is True, look for the first <p style="...font-style:italic;">;
    otherwise fall back to the first substantive <p> in the article body.
    Returns plain text, trimmed to ~280 chars (split on sentence boundary).
    """
    # Find paragraph blocks
    if prefer_italic:
        m = re.search(
            r'<p[^>]*font-style:italic[^>]*>(.*?)</p>',
            html, re.DOTALL,
        )
        if m:
            text = re.sub(r"<[^>]+>", "", m.group(1))
            text = re.sub(r"\s+", " ", text).strip()
            if 80 <= len(text) <= 1200:
                return _trim_to_sentence(text, 280)

    # Fall back to the first <p> after the H1
    body_match = re.search(r"<h1[^>]*>.*?</h1>(.*?)<h2", html, re.DOTALL)
    if body_match:
        for p in re.findall(r"<p[^>]*>(.*?)</p>", body_match.group(1), re.DOTALL):
            text = re.sub(r"<[^>]+>", "", p)
            text = re.sub(r"\s+", " ", text).strip()
            if 100 <= len(text) <= 1200:
                return _trim_to_sentence(text, 280)

    return ""


def _trim_to_sentence(text: str, max_chars: int) -> str:
    """Trim text to max_chars, ending at the last sentence boundary."""
    if len(text) <= max_chars:
        return text
    cut = text[:max_chars]
    last_period = cut.rfind(". ")
    if last_period > 0:
        return cut[: last_period + 1]
    return cut.rstrip() + "…"


def extract_meta_description(html: str) -> str:
    """Pull the meta description (clean, used for afternoon previews)."""
    m = re.search(r'<meta name="description" content="([^"]+)"', html)
    return m.group(1) if m else ""


def format_date(d: str) -> str:
    """Convert 2026-07-24 → July 24, 2026."""
    try:
        dt = datetime.strptime(d, "%Y-%m-%d")
        return dt.strftime("%B %-d, %Y")
    except ValueError:
        return d


def build_morning_card(d: str) -> str:
    """Build one morning card HTML block."""
    path = COMMENTARY / d / "index.html"
    if not path.exists():
        return ""
    html = path.read_text(encoding="utf-8")
    preview = extract_first_paragraph(html, prefer_italic=True)
    if not preview:
        # Fall back to the meta description
        preview = extract_meta_description(html)
    preview = preview.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return f'''    <div class="article-card">
     <div class="date-text">{format_date(d)}</div>
     <div style="font-size:.65rem;font-weight:600;color:var(--color-accent);letter-spacing:.05em;text-transform:uppercase;margin-bottom:.25rem;">MORNING MARKET ANALYSIS</div>
     <h3><a href="/commentary/#morning-{d}">Morning Update — {format_date(d)}</a></h3>
     <p>{preview}</p>
    </div>'''


def build_afternoon_card(d: str) -> str:
    """Build one afternoon card HTML block."""
    path = FORECAST / d / "index.html"
    if not path.exists():
        return ""
    html = path.read_text(encoding="utf-8")
    # Use the meta description for afternoon — it's clean and already written
    preview = extract_meta_description(html)
    if not preview:
        preview = extract_first_paragraph(html, prefer_italic=False)
    # Trim to ~280 chars for the preview (drops the full data dump)
    preview = _trim_to_sentence(preview, 280)
    preview = preview.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return f'''    <div class="article-card">
     <div class="date-text">{format_date(d)}</div>
     <h3><a href="/forecast/{d}/">Afternoon Market Commentary — {format_date(d)}</a></h3>
     <p>{preview}</p>
    </div>'''


def build_section(label: str, cards: list[str]) -> str:
    """Wrap the cards in the morning/afternoon section block."""
    if not cards:
        return ""
    return (
        f'  <!-- {label} SECTION -->\n'
        f'  <section>\n'
        f'   <div class="section-header">\n'
        f'    <h2>{label}</h2>\n'
        f'    <a href="/{label.split()[0].lower()}/" class="explore-link">Explore &#8594;</a>\n'
        f'   </div>\n'
        f'   <div class="card-grid">\n\n'
        + "\n\n".join(cards)
        + "\n\n   </div>\n  </section>"
    )


def replace_section(homepage: str, start_marker: str, end_marker: str, new_block: str) -> str:
    """Replace the text between two markers (inclusive) with new_block."""
    pattern = re.compile(
        re.escape(start_marker) + r".*?" + re.escape(end_marker),
        re.DOTALL,
    )
    if not pattern.search(homepage):
        raise SystemExit(f"ERROR: cannot find markers {start_marker!r} ... {end_marker!r}")
    return pattern.sub(start_marker + "\n" + new_block + "\n\n" + end_marker, homepage)


def main() -> int:
    if not HOMEPAGE.exists():
        print(f"ERROR: {HOMEPAGE} not found", file=sys.stderr)
        return 1

    morning_dates = list_morning_dates(3)
    afternoon_dates = list_afternoon_dates(3)
    print(f"Morning previews: {morning_dates}")
    print(f"Afternoon previews: {afternoon_dates}")

    morning_cards = [build_morning_card(d) for d in morning_dates]
    afternoon_cards = [build_afternoon_card(d) for d in afternoon_dates]

    morning_block = build_section("MORNING UPDATES", morning_cards)
    afternoon_block = build_section("AFTERNOON MARKET REPORTS", afternoon_cards)

    homepage = HOMEPAGE.read_text(encoding="utf-8")

    # Replace the morning section
    homepage = replace_section(
        homepage,
        "<!-- MORNING UPDATES SECTION -->\n  <section>",
        "</section>",
        homepage[homepage.index("<!-- MORNING UPDATES SECTION"):

        homepage.index("<!-- AFTERNOON MARKET REPORTS SECTION")].rstrip().lstrip(),
    )
    # Actually, let me do a cleaner edit: find the inner card-grid and replace it
    # Use a simpler approach: find the existing blocks and replace them

    homepage = HOMEPAGE.read_text(encoding="utf-8")

    # Replace between MORNING UPDATES SECTION comment and AFTERNOON MARKET REPORTS SECTION comment
    morning_pattern = re.compile(
        r"(<!-- MORNING UPDATES SECTION -->\s*)<section>.*?(</section>)\s*(<!-- AFTERNOON MARKET REPORTS SECTION -->)",
        re.DOTALL,
    )
    new_morning = (
        "<!-- MORNING UPDATES SECTION -->\n"
        "  <section>\n"
        "   <div class=\"section-header\">\n"
        "    <h2>MORNING UPDATES</h2>\n"
        "    <a href=\"/commentary/\" class=\"explore-link\">Explore &#8594;</a>\n"
        "   </div>\n"
        "   <div class=\"card-grid\">\n\n"
        + "\n\n".join(morning_cards)
        + "\n\n   </div>\n  </section>\n\n  "
    )
    homepage, n_m = morning_pattern.subn(new_morning + "<!-- AFTERNOON MARKET REPORTS SECTION -->", homepage)

    # Replace between AFTERNOON MARKET REPORTS SECTION comment and the next section (or </main>)
    afternoon_pattern = re.compile(
        r"<!-- AFTERNOON MARKET REPORTS SECTION -->\s*<section>.*?</section>",
        re.DOTALL,
    )
    new_afternoon = (
        "<!-- AFTERNOON MARKET REPORTS SECTION -->\n"
        "  <section>\n"
        "   <div class=\"section-header\">\n"
        "    <h2>AFTERNOON MARKET REPORTS</h2>\n"
        "    <a href=\"/forecast/\" class=\"explore-link\">Explore &#8594;</a>\n"
        "   </div>\n"
        "   <div class=\"card-grid\">\n\n"
        + "\n\n".join(afternoon_cards)
        + "\n\n   </div>\n  </section>"
    )
    homepage, n_a = afternoon_pattern.subn(new_afternoon, homepage)

    if n_m != 1 or n_a != 1:
        print(f"ERROR: expected exactly 1 match each, got n_m={n_m} n_a={n_a}", file=sys.stderr)
        return 1

    HOMEPAGE.write_text(homepage, encoding="utf-8")
    print(f"OK: wrote {HOMEPAGE} with {len(morning_cards)} morning + {len(afternoon_cards)} afternoon cards")
    return 0


if __name__ == "__main__":
    sys.exit(main())
