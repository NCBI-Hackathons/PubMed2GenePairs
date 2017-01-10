#import pandas as pd
import re
#import string

#input_file = "test_file"
#out_put_file = "24_25million.txt"


min_pid = 100
max_pid = 100027
class PubTatorReader(object):
    def __init__(self,filename):
        self.filename=filename
    def read_abstracts(self):
        abstract_dictionary={}
        
        input_file=self.filename
        with open (input_file, "r") as input_file1:
            lines       =   input_file1.xreadlines()
            for line in lines:
                line = line.strip('\n')
            if "|a|" in line and line[-3:] != "|a|":
                line = line.split('|a|')
                #abstract = line[1].split(". ")
                abstract = line[1]
                pid = line[0]
                if int(pid)>=min_pid and int(pid)<=max_pid:
                    abstract_dictionary[pid] = abstract
        yield abstract_dictionary
    def read_genes(self):
        #genes_dict = {}
        input_file=self.filename
        pid_genes_dict={}
        with open (input_file, "r") as input_file2:
            lines       =   input_file2.xreadlines()
            #genelist=[]
            for line in lines:
                if "Gene" in line and ("|a|" or "|t|") not in line :
                    line = line.strip('\n')
                    line = line.replace("(Tax:", '\t')
                    line = re.split(r'\t+', line)
                    genelist=[]
                    if len(line)>4:
                        p_id, gene = (line[0]), (line[3])
                        if p_id in pid_genes_dict.keys():
                            existing_genes=pid_genes_dict[p_id]
                            if len(existing_genes)<1:
                                pid_genes_dict[p_id]=pid_genes_dict[p_id],gene
                            else:
                                pid_genes_dict[p_id]=pid_genes_dict[p_id],gene
                        else:
                            pid_genes_dict[p_id]=gene

                            
                        #gene_list.append(line[3])
                        #pid_genes_dict[p_id]=genelist
                        
        return pid_genes_dict

    def get_common_gene_pairs(self):
        #this is not complete
        sample_genes1=self.read_genes()
        for k,v in sample_genes1.items():
            listofpairs=[]
            for i in itertools.combinations(v,2):
                listofpairs.append(i)
                genedict[k]=listofpairs
        return genedict
