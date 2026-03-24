"""
PDF Analyzer Agent
Extracts text, formulas, images, and structure from PDF files.
"""

import re
import os
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import pdfplumber
from PIL import Image
import io


class PDFAnalyzer:
    """Analyzes PDF files and extracts mathematical content."""

    def __init__(self, config: Dict):
        self.config = config
        self.pdf_config = config.get('pdf', {})

    def analyze(self, pdf_path: str, output_dir: str) -> Dict:
        """
        Analyze a PDF file and extract all relevant content.

        Args:
            pdf_path: Path to the PDF file
            output_dir: Directory to save extracted assets

        Returns:
            Dictionary containing extracted content
        """
        pdf_path = Path(pdf_path)
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        result = {
            'file_name': pdf_path.name,
            'pages': [],
            'full_text': '',
            'formulas': [],
            'images': [],
            'sections': [],
            'metadata': {}
        }

        with pdfplumber.open(pdf_path) as pdf:
            result['metadata'] = {
                'num_pages': len(pdf.pages),
                'info': pdf.metadata
            }

            max_pages = self.pdf_config.get('max_pages', 0)
            pages_to_process = pdf.pages if max_pages == 0 else pdf.pages[:max_pages]

            for page_num, page in enumerate(pages_to_process, start=1):
                page_data = self._process_page(page, page_num, output_dir)
                result['pages'].append(page_data)
                result['full_text'] += page_data['text'] + '\n\n'

            # Extract formulas from full text
            result['formulas'] = self._extract_formulas(result['full_text'])

            # Identify sections and structure
            result['sections'] = self._identify_sections(result['full_text'])

        return result

    def _process_page(self, page, page_num: int, output_dir: Path) -> Dict:
        """Process a single PDF page."""
        page_data = {
            'page_number': page_num,
            'text': '',
            'images': [],
            'tables': []
        }

        # Extract text
        text = page.extract_text()
        if text:
            page_data['text'] = text

        # Extract images if configured
        if self.pdf_config.get('extract_images', True):
            images = self._extract_images_from_page(page, page_num, output_dir)
            page_data['images'] = images

        # Extract tables
        tables = page.extract_tables()
        if tables:
            page_data['tables'] = tables

        return page_data

    def _extract_images_from_page(self, page, page_num: int, output_dir: Path) -> List[str]:
        """Extract images from a PDF page."""
        extracted_images = []

        try:
            # Note: pdfplumber doesn't directly extract images
            # This is a placeholder - you may need to use PyPDF2 or another library
            # for more sophisticated image extraction
            pass
        except Exception as e:
            print(f"Warning: Could not extract images from page {page_num}: {e}")

        return extracted_images

    def _extract_formulas(self, text: str) -> List[Dict]:
        """
        Extract LaTeX-style formulas from text.
        Looks for patterns like $...$ or $$...$$
        """
        formulas = []

        # Pattern for inline math $...$
        inline_pattern = r'\$([^\$]+)\$'
        inline_matches = re.finditer(inline_pattern, text)
        for match in inline_matches:
            formulas.append({
                'type': 'inline',
                'content': match.group(1).strip(),
                'raw': match.group(0)
            })

        # Pattern for display math $$...$$
        display_pattern = r'\$\$([^\$]+)\$\$'
        display_matches = re.finditer(display_pattern, text)
        for match in display_matches:
            formulas.append({
                'type': 'display',
                'content': match.group(1).strip(),
                'raw': match.group(0)
            })

        return formulas

    def _identify_sections(self, text: str) -> List[Dict]:
        """
        Identify sections in the document (chapters, sections, subsections).
        """
        sections = []

        # Look for common section patterns
        patterns = [
            (r'^Chapter\s+(\d+):?\s*(.+)$', 'chapter'),
            (r'^Section\s+(\d+\.?\d*):?\s*(.+)$', 'section'),
            (r'^(\d+\.\d+)\s+(.+)$', 'subsection'),
            (r'^([A-Z][A-Z\s]+)$', 'heading'),  # ALL CAPS headings
        ]

        lines = text.split('\n')
        for line_num, line in enumerate(lines, start=1):
            line = line.strip()
            if not line:
                continue

            for pattern, section_type in patterns:
                match = re.match(pattern, line)
                if match:
                    sections.append({
                        'type': section_type,
                        'line_number': line_num,
                        'title': line,
                        'number': match.group(1) if match.lastindex >= 1 else None
                    })
                    break

        return sections

    def get_text_summary(self, analysis: Dict) -> str:
        """Generate a summary of the extracted text."""
        total_chars = len(analysis['full_text'])
        total_words = len(analysis['full_text'].split())
        num_pages = len(analysis['pages'])
        num_formulas = len(analysis['formulas'])
        num_sections = len(analysis['sections'])

        summary = f"""PDF Analysis Summary:
- File: {analysis['file_name']}
- Pages: {num_pages}
- Characters: {total_chars:,}
- Words: {total_words:,}
- Formulas detected: {num_formulas}
- Sections identified: {num_sections}
"""
        return summary


def main():
    """Test the PDF analyzer."""
    import yaml

    # Load config
    config_path = Path(__file__).parent.parent / 'config.yaml'
    with open(config_path) as f:
        config = yaml.safe_load(f)

    # Example usage
    analyzer = PDFAnalyzer(config)

    # Test with a sample PDF (you'll need to provide a path)
    # result = analyzer.analyze('sample.pdf', './temp/test_output')
    # print(analyzer.get_text_summary(result))


if __name__ == '__main__':
    main()
