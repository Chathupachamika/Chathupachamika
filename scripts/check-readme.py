#!/usr/bin/env python3
"""Local README checks: assets exist, SVGs parse, alt text present, placeholders flagged,
duplicate headings, and required URLs preserved. Run: python3 scripts/check-readme.py"""
import re, sys, pathlib, xml.dom.minidom

root = pathlib.Path(__file__).resolve().parent.parent
readme = (root / "README.md").read_text(encoding="utf-8")
errors, warnings = [], []

# 1. local assets referenced by README exist
for ref in set(re.findall(r'(?:src|srcset)="(\./[^"]+|assets/[^"]+)"', readme)):
    if not (root / ref.lstrip("./")).exists():
        errors.append(f"missing asset: {ref}")

# 2. every SVG is well-formed XML
for svg in (root / "assets").glob("*.svg"):
    try:
        xml.dom.minidom.parse(str(svg))
    except Exception as e:
        errors.append(f"invalid SVG {svg.name}: {e}")

# 3. images without alt attribute
for tag in re.findall(r"<img\b[^>]*>", readme):
    if "alt=" not in tag:
        errors.append(f"img without alt: {tag[:70]}...")

# 4. duplicate headings
heads = re.findall(r"^#{1,4}\s+(.+)$", readme, re.M)
for h in set(heads):
    if heads.count(h) > 1:
        warnings.append(f"duplicate heading: {h}")

# 5. placeholders still present
for ph in ("REPO_NAME", "YOUR_", "TODO"):
    if ph in readme:
        warnings.append(f"placeholder text still present: {ph}")

# 6. original URLs preserved
required = [
    "http://portfolio20041119.s3-website.eu-north-1.amazonaws.com/",
    "Chathupachamika765@gmail.com",
    "https://twitter.com/chathupachamika",
    "https://www.linkedin.com/in/chathupa-chamika-/",
    "https://web.facebook.com/chathupa.chamika.7",
    "https://wa.me/+94754278741",
    "https://instagram.com/chathupachamika",
    "https://www.buymeacoffee.com/chathupache",
    "https://ko-fi.com/chathupachamika",
]
for url in required:
    if url not in readme:
        errors.append(f"required URL missing: {url}")

for w in warnings: print("WARN ", w)
for e in errors: print("ERROR", e)
print(f"{len(errors)} error(s), {len(warnings)} warning(s)")
sys.exit(1 if errors else 0)
