PubRank - Text-driven identification and ranking of associated gene pairs in PubMed
================================================

The discovery of biological relationships between genes is one of the keys to understanding the complex functional nature encoded in genomes. Most of the knowledge describing gene relationships can be found in the vast amounts of the biomedical literature. Therefore, tools for automatic exploration of co-occurring gene names in PubMed coud be valuable in gaining knowledge about biological associations. Given a target gene many biological experiments identify a number of genes that change along with the target gene. Additionally, the changed genes could be functionally related to the target gene. Examining pairwise gene relationships manually could be a tedious process. To help with that, we propose a tool which identifies and ranks co-occurring genes in PubMed abstracts. 




![alt tag](https://github.com/NCBI-Hackathons/PubMed2GenePairs/blob/master/figures/pipeline_ffx.jpg)

Schematics representation of GenRank pipeline. Counts of individual genes and gene pairs are obtained for all the data pubmed id based data provided. Individual and paired occurrence information is used to calculate the cdf based p-value using hypergeometric test.


Running GenRank
================================================

Our algorithm, which we refer to as GenRank (Fig. 1), provides a list of ranked genes given a target gene. We use the hypergeometric distribution to identify gene pairs that co-occur significantly in the subset of PubMed articles as follows. Let Nt be the number of documents in Medline that contain the target gene, Ns be the size of the document set that contain a candidate related gene, N be the size of Medline, and Nst be the number of documents that contain both genes. The random variable Y representing a number of documents containing both genes is a hypergeometric random variable with parameters Ns, Nt and N (Larson 1982). The probability distribution of Y is shown as follows:

![alt tag](https://github.com/NCBI-Hackathons/PubMed2GenePairs/blob/master/figures/P_y.png| width=100)

![alt tag](https://github.com/NCBI-Hackathons/PubMed2GenePairs/blob/master/figures/p_value.png)