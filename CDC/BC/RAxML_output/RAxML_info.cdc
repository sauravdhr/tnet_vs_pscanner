

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


Alignment has 68 distinct alignment patterns

Proportion of gaps and completely undetermined characters in this alignment: 0.00%

RAxML rapid bootstrapping and subsequent ML search

Using 1 distinct models/data partitions with joint branch length optimization



Executing 20 rapid bootstrap inferences and thereafter a thorough ML search 

All free model parameters will be estimated by RAxML
GAMMA model of rate heterogeneity, ML estimate of alpha-parameter

GAMMA Model parameters will be estimated up to an accuracy of 0.1000000000 Log Likelihood units

Partition: 0
Alignment Patterns: 68
Name: No Name Provided
DataType: DNA
Substitution Matrix: GTR




RAxML was called as follows:

raxmlHPC -f a -m GTRGAMMA -p 12345 -x 12345 -s /data/saurav/CDC/BC/sequences.fasta -w /data/saurav/CDC/BC/RAxML_output -N 20 -n cdc -k 



Time for BS model parameter optimization 0.391272
Bootstrap[0]: Time 1.146977 seconds, bootstrap likelihood -867.870611, best rearrangement setting 13
Bootstrap[1]: Time 0.936324 seconds, bootstrap likelihood -1176.228108, best rearrangement setting 13
Bootstrap[2]: Time 0.737033 seconds, bootstrap likelihood -985.300742, best rearrangement setting 12
Bootstrap[3]: Time 0.673836 seconds, bootstrap likelihood -1158.921188, best rearrangement setting 15
Bootstrap[4]: Time 0.617876 seconds, bootstrap likelihood -1099.470074, best rearrangement setting 10
Bootstrap[5]: Time 0.713987 seconds, bootstrap likelihood -966.365499, best rearrangement setting 10
Bootstrap[6]: Time 0.671363 seconds, bootstrap likelihood -1021.335352, best rearrangement setting 6
Bootstrap[7]: Time 0.629051 seconds, bootstrap likelihood -1050.302678, best rearrangement setting 14
Bootstrap[8]: Time 0.602903 seconds, bootstrap likelihood -1004.693527, best rearrangement setting 5
Bootstrap[9]: Time 0.673583 seconds, bootstrap likelihood -1020.100214, best rearrangement setting 7
Bootstrap[10]: Time 0.687811 seconds, bootstrap likelihood -1090.117138, best rearrangement setting 7
Bootstrap[11]: Time 0.579229 seconds, bootstrap likelihood -899.456493, best rearrangement setting 5
Bootstrap[12]: Time 0.751168 seconds, bootstrap likelihood -921.507391, best rearrangement setting 8
Bootstrap[13]: Time 0.594655 seconds, bootstrap likelihood -1150.526909, best rearrangement setting 7
Bootstrap[14]: Time 0.711729 seconds, bootstrap likelihood -1063.466783, best rearrangement setting 12
Bootstrap[15]: Time 0.611292 seconds, bootstrap likelihood -990.969850, best rearrangement setting 15
Bootstrap[16]: Time 0.671612 seconds, bootstrap likelihood -1162.306193, best rearrangement setting 12
Bootstrap[17]: Time 0.892884 seconds, bootstrap likelihood -914.990221, best rearrangement setting 12
Bootstrap[18]: Time 0.730237 seconds, bootstrap likelihood -1179.497977, best rearrangement setting 5
Bootstrap[19]: Time 0.727268 seconds, bootstrap likelihood -971.144529, best rearrangement setting 8


Overall Time for 20 Rapid Bootstraps 14.368067 seconds
Average Time per Rapid Bootstrap 0.718403 seconds

Starting ML Search ...

Fast ML optimization finished

Fast ML search Time: 20.455684 seconds

Slow ML Search 0 Likelihood: -1096.526305
Slow ML Search 1 Likelihood: -1098.905755
Slow ML Search 2 Likelihood: -1098.810562
Slow ML Search 3 Likelihood: -1096.526143
Slow ML optimization finished

Slow ML search Time: 27.081469 seconds
Thorough ML search Time: 2.137319 seconds

Final ML Optimization Likelihood: -1096.460868

Model Information:

Model Parameters of Partition 0, Name: No Name Provided, Type of Data: DNA
alpha: 0.235264
Tree-Length: 0.535800
rate A <-> C: 0.423819
rate A <-> G: 30.166535
rate A <-> T: 1.983620
rate C <-> G: 4.009983
rate C <-> T: 25.634887
rate G <-> T: 1.000000

freq pi(A): 0.185350
freq pi(C): 0.294072
freq pi(G): 0.313319
freq pi(T): 0.207258


ML search took 49.675313 secs or 0.013799 hours

Combined Bootstrap and ML search took 64.043425 secs or 0.017790 hours

Drawing Bootstrap Support Values on best-scoring ML tree ...



Found 1 tree in File /data/saurav/CDC/BC/RAxML_output/RAxML_bestTree.cdc



Found 1 tree in File /data/saurav/CDC/BC/RAxML_output/RAxML_bestTree.cdc

Program execution info written to /data/saurav/CDC/BC/RAxML_output/RAxML_info.cdc
All 20 bootstrapped trees written to: /data/saurav/CDC/BC/RAxML_output/RAxML_bootstrap.cdc

Best-scoring ML tree written to: /data/saurav/CDC/BC/RAxML_output/RAxML_bestTree.cdc

Best-scoring ML tree with support values written to: /data/saurav/CDC/BC/RAxML_output/RAxML_bipartitions.cdc

Best-scoring ML tree with support values as branch labels written to: /data/saurav/CDC/BC/RAxML_output/RAxML_bipartitionsBranchLabels.cdc

Overall execution time for full ML analysis: 64.047581 secs or 0.017791 hours or 0.000741 days

