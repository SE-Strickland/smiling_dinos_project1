# Smiling Dinos Project 1

Project 1 for BSC6451 Computational Tools Class - Fall 2024

This repository contains a script that allows you to use data from the NCBI GenBank.

In this sense, the following script allows you to use files in FASTA format that contain the database of genetic sequences of a particular species and return the following results:

- Length of the genetic base sequence: species_length.py
- Projection of scatter plots, treeMap, and dendrograms: Plot_genes.py
- An alert message in cases where the data sequence contains null information (N): uncall_bp_warn.py
- Finding of opening reading frame: orf_detection.py

The team members are:

- Mayu Katafuchi
- Bharti Parihar
- Fabian Romero
- Sarah Ellen Strickland

## Prior to running scripts
To run any of the scripts, you must install biopython from the terminal, using the command:

"pip install biopython"

To tun the plot_genes.py script need to install: biopython, matplotlib, seaborn, pandas, and squarify using the commands:

"pip install biopython matplotlib seaborn pandas squarify".
