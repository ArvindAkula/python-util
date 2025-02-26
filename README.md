# Python Utilities

A collection of useful Python utilities for various tasks.

## PDF Merger

A simple utility to merge multiple PDF files into a single PDF document.

### Installation

1. Clone this repository:
```
git clone https://github.com/yourusername/python-util.git
cd python-util
```

2. Install required dependencies:
```
pip install PyPDF2
```

### Usage

Basic usage:
```
python pdf_merger.py file1.pdf file2.pdf file3.pdf -o output.pdf
```

Arguments:
- Input files: List of PDF files to merge (required)
- `-o, --output`: Output filename (default: merged.pdf)

### Example

```
python pdf_merger.py document1.pdf document2.pdf -o combined.pdf
```

## Requirements

- Python 3.6+
- PyPDF2