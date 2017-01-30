#!/usr/bin/python

### NCBI NIH Hackathon
### quantify co-occurence of gene pairs from Gene (www.ncbi.nlm.nih.gov/gene), for hypergeom calculations based on pid
### input gene - pid data file can be downloaded from ftp://ftp.ncbi.nlm.nih.gov/gene/DATA/gene2pubmed.gz
### author: felixfrancier@gmail.com


############################################################
#Time to run the code: start timer
############################################################
import time
t0 = time.time()


############################################################
#### IMPORT PYTHON FUNCTIONS
############################################################
import pandas as pd
import re
from scipy.stats import hypergeom
import itertools
import re
from scipy.stats import hypergeom


############################################################
#### INPUT FILES, PARAMETERS
############################################################
input_file = "gene2pubmed"
#input_file = "test_genes2pubmed"
out_put_file = "output_10090_100perpmid.txt"
sel_tax_id = 10090      ### mouse
no_genes_per_pmid = 100

############################################################
#### FUNCTIONS
############################################################




############################################################
#### CODE
############################################################


### pid genes dictionary and list PubMed_ID as key
pid_genes_dict  = {}        ### dictionary of pid and corresponding genes
gene_count_dict = {}        ### counts of individual genes in the whole data set
pid_count       = 0
with open (input_file, "r") as input_file2:
    lines       =   input_file2.readlines()
    for line in lines:
        if str(sel_tax_id) in line:
            line        = line.rstrip('\r\n').split('\t')
            tax_id, GeneID, PubMed_ID = int(line[0]), int(line[1]), line[2]
            if tax_id == sel_tax_id:
                if PubMed_ID in pid_genes_dict:
                    pid_genes_dict[PubMed_ID].append(int(GeneID))
                else:
                    pid_genes_dict[PubMed_ID] = [GeneID]
                    pid_count += 1
                if GeneID not in gene_count_dict:
                    gene_count_dict[GeneID] = 1
                else:
                    gene_count_dict[GeneID] = gene_count_dict[GeneID] + 1
#print gene_count_dict
#print pid_count



### get gene pairs from each pid data
gene_pairs = []
for PubMed_ID, GeneID in pid_genes_dict.iteritems():
    if len(GeneID) == 2:
        GeneID = sorted(GeneID)
        gene_pairs.append(GeneID)
    #elif len(GeneID) > 1:                                      ### no max genes per pmid filter
    elif len(GeneID) > 1 and len(GeneID) <=no_genes_per_pmid:
        GeneID = sorted(GeneID)
        #print GeneID, "****"
        for i in xrange(len(GeneID)-1):
            for j in xrange(len(GeneID)-(i+1)):
                #print ([GeneID[i], GeneID[i+j+1]])
                gene_pairs.append([GeneID[i], GeneID[i+j+1]])
    
    

### count gene and gene pairs
gene_pairs.sort()
unique_gene_pairs = list(gene_pairs for gene_pairs,_ in itertools.groupby(gene_pairs))      ### get unique items in a list of list
#n = len(unique_gene_pairs)

with open(out_put_file, "w") as text_file:
    text_file.write("GeneA" + "\t" + "GeneA#" + "\t" + "GeneB" + "\t" + "GeneB#" + "\t" + "GeneAB#" + "\t" + "p-value" "\n")

    for gene_pair in unique_gene_pairs:
        gene_pair_counts = gene_pairs.count(gene_pair)
        geneA, geneB = gene_pair[0], gene_pair[1]
        geneA_count = gene_count_dict[gene_pair[0]]
        geneB_count = gene_count_dict[gene_pair[1]]
        hypergeometric_value = hypergeom.cdf(int(gene_pair_counts), pid_count, int(geneA_count), int(geneB_count))
        text_file.write(str(geneA) + "\t" + str(geneA_count) + "\t" + str(geneB) + "\t" + str(geneB_count) + "\t" + str(gene_pair_counts) + "\t" + str(hypergeometric_value) + "\n")

    
    





############################################################
#Time to run the code: end timer
############################################################
t1 = time.time()
total = t1-t0
total = ("{0:.2f}".format(round(total,2)))
print "total run time = ", str(total), "seconds"
