#!/usr/bin/env python3
"""
Script to extract text from astrology PDF books for knowledge base creation.
"""

import pdfplumber
import os
import json
from pathlib import Path

BOOKS_DIR = Path("../books")
OUTPUT_DIR = Path("./extracted-books")

# Book metadata
BOOKS = {
    "predictive-astrology-of-the-hindus": {
        "file": "predictive-astrology-of-the-hindus-2009nbsped-812083416x-9788120834163_compress.pdf",
        "title": "Predictive Astrology of the Hindus",
        "author": "Unknown",
        "size_mb": 3.9
    },
    "jataka-parijata-vol-1": {
        "file": "jataka-parijata-vol-1.pdf",
        "title": "Jataka Parijata (Volume 1)",
        "author": "Unknown",
        "size_mb": 7.3
    },
    "brihat-jataka": {
        "file": "Brihat Jataka 2nd Ed. by V Subrahmanya Sastri.pdf",
        "title": "Brihat Jataka (2nd Edition)",
        "author": "V. Subrahmanya Sastri",
        "size_mb": 29.0
    }
}

def extract_pdf_text(pdf_path, output_path, max_pages=None):
    """Extract text from PDF and save to file."""
    print(f"Extracting: {pdf_path.name}")
    
    extracted_data = {
        "metadata": {},
        "pages": []
    }
    
    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        print(f"  Total pages: {total_pages}")
        
        # Extract metadata
        if pdf.metadata:
            extracted_data["metadata"] = dict(pdf.metadata)
        
        pages_to_extract = min(total_pages, max_pages) if max_pages else total_pages
        
        for i, page in enumerate(pdf.pages[:pages_to_extract]):
            text = page.extract_text()
            if text and text.strip():
                extracted_data["pages"].append({
                    "page_number": i + 1,
                    "text": text
                })
            
            if (i + 1) % 10 == 0:
                print(f"  Processed {i + 1}/{pages_to_extract} pages...")
    
    # Save as JSON
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(extracted_data, f, ensure_ascii=False, indent=2)
    
    print(f"  Saved to: {output_path}")
    print(f"  Extracted {len(extracted_data['pages'])} pages with text\n")
    
    return extracted_data

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    for book_id, book_info in BOOKS.items():
        pdf_path = BOOKS_DIR / book_info["file"]
        output_path = OUTPUT_DIR / f"{book_id}.json"
        
        if not pdf_path.exists():
            print(f"Warning: {pdf_path} not found, skipping...")
            continue
        
        try:
            extract_pdf_text(pdf_path, output_path)
        except Exception as e:
            print(f"Error extracting {book_id}: {e}")

if __name__ == "__main__":
    main()
