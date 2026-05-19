#!/usr/bin/env python3
"""Fix dependability.us sitemap: sitemap has .html URLs but site redirects .html → non-.html (canonical style)"""

sitemap_path = "/Users/mike/.openclaw/workspace-bacottibot/websites/dependability-rebuild/sitemap.xml"

with open(sitemap_path, "r") as f:
    content = f.read()

# Remove .html suffix from all URL paths
# https://dependability.us/about.html -> https://dependability.us/about
# But keep the root / and articles/ paths which are fine
import re

# Fix .html pages that should be non-.html
replacements = [
    ("https://dependability.us/about.html", "https://dependability.us/about"),
    ("https://dependability.us/contact.html", "https://dependability.us/contact"),
    ("https://dependability.us/disclaimer.html", "https://dependability.us/disclaimer"),
    ("https://dependability.us/education.html", "https://dependability.us/education"),
    ("https://dependability.us/forecast.html", "https://dependability.us/forecast"),
    ("https://dependability.us/gold-as-a-store-of-value.html", "https://dependability.us/gold-as-a-store-of-value"),
    ("https://dependability.us/inflation-measurement-modern-economy.html", "https://dependability.us/inflation-measurement-modern-economy"),
    ("https://dependability.us/methodology.html", "https://dependability.us/methodology"),
    ("https://dependability.us/oil-paradox-energy-dominance.html", "https://dependability.us/oil-paradox-energy-dominance"),
    ("https://dependability.us/privacy.html", "https://dependability.us/privacy"),
    ("https://dependability.us/strategies.html", "https://dependability.us/strategies"),
    ("https://dependability.us/tlt-new-bond-regime.html", "https://dependability.us/tlt-new-bond-regime"),
    ("https://dependability.us/the-dollars-lever.html", "https://dependability.us/the-dollars-lever"),
    # Article pages already use .html in path, they don't redirect - keep as-is
    # Top-level index, about, commentary, disclaimer etc need .html removed
]

for old, new in replacements:
    content = content.replace(old, new)

with open(sitemap_path, "w") as f:
    f.write(content)

print("Done. New sitemap URLs:")
for line in content.split('\n'):
    if '<loc>' in line:
        print(line.strip().replace('<loc>','').replace('</loc>',''))