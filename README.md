# Biopython Scripts  
A collection of Biopython scripts for practicing sequence analysis, parsing biological file formats (FASTA, GenBank, etc.), and exploring genomic data.  

## Features  
 Parses **GenBank** files to extract gene metadata and CDS details (location, strand, product, translation).  
 Parses **FASTA** files to display sequence information with a length check (truncating long sequences).  
 Handles user input for file selection and provides error handling for invalid or empty files.  

## Scripts Included  
 **GenBank Parser** – Extracts gene ID, description, sequence length, and CDS details.  
 **FASTA Parser** – Reads FASTA files, prints sequence metadata, and limits sequence display to 50 characters.  

## Usage  
Run a script with a file name as an argument or enter it manually:  
```bash
python genbank_parser.py example.gb  
python fasta_parser.py example.fasta  
