from Bio import SeqIO
import sys

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = input("Enter the file name: ")

try:
    with open(file_name,"r") as file:
        records = list(SeqIO.parse(file,"fasta"))

        if not records:
            print("Error: The file is empty or not in the correct fasta format")
            sys.exit(1)
        else:
            for record in records:
                print(f"ID: {record.id}")
                print(f"Description: {record.description}")
                print(f"Length: {len(record.seq)}")
                print(f"Sequence: {record.seq[:50]+'...' if len(record.seq) > 50 else record.seq}")
                print("-"*50)

except FileNotFoundError:
    print(f"Error: The file {file_name} was not found")
except  ValueError as e:
    print(f"Error: {e}. Please check if the file is in fasta format")
except Exception as e:
    print(f"An error occured: {e}")

