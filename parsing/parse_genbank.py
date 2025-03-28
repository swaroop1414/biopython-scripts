from Bio import SeqIO
import sys 

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = input("Please enter the GenBank file name: ")

try:
    with open(filename,"r") as file:
        for record in SeqIO.parse(file,"genbank"):
            print(f"ID: {record.id}")
            print(f"Description: {record.description}")
            print(f"Length: {len(record.seq)}")
            print("-"*50)
        
            # Loop through features and filter only CDS (Coding Sequences)
            for feature in record.features:
                if feature.type == "CDS":
                    print(f"Location: {feature.location}")
                    print(f"Strand: {feature.strand}")
                    print(f"Gene: {feature.qualifiers.get('gene',['N/A'])[0]}")
                    print(f"Product: {feature.qualifiers.get('product',['N/A'])[0]}")
                    print(f"Translation: {feature.qualifiers.get('translation',['N/A'])[0]}")
                    print("-"*50)

except FileNotFoundError:
    print(f"Error: The file {filename} was not found.")
except ValueError as e:
    print(f"Error: {e}. Please check the file format. Excepted 'genbank' format.")
except Exception as e:
    print(f"An error occured: {e}")
