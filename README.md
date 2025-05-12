# Autism Gene Checker (Biopython + NCBI)

This is a very simple Python project that checks if a gene is associated with autism — using real gene summaries from NCBI.

## What you need
- Python 3 installed
- Biopython installed (see below)
- Internet connection (to contact NCBI)

## What it does
You type in a gene name (like MECP2 or SHANK3), and the script:
1. Searches the NCBI Gene database
2. Shows you the official summary of the gene
3. Tells you if the word "autism" is found in that summary

## How to run it
1. Save the code to a file called `autism_gene_checker.py`
2. Open a terminal (Command Prompt on Windows, or just double-click if configured)
3. Type:
```sh
python autism_gene_checker.py
