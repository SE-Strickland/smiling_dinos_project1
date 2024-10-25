# Function to read a multi-sequence FASTA file and store each sequence with its header
def read_multi_fasta(file_path):
    """
    Function to read a FASTA file with multiple sequences and return a dictionary with
    headers as keys and sequences as values.
    :param file_path: Path to the FASTA file
    :return: A dictionary with headers as keys and nucleotide sequences as values
    """
    sequences = {}
    current_header = None
    current_sequence = []
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                # Save the previous sequence if there is one
                if current_header:
                    sequences[current_header] = ''.join(current_sequence)
                
                # Start a new sequence
                current_header = line[1:]  # Exclude the ">" character
                current_sequence = []
            else:
                # Add line to the current sequence
                current_sequence.append(line)
        
        # Save the last sequence after loop ends
        if current_header:
            sequences[current_header] = ''.join(current_sequence)
    
    return sequences

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

# Main part of the script to process multi-species FASTA
if __name__ == "__main__":
    # Specify the path to your FASTA file
    fasta_file_path = 'Project_1_matK_Taraxacum.fasta'
    
    # Read all sequences from the multi-sequence FASTA file
    sequences = read_multi_fasta(fasta_file_path)
    
    # Loop through each species' sequence and find ORFs
    for species_name, sequence in sequences.items():
        # Find ORFs in the sequence (minimum length of 100 nucleotides)
        orfs = find_orfs(sequence, min_length=100)
        
        # Display the species name and the identified ORFs
        print(f"Species: {species_name}")
        if orfs:
            print("Open Reading Frames (ORFs) found:")
            for start, end in orfs:
                print(f"  ORF starts at {start}, ends at {end}")
        else:
            print("  No ORFs found")
        print("-" * 50)
