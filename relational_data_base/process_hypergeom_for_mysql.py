#!/usr/bin/python

### NCBI NIH Hackathon
### convert module 1 output for mysql database.
### output1: unique list of genes with incremental numbering
### output2: module1 output with gene names converted to numbers
### author: felixfrancier@gmail.com

import pandas as pd
import re
import numpy as np


#input_file = "sample_output_web_interface.txt"
input_file = "../final_output_10m_011116.txt"

out_put_file1 = "gene_numbering_011116.txt"
out_put_file2 = "whole_output_with_numbering_011116.txt"
df = pd.read_csv(input_file, sep='\t')


#print df
GeneA_col = df['GeneA'].tolist()
GeneB_col = df['GeneB'].tolist()
combined_list_genes = list(set(GeneA_col + GeneB_col))
n =  int(len(combined_list_genes)+1)
number_list = range(1, n)



df_gene_names = pd.DataFrame(combined_list_genes, columns=['Gene_name'])

df_gene_names['Gene_number'] = number_list

### print output1 genenames and gene number
df_gene_names.to_csv(out_put_file1, header=None, index=None, sep='\t', mode='a')

df_gene_names_A = df_gene_names.rename(columns={ 'Gene_name' : 'GeneA', 'Gene_number' : 'GeneA_number'})

dfA = pd.merge(df, df_gene_names_A, on='GeneA', how='inner')

df_gene_names_B = df_gene_names.rename(columns={ 'Gene_name' : 'GeneB', 'Gene_number' : 'GeneB_number'})

#print df_gene_names_B
#
dfAB = pd.merge(dfA, df_gene_names_B, on='GeneB', how='inner')


### select only gene identifier and p_value.
dfAB_subset = dfAB[['GeneA_number', 'GeneB_number', 'p_value']]

dfAB_subset.index += 1 



### print output2 module1 output with gene names converted to numbers
#dfAB.to_csv(out_put_file2, header=None, index=None, sep='\t', mode='a')
dfAB_subset.to_csv(out_put_file2, header=None, index=True, sep='\t', mode='a')








