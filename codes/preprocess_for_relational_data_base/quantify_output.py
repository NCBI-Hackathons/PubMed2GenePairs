#!/usr/bin/python

### NCBI NIH Hackathon
### quantify module 1 output for manuscript
### number of unique genes
### number of co-occurence
### co-occurence with <= 0.01 p_value
### author: felixfrancier@gmail.com

import pandas as pd
import re
import numpy as np




#input_file = "sample_output_web_interface.txt"
input_file = "../final_output_10m_011116.txt"

out_put_file1 = "gene_numbering.txt"
out_put_file2 = "whole_output_with_numbering.txt"
df = pd.read_csv(input_file, sep='\t')

#print df
GeneA_col = df['GeneA'].tolist()
GeneB_col = df['GeneB'].tolist()

combined_list_genes = list(set(GeneA_col + GeneB_col))

df = df[df.p_value <= 0.05]
#df = df[df.p_value <= 0.01]

p_val_col = df['p_value'].tolist()


print len(GeneA_col)
print len(combined_list_genes)

print "# gene pairs >= 0.05 p value = ", len(p_val_col)

