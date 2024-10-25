# If Biopython is not installed, install with "pip install biopython"

# Import fasta file
fasta_file = "Project_1_matK_Taraxacum.fasta"

# Import Biopython
from Bio import SeqIO

# Make a fuction named extract_species_and_length()
def extract_species_and_length(fasta_file, output_file):
    species_lengths = []

    # Use SeqIO.parse function in Biopython
    for record in SeqIO.parse(fasta_file, "fasta"):
        # Extract the species name 
        header = record.description
        
        # Extracts the second and third parts of the header
        species_name = ' '.join(header.split()[1:3])  

        # Calculate the length of the sequence
        gene_length = len(record.seq)

        # Store the result
        species_lengths.append((species_name, gene_length))

    # Save the results to a file
    with open(output_file, "w") as f:
        f.write("Species Name\tGene Length\n") 
        for species, length in species_lengths:
            f.write(f"{species}\t{length}\n")

# Write output file name
output_file = "species_lengths.txt" 

# Run the function
extract_species_and_length(fasta_file, output_file)

# Say it's done!
print(f"Output file name is {output_file}, it includes species name and bp length.")
print("You are a genius!!")
