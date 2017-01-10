#!/usr/bin/python

### NCBI NIH Hackathon
### quantify co-occurence of gene pairs for hypergeom calculations based on pid
### author: felixfrancier@gmail.com

#import pandas as pd
import re
#import string
    
#input_file = "test_file"

#input_file = "/home/ubuntu/kodalivk/24m.bioconcepts2pubtator_offsets"
input_file = "/home/ubuntu/kodalivk/10k.bioconcepts2pubtator_offsets"
out_put_file = "output_test_011016.txt"
#out_put_file = "24_25million.txt"


#min_pid = 24000000
#max_pid = 25000000


min_pid = 1
max_pid = 25000000000




### genes dictionary and list ### pid as key
pid_genes_dict = {}
genes_list = []
with open (input_file, "r") as input_file2:
    lines       =   input_file2.readlines()
    for line in lines:
        if "Gene" in line and ("|a|" or "|t|") not in line :
            line = line.strip('\n')
            line = line.replace("(Tax:", '\t')
            line = re.split(r'\t+', line)
            #p_id, gene = (line[0]), (line[5])
            if len(line) > 4:
                p_id, gene = (line[0]), (line[3])
                if int(p_id)>=min_pid and int(p_id)<=max_pid:
                    
                    genes_list.append(gene)
                if p_id in pid_genes_dict:
                    pid_genes_dict[p_id].append(gene)
                else:
                    pid_genes_dict[p_id] = [gene]
genes_list = list(set(genes_list))
print pid_genes_dict










'''

### genes dictionary and list ### gene as key
pid_genes_dict = {}
genes_list = []
with open (input_file, "r") as input_file2:
    lines       =   input_file2.readlines()
    for line in lines:
        if "Gene" in line and ("|a|" or "|t|") not in line :
            line = line.strip('\n')
            line = line.replace("(Tax:", '\t')
            line = re.split(r'\t+', line)
            #p_id, gene = (line[0]), (line[5])
            if len(line) > 4:
                p_id, gene = str(line[0]), str(line[3])
                if int(p_id)>=min_pid and int(p_id)<=max_pid:
                    
                    genes_list.append(gene)
                if gene in pid_genes_dict:
                    pid_genes_dict[gene].append(int(p_id))
                else:
                    pid_genes_dict[gene] = [p_id]
genes_list = list(set(genes_list))
#print pid_genes_dict






### get list of genes from dictionary:
genes_set = list(set(pid_genes_dict.keys()))
#print genes_set


### get gene pairs
gene_pairs = []
for i in xrange(len(genes_set)-1):
    for j in xrange(len(genes_set)-(i+1)):
        #print genes_list[i], genes_list[i+j+1]
        gene_pairs.append([genes_set[i], genes_set[i+j+1]])
#print gene_pairs


with open(out_put_file, "w") as text_file:
    text_file.write("GeneA" + "\t" + "GeneA#" + "\t" + "GeneB" + "\t" + "GeneB#" + "\t" + "GeneAB" + "\t" + "GeneAB#" + "\n")

    counter = 0
    ### get pid counts
    for gene_pair in gene_pairs:
        GeneA, GeneB = str(gene_pair[0]), str(gene_pair[1])
        GeneA_list, GeneB_list = (pid_genes_dict[gene_pair[0]]), (pid_genes_dict[gene_pair[1]])
        no_GeneA, no_GeneB = len(GeneA_list), len(GeneB_list)
        #print pid_genes_dict[gene_pair[0]], pid_genes_dict[gene_pair[1]]
        GeneA_B = str(gene_pair[0])+ "_" + str(gene_pair[1])
        GeneA_B_list = (list(set(pid_genes_dict[gene_pair[0]]).intersection(set(pid_genes_dict[gene_pair[1]]))))
        print GeneA_B, "counter = ", counter
        counter = counter + 1
        
        no_GeneA_B = len(set(GeneA_B_list))
        text_file.write(GeneA + "\t" + str(no_GeneA) + "\t" + GeneB + "\t" + str(no_GeneA) + "\t" + GeneA_B + "\t" + str(no_GeneA_B) + "\n")
        #print GeneA
        #print pid_genes_dict[gene_pair[0]], pid_genes_dict[gene_pair[1]]
        #print GeneA, str(no_GeneA), GeneB, str(no_GeneB), GeneA_B, str(no_GeneA_B)
        
'''

