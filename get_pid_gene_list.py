#!/usr/bin/python

### NCBI NIH Hackathon
### parse PubTator to get a list of gene ids corresponing to each pubmed id
### author: felixfrancier@gmail.com

import pandas as pd
import re
import string

input_file = "test_file"



p_id_genes_dict = {}
abstractsdict={}
with open (input_file, "r") as input_file:
    lines       =   input_file.readlines()
    for line in lines:
        if "Gene" in line:
            line = line.strip('\n')
            line = line.replace("(Tax:", '\t')
            line = re.split(r'\t+', line)
            print line

            p_id, gene = (line[0]), (line[5])
            print p_id, gene
            
            if p_id in p_id_genes_dict:
                p_id_genes_dict[p_id].append(gene)
            else:
                p_id_genes_dict[p_id] = [gene]
        elif "|a|" in i:
            if "|a|\n" in i:
                words=word_tokenize(str(i))
                
                pubmedid=words[0].split("|")[0]
                abstractsdict[pubmedid]="None"
            else:
                
                words=word_tokenize(str(i))
                pubmedid=words[0].split("|")[0]
                words[0]="".join(words[0].split("|")[2:])
                #print words
                abstractsdict[pubmedid]=words
print p_id_genes_dict
print abstractsdict




