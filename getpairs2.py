filn="/Users/gbang/Documents/24m.sample.unique"
with open(gene_list1, 'r+') as f:
    #chunk=[]
    chunkdict=defaultdict(list)
    for line in f:
        try:
            thisline=line.split("\t")
            nextline=f.next().split("\t")
            chunkdict[thisline[0]].append(thisline[1].rstrip())
        except StopIteration:
            break
#print "dictread"
sample_genes1={"0002":["GENE1", "GENE2", "GENE3", "GENE4"],"0003":["GENE1", "GENE2", "GENE3", "GENE6"],"0202":["GENE4", "GENE2", "GENE1", "GENE7"]}
def get_common_gene_pairs(genelist):
    #genedict={}
    #for k,v in sample_genes1.items():
    #    listofpairs=[]
    #    for i in itertools.combinations(v,2):
    #        listofpairs.append(i)
    #        genedict[k]=listofpairs
    #return 
    return {k : list(itertools.combinations(v,2)) for k,v in genelist.iteritems()}

aaa=get_common_gene_pairs(chunkdict)
from collections import namedtuple,defaultdict
def get_gene_pair_pids(d):
    i=defaultdict(list)
    #d=get_common_gene_pairs(samplegenes1)
    Pub_genes=namedtuple("pair", ["gene1", "gene2"])
    for p_id,genepairs in d.iteritems():
        for p in genepairs:
            thispair=Pub_genes(p[0], p[1])
            if thispair in i.keys():
                i[thispair].append(p_id)
            else:
                i[thispair]=[p_id,]
        #print p_id
    return i

if __name__=="__main__":
    print get_gene_pair_pids(aaa)
