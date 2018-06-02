
# coding: utf-8

# In[16]:


from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import sys


# In[34]:


E_VALUE_THRESH = 0.04
with open("small-test.fasta", "r") as handle:
    with open ('result-blast.fasta','w') as out:
        with open('blast_search.xml', 'w') as file:
            records = SeqIO.parse(handle, "fasta")
            for i in records:
                result_handle = NCBIWWW.qblast("blastn", "nt", i.seq, format_type='XML', alignments = 1, descriptions = 1)
                #file.write(result_handle.read())
                blast_records = NCBIXML.parse(result_handle)
                blast_record = next(blast_records)
                for alignment in blast_record.alignments:
                    for hsp in alignment.hsps:
                        if hsp.expect < E_VALUE_THRESH:
                            title = alignment.title.split('|')
                            out.write('>'+title[4]+'\n'+str(i.seq)+'\n')
                            break
                    break

