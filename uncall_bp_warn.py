#Install biopython, if not already installed use "!pip install biopython" command at start


# Put path to your fasta file

fasta_file = "Project_1_matK_Taraxacum.fasta"

    

from Bio import SeqIO



open("spec_ids_for_uncalled_bps.txt", "a")



#Opening fasta file and parsing header/sample ID

with open(fasta_file, "r") as fasta_file:

    for record in SeqIO.parse(fasta_file, "fasta"):

        header = record.description

        species_name = ' '.join(header.split()[1:3]) 

        sequence = str(record.seq)

       

        #Print information for each attribute, providing a warning if uncalled nucleotides

        print(f"ID: {record.id}")

        print(f"Species: {species_name}")

    

        if "N" in record.seq:

            print(f"Warning: Uncalled base pairs in this sequence!")

            print(f"Sequence: {sequence}")

            print("----------------------------------------------")

            with open("spec_ids_for_uncalled_bps.txt", "a") as file:

                file.write(f"Warning: Uncalled base pairs in: sample ID {record.id} from species {species_name}.\n")

            

        else:

            print(f"Sequence: {sequence}")

            print("----------------------------------------------")



            
