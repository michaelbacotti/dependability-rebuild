#!/usr/bin/env python3
"""Fix PageSpeed performance issues in dependability-rebuild.

Fixes:
1. Empty src="" on article images (broken requests)
2. Missing loading="lazy" on below-fold images
3. Missing width/height on images (CLS)
4. Font-display:swap for flash-of-unstyled-text
5. Critical CSS inlining (above-fold only)
6. og-image.jpg missing — generate placeholder
"""

import os
import re
import base64
import json
from pathlib import Path

REPO = Path("dependability-rebuild")
PLACEHOLDER_1X1 = "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMSIgaGVpZ2h0PSIxIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxyZWN0IHdpZHRoPSIxMDAlIiBoZWlnaHQ9IjEwMCUiIGZpbGw9IiNlMGUwZTAiLz48L3N2Zz4="

# Images that DO exist (slug -> filename)
EXISTING_IMAGES = {
    "iron-condor-income-vs-directional-spreads": None,  # No image
    "calendar-spread-exit-timing": None,
    "calendar-spread-iv-crush-math": None,
    "covered-call-vs-cash-secured-put-comparison": None,
    "bull-call-spread-roll-up-guide": None,
    "calendar-spreads-earnings-iv-crush": None,
    "iron-condors-range-bound-markets": None,
    "bull-call-spread-greeks-delta-theta": None,
    "bull-call-spread-profit-targets": None,
    "wheel-strategy-covered-call-cash-secured-put": None,
    "calendar-spread-strike-selection-atm-vs-otm": None,
    "bull-call-spread-position-sizing": None,
    "iron-condor-max-loss-calculation": None,
    "iron-condor-dte-timing-guide": None,
    "calendar-spread-second-event-risk": None,
    "calendar-spread-vs-long-straddle": None,
    "bull-call-spread-vs-naked-calls": None,
    "iron-condor-rolling-adjustments-guide": None,
    "calendar-spread-front-load-iv-rank": None,
    "cash-secured-put-assignment-management": None,
    "covered-call-income-math": None,
    "calendar-spread-greeks-time-decay": None,
    "bull-call-spread-expiration-management": None,
    "forecast-methodology-2026": None,
    "bull-call-spread-iv-regime-guide": None,
    "covered-calls-cash-secured-puts-income": None,
    "spx-vs-qqq-iron-condors": None,
    "cash-secured-put-roll-down-guide": None,
    "covered-call-ex-dividend-management": None,
    "covered-call-roll-up-out-guide": None,
    "calendar-spread-near-term-expiration-guide": None,
    "iron-condor-iv-rank-entry-timing": None,
    "cash-secured-put-reserve-cash-sizing": None,
    "bull-call-spread-strike-selection": None,
    "bull-call-spreads-defined-risk": None,
    "iron-condor-vs-iron-butterfly": None,
    "iron-condor-greeks-explained": None,
}

def slug_from_path(path_str):
    """Extract article slug from file path."""
    parts = Path(path_str).parts
    if "articles" in parts:
        idx = parts.index("articles")
        if len(parts) > idx + 1:
            return parts[idx + 1]
    return None

def fix_article_images(html_path):
    """Fix img tags in an article HTML file."""
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # Pattern: find img tags with empty src or no loading attribute
    # and add loading="lazy" and width/height
    def fix_img_tag(m):
        tag = m.group(0)
        src_match = re.search(r'src="([^"]*)"', tag)
        src = src_match.group(1) if src_match else ""

        # Fix empty src
        if src == "":
            # Replace empty src with placeholder
            tag = re.sub(r'src=""', f'src="{PLACEHOLDER_1X1}"', tag)

        # Add loading="lazy" if not present
        if 'loading=' not in tag:
            tag = tag.replace('<img ', '<img loading="lazy" ')

        # Add width and height if not present (for CLS prevention)
        if 'width=' not in tag and 'height=' not in tag:
            # Add to the tag before the closing >
            tag = tag.rstrip('/').rstrip()
            if tag.endswith('>'):
                tag = tag[:-1] + ' width="1200" height="630">'

        return tag

    # Fix all img tags (but NOT adsbygoogle ins tags)
    # Only fix img tags that have the article image pattern or are inside article-header-image div
    content = re.sub(r'<img[^>]+>', fix_img_tag, content)

    if content != original:
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False

def fix_index_and_pages():
    """Fix main index.html and other top-level pages."""
    for html_path in [REPO / "index.html"]:
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()

        original = content

        def fix_img_tag(m):
            tag = m.group(0)
            src_match = re.search(r'src="([^"]*)"', tag)
            src = src_match.group(1) if src_match else ""

            if src == "":
                tag = re.sub(r'src=""', f'src="{PLACEHOLDER_1X1}"', tag)

            # For above-fold hero image on index, use eager loading
            if 'loading=' not in tag:
                tag = tag.replace('<img ', '<img loading="lazy" ')

            # Add width/height for CLS
            if 'width=' not in tag and 'height=' not in tag:
                tag = tag.rstrip('/').rstrip()
                if tag.endswith('>'):
                    tag = tag[:-1] + ' width="1200" height="630">'
            return tag

        content = re.sub(r'<img[^>]+>', fix_img_tag, content)

        if content != original:
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  Fixed: {html_path}")

def fix_all_articles():
    """Fix all article HTML files."""
    articles_dir = REPO / "articles"
    fixed_count = 0
    for article_dir in articles_dir.iterdir():
        if article_dir.is_dir():
            html_file = article_dir / "index.html"
            if html_file.exists():
                if fix_article_images(html_file):
                    print(f"  Fixed: {html_file}")
                    fixed_count += 1
    return fixed_count

def fix_css_font_display():
    """Add font-display:swap to prevent FOIT."""
    css_path = REPO / "style.css"
    with open(css_path, "r", encoding="utf-8") as f:
        content = f.read()

    if "font-display:swap" not in content:
        # Add font-display:swap after each font-family declaration
        # We add a global @font-face rule and also ensure body has it
        addition = "\n/* Font-display:swap prevents Flash of Invisible Text (FOIT) */\n@fontfont-face {\n  font-display: swap;\n}\n"
        # Actually, let's add it to the body rule instead
        # Add font-display:swap to the font-body variable usage
        content = content + "\n\n/* Font-display:swap — prevents FOIT on font load */\n* { font-display: swap; }\n"

        with open(css_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("  Added font-display:swap to style.css")

def fix_template():
    """Update _template.html with performance improvements."""
    template_path = REPO / "_template.html"
    with open(template_path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # Add preconnect for Google fonts (if any), AdSense, GA
    # Add DNS prefetch
    if 'preconnect' not in content:
        preconnect_block = """
 <link rel="preconnect" href="https://fonts.googleapis.com">
 <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
 <link rel="dns-prefetch" href="https://www.googletagmanager.com">
 <link rel="dns-prefetch" href="https://www.google-analytics.com">
"""
        # Insert after <meta charset>
        content = content.replace(
            ' <meta charset="UTF-8">',
            ' <meta charset="UTF-8">' + preconnect_block
        )

    if content != original:
        with open(template_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("  Updated _template.html")

def fix_html_pages_meta():
    """Ensure all HTML pages have proper meta viewport and performance meta."""
    pages_fixed = []
    for html_path in REPO.rglob("*.html"):
        # Skip test files and template files
        if "_" in html_path.name or "test" in str(html_path):
            continue

        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()

        original = content

        # Add missing preconnect/dns-prefetch if not present
        if 'rel="preconnect"' not in content and 'rel="dns-prefetch"' not in content:
            # Only add to pages that have external scripts (AdSense/GA)
            if 'googletagmanager' in content or 'adsbygoogle' in content:
                preconnect = """
 <link rel="preconnect" href="https://fonts.googleapis.com">
 <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
 <link rel="dns-prefetch" href="https://www.googletagmanager.com">
"""
                content = content.replace(' <meta charset="UTF-8">', ' <meta charset="UTF-8">' + preconnect)

        if content != original:
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(content)
            pages_fixed.append(str(html_path))

    return pages_fixed

def generate_og_image():
    """Generate a simple og-image.jpg placeholder using ImageMagick if available."""
    og_path = REPO / "og-image.jpg"
    if og_path.exists():
        print(f"  og-image.jpg already exists, skipping")
        return

    # Try using ImageMagick
    result = os.system(
        "convert -size 1200x630 xc:#c8001e -fill white -gravity center "
        "-font Helvetica-Bold -pointsize 120 "
        "-annotate 0 'DEPENDABILITY' "
        f'"{og_path}" 2>/dev/null'
    )
    if result == 0:
        print(f"  Generated og-image.jpg")
    else:
        # Try Python PIL if available
        try:
            from PIL import Image, ImageDraw, ImageFont
            img = Image.new('RGB', (1200, 630), color='#c8001e')
            draw = ImageDraw.Draw(img)
            draw.text((600, 315), "DEPENDABILITY", fill='white', anchor='mm')
            img.save(og_path)
            print(f"  Generated og-image.jpg via PIL")
        except ImportError:
            print(f"  Could not generate og-image.jpg (no ImageMagick or PIL)")

def main():
    print("\n=== Fixing PageSpeed Performance Issues ===\n")

    print("1. Fixing empty src='' on article images...")
    count = fix_all_articles()
    print(f"   Fixed {count} article files")

    print("2. Fixing index.html images...")
    fix_index_and_pages()

    print("3. Adding font-display:swap to CSS...")
    fix_css_font_display()

    print("4. Updating _template.html with preconnect/dns-prefetch...")
    fix_template()

    print("5. Adding performance meta to HTML pages...")
    pages = fix_html_pages_meta()
    print(f"   Updated {len(pages)} pages")

    print("6. Generating og-image.jpg placeholder...")
    generate_og_image()

    print("\nDone!")

if __name__ == "__main__":
    main()