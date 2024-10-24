# Function to read a FASTA file and extract the nucleotide sequence
def read_fasta(file_path):
    """
    Function to read a FASTA file and return the nucleotide sequence as a string.
    :param file_path: Path to the FASTA file
    :return: The nucleotide sequence as a string
    """
    sequence = ''
    with open(file_path, 'r') as file:
        for line in file:
            if not line.startswith('>'):
                sequence += line.strip()
    return sequence

# Function to find open reading frames (ORFs) in a nucleotide sequence
def find_orfs(fasta_sequence, min_length=100):
    """
    Function to find open reading frames (ORFs) in a nucleotide sequence.
    :param fasta_sequence: A string representing the nucleotide sequence from the FASTA file
    :param min_length: Minimum length of the ORF to consider (default is 100 nucleotides)
    :return: A list of tuples containing (start, end) positions of each ORF
    """
    sequence = fasta_sequence.upper()
    orfs = []
    
    # Search for start codon (ATG) and stop codons (TAA, TAG, TGA)
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        if codon == "ATG":  # Start codon
            for j in range(i + 3, len(sequence) - 2, 3):
                stop_codon = sequence[j:j+3]
                if stop_codon in ["TAA", "TAG", "TGA"]:  # Stop codon
                    orf_length = j + 3 - i
                    if orf_length >= min_length:
                        orfs.append((i+1, j+3))  # Convert to 1-based indexing
                    break
    
    return orfs

# Example usage of the script:
if __name__ == "__main__":
    # Specify the path to your FASTA file
    fasta_file_path = 'Project_1_matK_Taraxacum.fasta'
    
    # Read the sequence from the FASTA file
    sequence = read_fasta(fasta_file_path)
    
    # Find ORFs in the sequence (minimum length of 100 nucleotides)
    orfs = find_orfs(sequence, min_length=100)
    
    # Display the identified ORFs (start and end positions)
    print("Open Reading Frames (ORFs) found:")
    for start, end in orfs:
        print(f"ORF starts at {start}, ends at {end}")
