### Handmade Blast searcher

Receives fasta file, performs alignmnet with NCBI Blast database. Output is also fasta, but all records named with  
the species with the most similar alignmnet

Require:  
__SeqIO__ to handle with fasta  
__NCBIWWW__ to perform database search  
__NCBIXML__ to handle with search results

### How to use:
$ blast-searcher.py <your.fasta>
Output: file result-blast.fasta

