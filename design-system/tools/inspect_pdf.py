#!/usr/bin/env python3
"""Inspect PDF page geometry, font metadata, text sizes/colors, and text positions.
Requires: py -m pip install pymupdf
Usage: py tools\\inspect_pdf.py reference\\brittany-chiang-resume.pdf
"""
from collections import Counter
from pathlib import Path
import hashlib, json, sys

try:
    import fitz
except ImportError:
    raise SystemExit("Install PyMuPDF first: py -m pip install pymupdf")

if len(sys.argv) != 2:
    raise SystemExit("Usage: python tools/inspect_pdf.py path/to/file.pdf")
path = Path(sys.argv[1])
if not path.is_file():
    raise SystemExit(f"File not found: {path}")

doc = fitz.open(path)
print("FILE:", path)
print("SHA-256:", hashlib.sha256(path.read_bytes()).hexdigest())
print("PAGE COUNT:", len(doc))
print("METADATA:", json.dumps(doc.metadata, indent=2, ensure_ascii=False))

for number, page in enumerate(doc, 1):
    rect = page.rect
    print(f"\\n{'=' * 72}\\nPAGE {number}")
    print(f"SIZE: {rect.width:.2f} x {rect.height:.2f} pt "
          f"({rect.width/72:.3f} x {rect.height/72:.3f} in)")
    print("FONTS:")
    for font in page.get_fonts(full=True):
        print(" ", repr(font))

    fonts, sizes, colors = Counter(), Counter(), Counter()
    spans = []
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for span in line["spans"]:
                value = span.get("text", "")
                if not value.strip():
                    continue
                font = span.get("font", "?")
                size = round(span.get("size", 0), 2)
                color = f"#{span.get('color', 0):06x}"
                fonts[font] += len(value)
                sizes[size] += len(value)
                colors[color] += len(value)
                spans.append({
                    "bbox_pt": [round(v, 2) for v in span.get("bbox", [])],
                    "font": font, "size_pt": size, "color": color,
                    "flags": span.get("flags"), "text": value
                })
    print("FONT USAGE:", fonts.most_common())
    print("FONT SIZES:", sizes.most_common())
    print("TEXT COLORS:", colors.most_common())
    print("TEXT SPANS (bbox uses top-left origin; units are points):")
    for span in spans:
        print(" ", json.dumps(span, ensure_ascii=False))

print("\\nNote: fonts may be subsetted and PDF text colors may not describe the page background.")
print("Use a rendered page alongside these measurements; extraction cannot capture all optical details.")
