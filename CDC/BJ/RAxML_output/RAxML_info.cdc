

IMPORTANT WARNING: Sequences BJ23_N1107 and BJ25_N1116 are exactly identical


IMPORTANT WARNING: Sequences BJ23_N1107 and BJ28_N1128 are exactly identical


IMPORTANT WARNING: Sequences BJ25_N1118 and BJ28_N1125 are exactly identical

IMPORTANT WARNING
Found 3 sequences that are exactly identical to other sequences in the alignment.
Normally they should be excluded from the analysis.

Just in case you might need it, an alignment file with 
sequence duplicates removed is printed to file /data/saurav/CDC/BJ/sequences.fasta.reduced


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


Alignment has 51 distinct alignment patterns

Proportion of gaps and completely undetermined characters in this alignment: 0.00%

RAxML rapid bootstrapping and subsequent ML search

Using 1 distinct models/data partitions with joint branch length optimization



Executing 20 rapid bootstrap inferences and thereafter a thorough ML search 

All free model parameters will be estimated by RAxML
GAMMA model of rate heterogeneity, ML estimate of alpha-parameter

GAMMA Model parameters will be estimated up to an accuracy of 0.1000000000 Log Likelihood units

Partition: 0
Alignment Patterns: 51
Name: No Name Provided
DataType: DNA
Substitution Matrix: GTR




RAxML was called as follows:

raxmlHPC -f a -m GTRGAMMA -p 12345 -x 12345 -s /data/saurav/CDC/BJ/sequences.fasta -w /data/saurav/CDC/BJ/RAxML_output -N 20 -n cdc -k 



Time for BS model parameter optimization 0.255827
Bootstrap[0]: Time 0.699424 seconds, bootstrap likelihood -723.733984, best rearrangement setting 13
Bootstrap[1]: Time 0.449088 seconds, bootstrap likelihood -1004.967714, best rearrangement setting 13
Bootstrap[2]: Time 0.452753 seconds, bootstrap likelihood -848.241899, best rearrangement setting 12
Bootstrap[3]: Time 0.469863 seconds, bootstrap likelihood -780.709274, best rearrangement setting 15
Bootstrap[4]: Time 0.626054 seconds, bootstrap likelihood -989.271858, best rearrangement setting 10
Bootstrap[5]: Time 0.530265 seconds, bootstrap likelihood -905.041863, best rearrangement setting 10
Bootstrap[6]: Time 0.472776 seconds, bootstrap likelihood -872.897082, best rearrangement setting 6
Bootstrap[7]: Time 0.510652 seconds, bootstrap likelihood -926.946341, best rearrangement setting 14
Bootstrap[8]: Time 0.372062 seconds, bootstrap likelihood -842.052116, best rearrangement setting 5
Bootstrap[9]: Time 0.415993 seconds, bootstrap likelihood -834.630048, best rearrangement setting 7
Bootstrap[10]: Time 0.529232 seconds, bootstrap likelihood -1003.175360, best rearrangement setting 7
Bootstrap[11]: Time 0.448997 seconds, bootstrap likelihood -855.661451, best rearrangement setting 5
Bootstrap[12]: Time 0.571486 seconds, bootstrap likelihood -774.423308, best rearrangement setting 8
Bootstrap[13]: Time 0.495114 seconds, bootstrap likelihood -1044.284458, best rearrangement setting 7
Bootstrap[14]: Time 0.472730 seconds, bootstrap likelihood -901.408926, best rearrangement setting 12
Bootstrap[15]: Time 0.513769 seconds, bootstrap likelihood -762.685981, best rearrangement setting 15
Bootstrap[16]: Time 0.712780 seconds, bootstrap likelihood -923.988950, best rearrangement setting 12
Bootstrap[17]: Time 0.456806 seconds, bootstrap likelihood -914.346750, best rearrangement setting 12
Bootstrap[18]: Time 0.439226 seconds, bootstrap likelihood -925.799212, best rearrangement setting 5
Bootstrap[19]: Time 0.579939 seconds, bootstrap likelihood -773.196034, best rearrangement setting 8


Overall Time for 20 Rapid Bootstraps 10.224898 seconds
Average Time per Rapid Bootstrap 0.511245 seconds

Starting ML Search ...

Fast ML optimization finished

Fast ML search Time: 5.377829 seconds

Slow ML Search 0 Likelihood: -932.406554
Slow ML Search 1 Likelihood: -932.504456
Slow ML Search 2 Likelihood: -932.504459
Slow ML Search 3 Likelihood: -933.693825
Slow ML optimization finished

Slow ML search Time: 12.010011 seconds
Thorough ML search Time: 1.531406 seconds

Final ML Optimization Likelihood: -932.406439

Model Information:

Model Parameters of Partition 0, Name: No Name Provided, Type of Data: DNA
alpha: 0.136975
Tree-Length: 0.397618
rate A <-> C: 0.998753
rate A <-> G: 5.092145
rate A <-> T: 0.211686
rate C <-> G: 0.466173
rate C <-> T: 4.931280
rate G <-> T: 1.000000

freq pi(A): 0.181938
freq pi(C): 0.294913
freq pi(G): 0.317400
freq pi(T): 0.205748


ML search took 18.919965 secs or 0.005256 hours

Combined Bootstrap and ML search took 29.144908 secs or 0.008096 hours

Drawing Bootstrap Support Values on best-scoring ML tree ...



Found 1 tree in File /data/saurav/CDC/BJ/RAxML_output/RAxML_bestTree.cdc



Found 1 tree in File /data/saurav/CDC/BJ/RAxML_output/RAxML_bestTree.cdc

Program execution info written to /data/saurav/CDC/BJ/RAxML_output/RAxML_info.cdc
All 20 bootstrapped trees written to: /data/saurav/CDC/BJ/RAxML_output/RAxML_bootstrap.cdc

Best-scoring ML tree written to: /data/saurav/CDC/BJ/RAxML_output/RAxML_bestTree.cdc

Best-scoring ML tree with support values written to: /data/saurav/CDC/BJ/RAxML_output/RAxML_bipartitions.cdc

Best-scoring ML tree with support values as branch labels written to: /data/saurav/CDC/BJ/RAxML_output/RAxML_bipartitionsBranchLabels.cdc

Overall execution time for full ML analysis: 29.148003 secs or 0.008097 hours or 0.000337 days

