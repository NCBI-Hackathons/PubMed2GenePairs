#!/usr/bin/python
### NCBI Hackathon
### quantify co-occurence of genes and gene pairs from pubtator data; and compute hypergeometric cdf.
### gene pairs are calculated per pubmed_id. duplicate and reversed gene pairs are removed.
### author: Felix Francis (email: felixfrancier@gmail.com)


### Import functions
import re
from scipy.stats import hypergeom




### Input parameters
#input_file = "/home/ubuntu/kodalivk/10m.bioconcepts2pubtator_offsets"
#input_file = "/home/ubuntu/kodalivk/24m.bioconcepts2pubtator_offsets"
input_file = "/home/ubuntu/kodalivk/10k.bioconcepts2pubtator_offsets"
out_put_file = "final_output_10k_v2_011616.txt"


min_pid = 1
max_pid = 2500000000



### create pid dictionary and list with 'pid' as key
def gen_pid_dictionary(input_file):
    pid_genes_dict = {}
    genes_list = []
    with open (input_file, "r") as input_file2:
        lines       =   input_file2.readlines()
        for line in lines:
            if "Gene" in line and ("|a|" or "|t|") not in line :
                line = line.strip('\n')
                line = line.replace("(Tax:", '\t')
                line = re.split(r'\t+', line)
                if len(line) > 4:
                    p_id, gene = (line[0]), (line[3])
                    if int(p_id)>=min_pid and int(p_id)<=max_pid:
                        
                        genes_list.append(gene)
                    if p_id in pid_genes_dict:
                        if gene not in pid_genes_dict[p_id]:
                            pid_genes_dict[p_id].append(gene)
                    else:
                        pid_genes_dict[p_id] = [gene]
    genes_list = list(set(genes_list))
    return (genes_list, pid_genes_dict)



gen_pid_dictionary_output = gen_pid_dictionary(input_file)




### compute gene pairs for a given pubmed id
def gene_pairs_per_pid(input_file, gen_pid_dictionary_output):
    gene_pairs = []
    gene_count_dict = {}
    genes_list, pid_genes_dict = gen_pid_dictionary_output[0], gen_pid_dictionary_output[1]
    for pid, genes in pid_genes_dict.iteritems():
        #print pid, genes
        for i in xrange(len(genes)-1):
            for j in xrange(len(genes)-(i+1)):
                gene_pair_sublist = sorted([genes[i], genes[i+j+1]])
                gene_pairs.append(gene_pair_sublist)
        for gene in genes:
            if gene in gene_count_dict:
                gene_count_dict[gene] = gene_count_dict[gene] + 1
            else:
                gene_count_dict[gene] = 1
    gene_pairs = [list(x) for x in set(tuple(x) for x in gene_pairs)]
    return gene_pairs

gene_pairs = gene_pairs_per_pid(input_file, gen_pid_dictionary_output)



### create genes dictionary and list 'gene' as key
pid_genes_dict = {}
genes_list = []
with open (input_file, "r") as input_file2:
    lines       =   input_file2.readlines()
    for line in lines:
        if "Gene" in line and ("|a|" or "|t|") not in line :
            line = line.strip('\n')
            line = line.replace("(Tax:", '\t')
            line = re.split(r'\t+', line)
            if len(line) > 4:
                p_id, gene = str(line[0]), str(line[3])
                if int(p_id)>=min_pid and int(p_id)<=max_pid:
                    genes_list.append(gene)
                if gene in pid_genes_dict:
                    pid_genes_dict[gene].append(int(p_id))
                else:
                    pid_genes_dict[gene] = [p_id]
genes_list = list(set(genes_list))



total_no_genes = len(genes_list)

hypergeom_list = []

with open(out_put_file, "w") as text_file:
    text_file.write("GeneA" + "\t" + "GeneA#" + "\t" + "GeneB" + "\t" + "GeneB#" + "\t" + "GeneAB" + "\t" + "GeneAB#" + "\t" + "p-value" "\n")
    for gene_pair in gene_pairs:
        GeneA, GeneB = str(gene_pair[0]), str(gene_pair[1])
        GeneA_list, GeneB_list = (pid_genes_dict[gene_pair[0]]), (pid_genes_dict[gene_pair[1]])
        no_GeneA, no_GeneB = len(GeneA_list), len(GeneB_list)
        #print pid_genes_dict[gene_pair[0]], pid_genes_dict[gene_pair[1]]
        GeneA_B = str(gene_pair[0])+ "_" + str(gene_pair[1])
        GeneA_B_list = (list(set(pid_genes_dict[gene_pair[0]]).intersection(set(pid_genes_dict[gene_pair[1]]))))
        no_GeneA_B = len(set(GeneA_B_list))
        #hypergeometric_value = hypergeom.cdf(2, int(no_GeneA), int(no_GeneB), int(no_GeneA_B)) 
        #hypergeom_list.append(hypergeometric_value)
        #text_file.write(GeneA + "\t" + str(no_GeneA) + "\t" + GeneB + "\t" + str(no_GeneB) + "\t" + GeneA_B + "\t" + str(no_GeneA_B) + "\t" + str(hypergeometric_value) + "\n")












'''
with open(out_put_file, "w") as text_file:
    text_file.write("GeneA" + "\t" + "GeneA#" + "\t" + "GeneB" + "\t" + "GeneB#" + "\t" + "GeneAB" + "\t" + "GeneAB#" + "\n")
    for gene_pair in gene_pairs:
        GeneA, GeneB = str(gene_pair[0]), str(gene_pair[1])
        GeneA_list, GeneB_list = (pid_genes_dict[gene_pair[0]]), (pid_genes_dict[gene_pair[1]])
        no_GeneA, no_GeneB = len(GeneA_list), len(GeneB_list)
        GeneA_B = str(gene_pair[0])+ "_" + str(gene_pair[1])
        GeneA_B_list = (list(set(pid_genes_dict[gene_pair[0]]).intersection(set(pid_genes_dict[gene_pair[1]]))))
        no_GeneA_B = len(set(GeneA_B_list))
        text_file.write(GeneA + "\t" + str(no_GeneA) + "\t" + GeneB + "\t" + str(no_GeneA) + "\t" + GeneA_B + "\t" + str(no_GeneA_B) + "\n")

'''

'''

### create pid dictionary and list with 'pid' as key
def gen_pid_dictionary(input_file):
    pid_genes_dict = {}
    genes_list = []
    with open (input_file, "r") as input_file2:
        lines       =   input_file2.readlines()
        for line in lines:
            if "Gene" in line and ("|a|" or "|t|") not in line :
                line = line.strip('\n')
                line = line.replace("(Tax:", '\t')
                line = re.split(r'\t+', line)
                if len(line) > 4:
                    p_id, gene = (line[0]), (line[3])
                    if int(p_id)>=min_pid and int(p_id)<=max_pid:
                        
                        genes_list.append(gene)
                    if p_id in pid_genes_dict:
                        if gene not in pid_genes_dict[p_id]:
                            pid_genes_dict[p_id].append(gene)
                    else:
                        pid_genes_dict[p_id] = [gene]
    genes_list = list(set(genes_list))




### compute gene pairs for a given pubmed id
def gene_pairs_per_pid(input_file):
    gene_pairs = []
    gene_count_dict = {}
    for pid, genes in pid_genes_dict.iteritems():
        #print pid, genes
        for i in xrange(len(genes)-1):
            for j in xrange(len(genes)-(i+1)):
                gene_pairs.append([genes[i], genes[i+j+1]])
        for gene in genes:
            if gene in gene_count_dict:
                gene_count_dict[gene] = gene_count_dict[gene] + 1
            else:
                gene_count_dict[gene] = 1


### create genes dictionary and list 'gene' as key
def gen_genes_dictionary(input_file):
    pid_genes_dict = {}
    genes_list = []
    with open (input_file, "r") as input_file2:
        lines       =   input_file2.readlines()
        for line in lines:
            if "Gene" in line and ("|a|" or "|t|") not in line :
                line = line.strip('\n')
                line = line.replace("(Tax:", '\t')
                line = re.split(r'\t+', line)
                if len(line) > 4:
                    p_id, gene = str(line[0]), str(line[3])
                    if int(p_id)>=min_pid and int(p_id)<=max_pid:
                        genes_list.append(gene)
                    if gene in pid_genes_dict:
                        pid_genes_dict[gene].append(int(p_id))
                    else:
                        pid_genes_dict[gene] = [p_id]
    genes_list = list(set(genes_list))


def write_out_put(out_put_file):
    with open(out_put_file, "w") as text_file:
        text_file.write("GeneA" + "\t" + "GeneA#" + "\t" + "GeneB" + "\t" + "GeneB#" + "\t" + "GeneAB" + "\t" + "GeneAB#" + "\n")
        for gene_pair in gene_pairs:
            GeneA, GeneB = str(gene_pair[0]), str(gene_pair[1])
            GeneA_list, GeneB_list = (pid_genes_dict[gene_pair[0]]), (pid_genes_dict[gene_pair[1]])
            no_GeneA, no_GeneB = len(GeneA_list), len(GeneB_list)
            GeneA_B = str(gene_pair[0])+ "_" + str(gene_pair[1])
            GeneA_B_list = (list(set(pid_genes_dict[gene_pair[0]]).intersection(set(pid_genes_dict[gene_pair[1]]))))
            no_GeneA_B = len(set(GeneA_B_list))
            text_file.write(GeneA + "\t" + str(no_GeneA) + "\t" + GeneB + "\t" + str(no_GeneA) + "\t" + GeneA_B + "\t" + str(no_GeneA_B) + "\n")



'''