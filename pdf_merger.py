#!/usr/bin/env python3
"""
PDF Merger Utility

This script provides functionality to merge multiple PDF files into a single PDF document.
"""

import os
import argparse
from PyPDF2 import PdfMerger


def merge_pdfs(input_files, output_file):
    """
    Merge multiple PDF files into one PDF.
    
    Args:
        input_files (list): List of paths to PDF files to merge
        output_file (str): Path to save the merged PDF
    
    Returns:
        bool: True if successful, False otherwise
    """
    if not input_files:
        print("Error: No input files provided")
        return False
    
    # Validate input files
    for file_path in input_files:
        if not os.path.exists(file_path):
            print(f"Error: File not found: {file_path}")
            return False
        if not file_path.lower().endswith('.pdf'):
            print(f"Error: File is not a PDF: {file_path}")
            return False
    
    try:
        merger = PdfMerger()
        
        # Add each PDF to the merger
        for pdf in input_files:
            print(f"Adding: {pdf}")
            merger.append(pdf)
        
        # Write the merged PDF to output file
        print(f"Creating merged PDF: {output_file}")
        merger.write(output_file)
        merger.close()
        print("PDF merge completed successfully!")
        return True
    
    except Exception as e:
        print(f"Error merging PDFs: {str(e)}")
        return False


def main():
    """Main function to handle command line arguments and execute the PDF merge."""
    parser = argparse.ArgumentParser(description='Merge multiple PDF files into one PDF.')
    parser.add_argument('input_files', nargs='+', help='Input PDF files to merge')
    parser.add_argument('-o', '--output', default='merged.pdf',
                      help='Output file name (default: merged.pdf)')
    
    args = parser.parse_args()
    merge_pdfs(args.input_files, args.output)


if __name__ == "__main__":
    main()