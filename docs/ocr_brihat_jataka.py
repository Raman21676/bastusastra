#!/usr/bin/env python3
"""
OCR Script for Brihat Jataka
Extracts text from scanned PDF using Tesseract OCR
"""

import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
import os
import json
import sys

def check_tesseract():
    """Check if tesseract is installed"""
    try:
        version = pytesseract.get_tesseract_version()
        print(f"✓ Tesseract found: {version}")
        return True
    except Exception as e:
        print(f"✗ Tesseract not available: {e}")
        return False

def extract_page_as_image(doc, page_num, zoom=2):
    """Extract a page as a PIL Image"""
    page = doc[page_num]
    
    # Set zoom factor for better OCR quality
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    
    # Convert to PIL Image
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    
    return img

def ocr_page(image, lang='eng'):
    """Perform OCR on an image"""
    # Configure tesseract for better accuracy with old books
    custom_config = r'--oem 3 --psm 6'
    
    text = pytesseract.image_to_string(image, lang=lang, config=custom_config)
    return text

def process_book(pdf_path, output_path, start_page=0, end_page=None, batch_size=10):
    """
    Process the book and extract text using OCR
    
    Args:
        pdf_path: Path to the PDF file
        output_path: Path to save the extracted JSON
        start_page: Starting page number (0-indexed)
        end_page: Ending page number (None for all pages)
        batch_size: Number of pages to process before saving
    """
    
    print(f"Processing: {pdf_path}")
    print(f"Output: {output_path}")
    print(f"Pages: {start_page} to {end_page or 'end'}")
    print("=" * 60)
    
    # Open PDF
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    
    if end_page is None:
        end_page = total_pages
    
    print(f"Total pages in PDF: {total_pages}")
    
    # Load existing progress if any
    extracted_data = {
        "metadata": {
            "title": "Brihat Jataka",
            "author": "V. Subrahmanya Sastri",
            "total_pages": total_pages
        },
        "pages": []
    }
    
    if os.path.exists(output_path):
        try:
            with open(output_path, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
                extracted_data["pages"] = existing_data.get("pages", [])
                print(f"Loaded {len(extracted_data['pages'])} previously extracted pages")
        except Exception as e:
            print(f"Could not load existing data: {e}")
    
    # Process pages
    processed_count = len(extracted_data["pages"])
    
    for page_num in range(start_page, min(end_page, total_pages)):
        # Check if already processed
        if any(p["page_number"] == page_num + 1 for p in extracted_data["pages"]):
            print(f"Page {page_num + 1} already processed, skipping...")
            continue
        
        try:
            print(f"\nProcessing page {page_num + 1}/{total_pages}...")
            
            # Extract page as image
            img = extract_page_as_image(doc, page_num)
            
            # Perform OCR
            text = ocr_page(img)
            
            # Store result
            page_data = {
                "page_number": page_num + 1,
                "text": text,
                "char_count": len(text)
            }
            
            extracted_data["pages"].append(page_data)
            processed_count += 1
            
            print(f"  ✓ Extracted {len(text)} characters")
            
            # Save progress periodically
            if processed_count % batch_size == 0:
                print(f"\n  Saving progress ({processed_count} pages processed)...")
                with open(output_path, 'w', encoding='utf-8') as f:
                    json.dump(extracted_data, f, ensure_ascii=False, indent=2)
                
        except Exception as e:
            print(f"  ✗ Error on page {page_num + 1}: {e}")
            continue
    
    # Final save
    print(f"\n{'='*60}")
    print(f"Processing complete!")
    print(f"Total pages processed: {processed_count}")
    print(f"Saving to: {output_path}")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(extracted_data, f, ensure_ascii=False, indent=2)
    
    doc.close()
    
    return extracted_data

def extract_key_content(output_path):
    """Extract key astrological content from OCR output"""
    
    with open(output_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print("\n" + "="*60)
    print("EXTRACTING KEY CONTENT")
    print("="*60)
    
    key_sections = {
        "planetary_combinations": [],
        "yogas": [],
        "dasha_rules": [],
        "house_interpretations": [],
        "predictions": []
    }
    
    for page in data["pages"]:
        text = page["text"].lower()
        page_num = page["page_number"]
        
        # Look for key sections
        if any(word in text for word in ["yoga", "combination", "raj yoga"]):
            key_sections["yogas"].append({
                "page": page_num,
                "preview": page["text"][:200]
            })
        
        if any(word in text for word in ["dasha", "major period", "sub-period"]):
            key_sections["dasha_rules"].append({
                "page": page_num,
                "preview": page["text"][:200]
            })
        
        if any(word in text for word in ["house", "bhava", "ascendant"]):
            key_sections["house_interpretations"].append({
                "page": page_num,
                "preview": page["text"][:200]
            })
    
    # Save key sections
    key_output = output_path.replace('.json', '-key-content.json')
    with open(key_output, 'w', encoding='utf-8') as f:
        json.dump(key_sections, f, ensure_ascii=False, indent=2)
    
    print(f"Key content extracted and saved to: {key_output}")
    
    return key_sections

def main():
    pdf_path = "../books/Brihat Jataka 2nd Ed. by V Subrahmanya Sastri.pdf"
    output_path = "extracted-books/brihat-jataka-ocr.json"
    
    # Check tesseract
    if not check_tesseract():
        print("\n" + "="*60)
        print("ERROR: Tesseract is not installed!")
        print("="*60)
        print("\nPlease install Tesseract OCR:")
        print("  brew install tesseract")
        print("\nOr wait for the installation to complete if already in progress.")
        print("\nThen run this script again.")
        sys.exit(1)
    
    # Create output directory
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Process command line arguments
    start_page = 0
    end_page = None
    
    if len(sys.argv) > 1:
        start_page = int(sys.argv[1]) - 1  # Convert to 0-indexed
    if len(sys.argv) > 2:
        end_page = int(sys.argv[2])
    
    # Process book
    data = process_book(pdf_path, output_path, start_page, end_page)
    
    # Extract key content
    key_content = extract_key_content(output_path)
    
    print("\n" + "="*60)
    print("OCR EXTRACTION COMPLETE")
    print("="*60)
    print(f"\nOutput files:")
    print(f"  - {output_path}")
    print(f"  - {output_path.replace('.json', '-key-content.json')}")

if __name__ == "__main__":
    main()
