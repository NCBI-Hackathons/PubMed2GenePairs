#!/usr/bin/python

### NCBI NIH Hackathon
### quantify co-occurence of gene pairs for hypergeom calculations based on pid
### author: felixfrancier@gmail.com

#import pandas as pd
import re
from scipy.stats import hypergeom

#input_file = "output_whole_dataset_based_011817.txt"
input_file = "test"
out_put_file = "output_whole_dataset_based_012917.txt"

no_pmid = 24000000


with open (input_file) as input_file2:
    with open(out_put_file, "w") as text_file:
        text_file.write("GeneA" + "\t" + "GeneA#" + "\t" + "GeneB" + "\t" + "GeneB#" + "\t" + "GeneAB" + "\t" + "GeneAB#" + "\t" + "p-value" "\n")

        next(input_file2)
        for line in input_file2:
            line = line.strip("\n")
            line = line.split("\t")
            #print line
            GeneA, GeneA_no, GeneB, GeneB_no, GeneAB, GeneAB_no = line[0], line[1], line[2], line[3], line[4], line[5]
            if int(GeneAB_no)>=1:
                #p_value = hypergeom.cdf(int(GeneAB_no), no_pmid, int(GeneA_no), int(GeneB_no)) 
                p_value = hypergeom.sf(int(GeneAB_no), no_pmid, int(GeneA_no), int(GeneB_no)) 
                #print GeneA, GeneA_no, GeneB, GeneB_no, GeneAB, GeneAB_no, p_value
                text_file.write(str(GeneA) + "\t" + str(GeneA_no) + "\t" + str(GeneB) + "\t" + str(GeneB_no) + "\t" + str(GeneAB) + "\t" + str(GeneAB_no) + "\t" + str(p_value) + "\n")

'''

with open(out_put_file, "w") as text_file:
    text_file.write("GeneA" + "\t" + "GeneA#" + "\t" + "GeneB" + "\t" + "GeneB#" + "\t" + "GeneAB" + "\t" + "GeneAB#" + "\t" + "p-value" "\n")

    counter = 0
    ### get pid counts
    for gene_pair in gene_pairs:
        GeneA, GeneB = str(gene_pair[0]), str(gene_pair[1])
        GeneA_list, GeneB_list = (pid_genes_dict[gene_pair[0]]), (pid_genes_dict[gene_pair[1]])
        no_GeneA, no_GeneB = len(GeneA_list), len(GeneB_list)
        #print pid_genes_dict[gene_pair[0]], pid_genes_dict[gene_pair[1]]
        GeneA_B = str(gene_pair[0])+ "_" + str(gene_pair[1])
        GeneA_B_list = (list(set(pid_genes_dict[gene_pair[0]]).intersection(set(pid_genes_dict[gene_pair[1]]))))
        #print GeneA_B, "counter = ", counter
        counter = counter + 1
        no_GeneA_B = len(set(GeneA_B_list))


        hypergeometric_value = hypergeom.cdf(2, int(no_GeneA), int(no_GeneB), int(no_GeneA_B)) 
        hypergeom_list.append(hypergeometric_value)


        text_file.write(GeneA + "\t" + str(no_GeneA) + "\t" + GeneB + "\t" + str(no_GeneB) + "\t" + GeneA_B + "\t" + str(no_GeneA_B) + "\t" + str(hypergeometric_value) + "\n")

'''














