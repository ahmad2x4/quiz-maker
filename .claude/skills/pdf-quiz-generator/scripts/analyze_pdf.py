#!/usr/bin/env python3
"""
PDF Analyzer Script
Extracts text, formulas, and structure from PDF files for quiz generation.
"""

import sys
import json
from pathlib import Path

try:
    import pdfplumber
    HAS_PDFPLUMBER = True
except ImportError:
    HAS_PDFPLUMBER = False
    print("Warning: pdfplumber not installed. Install with: pip install pdfplumber", file=sys.stderr)


def analyze_pdf(pdf_path):
    """Extract content from PDF file."""
    if not HAS_PDFPLUMBER:
        return {"error": "pdfplumber not installed"}

    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        return {"error": f"File not found: {pdf_path}"}

    result = {
        "file_name": pdf_path.name,
        "pages": [],
        "full_text": "",
        "total_pages": 0
    }

    try:
        with pdfplumber.open(pdf_path) as pdf:
            result["total_pages"] = len(pdf.pages)

            for page_num, page in enumerate(pdf.pages, start=1):
                text = page.extract_text() or ""
                result["pages"].append({
                    "page_number": page_num,
                    "text": text
                })
                result["full_text"] += text + "\n\n"

        return result

    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_pdf.py <pdf_file>", file=sys.stderr)
        sys.exit(1)

    pdf_path = sys.argv[1]
    result = analyze_pdf(pdf_path)

    print(json.dumps(result, indent=2))
