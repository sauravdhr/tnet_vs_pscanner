

IMPORTANT WARNING: Sequences AI001_N204 and AI002_N224 are exactly identical


IMPORTANT WARNING: Sequences AI001_N204 and AI107_N314 are exactly identical


IMPORTANT WARNING: Sequences AI002_N220 and AI142_N325 are exactly identical


IMPORTANT WARNING: Sequences AI002_N225 and AI004_N247 are exactly identical


IMPORTANT WARNING: Sequences AI002_N225 and AI005_N271 are exactly identical


IMPORTANT WARNING: Sequences AI002_N225 and AI107_N317 are exactly identical


IMPORTANT WARNING: Sequences AI003_N234 and AI007_N281 are exactly identical


IMPORTANT WARNING: Sequences AI003_N234 and AI201_N333 are exactly identical


IMPORTANT WARNING: Sequences AI003_N236 and AI202_N338 are exactly identical


IMPORTANT WARNING: Sequences AI003_N236 and AI202_N342 are exactly identical


IMPORTANT WARNING: Sequences AI052_N288 and AI105_N300 are exactly identical


IMPORTANT WARNING: Sequences AI052_N289 and AI105_N301 are exactly identical


IMPORTANT WARNING: Sequences AI105_N307 and AI105_N309 are exactly identical


IMPORTANT WARNING: Sequences AI107_N312 and AI240_N346 are exactly identical


IMPORTANT WARNING: Sequences AI142_N329 and AI202_N339 are exactly identical

IMPORTANT WARNING
Found 15 sequences that are exactly identical to other sequences in the alignment.
Normally they should be excluded from the analysis.

Just in case you might need it, an alignment file with 
sequence duplicates removed is printed to file /data/saurav/CDC/AI/sequences.fasta.reduced


Using BFGS method to optimize GTR rate parameters, to disable this specify "--no-bfgs" 



This is RAxML version 8.2.12 released by Alexandros Stamatakis on May 2018.

With greatly appreciated code contributions by:
Andre Aberer      (HITS)
Simon Berger      (HITS)
Alexey Kozlov     (HITS)
Kassian Kobert    (HITS)
David Dao         (KIT and HITS)
Sarah Lutteropp   (KIT and HITS)
Nick Pattengale   (Sandia)
Wayne Pfeiffer    (SDSC)
Akifumi S. Tanabe (NRIFS)
Charlie Taylor    (UF)


Alignment has 129 distinct alignment patterns

Proportion of gaps and completely undetermined characters in this alignment: 0.00%

RAxML rapid bootstrapping and subsequent ML search

Using 1 distinct models/data partitions with joint branch length optimization



Executing 20 rapid bootstrap inferences and thereafter a thorough ML search 

All free model parameters will be estimated by RAxML
GAMMA model of rate heterogeneity, ML estimate of alpha-parameter

GAMMA Model parameters will be estimated up to an accuracy of 0.1000000000 Log Likelihood units

Partition: 0
Alignment Patterns: 129
Name: No Name Provided
DataType: DNA
Substitution Matrix: GTR




RAxML was called as follows:

raxmlHPC -f a -m GTRGAMMA -p 12345 -x 12345 -s /data/saurav/CDC/AI/sequences.fasta -w /data/saurav/CDC/AI/RAxML_output -N 20 -n cdc -k 



Time for BS model parameter optimization 1.144360
Bootstrap[0]: Time 4.625012 seconds, bootstrap likelihood -1709.350992, best rearrangement setting 13
Bootstrap[1]: Time 5.128432 seconds, bootstrap likelihood -2023.567798, best rearrangement setting 13
Bootstrap[2]: Time 4.847090 seconds, bootstrap likelihood -2016.184669, best rearrangement setting 12
Bootstrap[3]: Time 3.728770 seconds, bootstrap likelihood -1893.029611, best rearrangement setting 15
Bootstrap[4]: Time 3.497333 seconds, bootstrap likelihood -2056.658247, best rearrangement setting 10
Bootstrap[5]: Time 2.894805 seconds, bootstrap likelihood -1734.939051, best rearrangement setting 10
Bootstrap[6]: Time 2.984934 seconds, bootstrap likelihood -1835.891941, best rearrangement setting 6
Bootstrap[7]: Time 3.788633 seconds, bootstrap likelihood -2059.910214, best rearrangement setting 14
Bootstrap[8]: Time 2.700901 seconds, bootstrap likelihood -2014.699013, best rearrangement setting 5
Bootstrap[9]: Time 3.465184 seconds, bootstrap likelihood -1911.654555, best rearrangement setting 7
Bootstrap[10]: Time 3.232198 seconds, bootstrap likelihood -1975.660694, best rearrangement setting 7
Bootstrap[11]: Time 2.367912 seconds, bootstrap likelihood -1630.337664, best rearrangement setting 5
Bootstrap[12]: Time 3.287725 seconds, bootstrap likelihood -1965.068141, best rearrangement setting 8
Bootstrap[13]: Time 3.359619 seconds, bootstrap likelihood -1968.701068, best rearrangement setting 7
Bootstrap[14]: Time 3.944096 seconds, bootstrap likelihood -1927.096971, best rearrangement setting 12
Bootstrap[15]: Time 3.949435 seconds, bootstrap likelihood -1779.845251, best rearrangement setting 15
Bootstrap[16]: Time 3.380048 seconds, bootstrap likelihood -1865.357646, best rearrangement setting 12
Bootstrap[17]: Time 3.679716 seconds, bootstrap likelihood -1972.996842, best rearrangement setting 12
Bootstrap[18]: Time 2.661537 seconds, bootstrap likelihood -2237.970946, best rearrangement setting 5
Bootstrap[19]: Time 3.824113 seconds, bootstrap likelihood -1852.026236, best rearrangement setting 8


Overall Time for 20 Rapid Bootstraps 71.697489 seconds
Average Time per Rapid Bootstrap 3.584874 seconds

Starting ML Search ...

Fast ML optimization finished

Fast ML search Time: 66.711239 seconds

Slow ML Search 0 Likelihood: -2106.807766
Slow ML Search 1 Likelihood: -2108.832817
Slow ML Search 2 Likelihood: -2114.831505
Slow ML Search 3 Likelihood: -2115.139870
Slow ML optimization finished

Slow ML search Time: 103.675997 seconds
Thorough ML search Time: 8.364609 seconds

Final ML Optimization Likelihood: -2106.779965

Model Information:

Model Parameters of Partition 0, Name: No Name Provided, Type of Data: DNA
alpha: 0.649882
Tree-Length: 1.159359
rate A <-> C: 2.002152
rate A <-> G: 12.605162
rate A <-> T: 0.636739
rate C <-> G: 0.971444
rate C <-> T: 9.079206
rate G <-> T: 1.000000

freq pi(A): 0.161903
freq pi(C): 0.306865
freq pi(G): 0.301915
freq pi(T): 0.229318


ML search took 178.752918 secs or 0.049654 hours

Combined Bootstrap and ML search took 250.450441 secs or 0.069570 hours

Drawing Bootstrap Support Values on best-scoring ML tree ...



Found 1 tree in File /data/saurav/CDC/AI/RAxML_output/RAxML_bestTree.cdc



Found 1 tree in File /data/saurav/CDC/AI/RAxML_output/RAxML_bestTree.cdc

Program execution info written to /data/saurav/CDC/AI/RAxML_output/RAxML_info.cdc
All 20 bootstrapped trees written to: /data/saurav/CDC/AI/RAxML_output/RAxML_bootstrap.cdc

Best-scoring ML tree written to: /data/saurav/CDC/AI/RAxML_output/RAxML_bestTree.cdc

Best-scoring ML tree with support values written to: /data/saurav/CDC/AI/RAxML_output/RAxML_bipartitions.cdc

Best-scoring ML tree with support values as branch labels written to: /data/saurav/CDC/AI/RAxML_output/RAxML_bipartitionsBranchLabels.cdc

Overall execution time for full ML analysis: 250.459046 secs or 0.069572 hours or 0.002899 days

