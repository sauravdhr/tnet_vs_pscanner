

IMPORTANT WARNING: Sequences AJ6_N400 and AJ86_N409 are exactly identical

IMPORTANT WARNING
Found 1 sequence that is exactly identical to other sequences in the alignment.
Normally they should be excluded from the analysis.

Just in case you might need it, an alignment file with 
sequence duplicates removed is printed to file /data/saurav/CDC/AJ/sequences.fasta.reduced


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


Alignment has 83 distinct alignment patterns

Proportion of gaps and completely undetermined characters in this alignment: 0.00%

RAxML rapid bootstrapping and subsequent ML search

Using 1 distinct models/data partitions with joint branch length optimization



Executing 20 rapid bootstrap inferences and thereafter a thorough ML search 

All free model parameters will be estimated by RAxML
GAMMA model of rate heterogeneity, ML estimate of alpha-parameter

GAMMA Model parameters will be estimated up to an accuracy of 0.1000000000 Log Likelihood units

Partition: 0
Alignment Patterns: 83
Name: No Name Provided
DataType: DNA
Substitution Matrix: GTR




RAxML was called as follows:

raxmlHPC -f a -m GTRGAMMA -p 12345 -x 12345 -s /data/saurav/CDC/AJ/sequences.fasta -w /data/saurav/CDC/AJ/RAxML_output -N 20 -n cdc -k 



Time for BS model parameter optimization 0.148281
Bootstrap[0]: Time 0.568444 seconds, bootstrap likelihood -1018.583092, best rearrangement setting 13
Bootstrap[1]: Time 0.455551 seconds, bootstrap likelihood -1209.740559, best rearrangement setting 13
Bootstrap[2]: Time 0.357130 seconds, bootstrap likelihood -1021.635569, best rearrangement setting 12
Bootstrap[3]: Time 0.422650 seconds, bootstrap likelihood -1074.279066, best rearrangement setting 15
Bootstrap[4]: Time 0.369460 seconds, bootstrap likelihood -1214.759705, best rearrangement setting 10
Bootstrap[5]: Time 0.336377 seconds, bootstrap likelihood -1135.060549, best rearrangement setting 10
Bootstrap[6]: Time 0.382093 seconds, bootstrap likelihood -1111.934251, best rearrangement setting 6
Bootstrap[7]: Time 0.328674 seconds, bootstrap likelihood -1065.453386, best rearrangement setting 14
Bootstrap[8]: Time 0.400464 seconds, bootstrap likelihood -1077.744548, best rearrangement setting 5
Bootstrap[9]: Time 0.311126 seconds, bootstrap likelihood -1058.779843, best rearrangement setting 7
Bootstrap[10]: Time 0.430132 seconds, bootstrap likelihood -1176.250389, best rearrangement setting 7
Bootstrap[11]: Time 0.402083 seconds, bootstrap likelihood -1078.409030, best rearrangement setting 5
Bootstrap[12]: Time 0.432068 seconds, bootstrap likelihood -1065.679038, best rearrangement setting 8
Bootstrap[13]: Time 0.389589 seconds, bootstrap likelihood -1228.133276, best rearrangement setting 7
Bootstrap[14]: Time 0.405254 seconds, bootstrap likelihood -1214.399628, best rearrangement setting 12
Bootstrap[15]: Time 0.540166 seconds, bootstrap likelihood -987.087284, best rearrangement setting 15
Bootstrap[16]: Time 0.525874 seconds, bootstrap likelihood -1110.874303, best rearrangement setting 12
Bootstrap[17]: Time 0.417057 seconds, bootstrap likelihood -1096.401682, best rearrangement setting 12
Bootstrap[18]: Time 0.409248 seconds, bootstrap likelihood -1189.003456, best rearrangement setting 5
Bootstrap[19]: Time 0.393155 seconds, bootstrap likelihood -1092.449932, best rearrangement setting 8


Overall Time for 20 Rapid Bootstraps 8.336984 seconds
Average Time per Rapid Bootstrap 0.416849 seconds

Starting ML Search ...

Fast ML optimization finished

Fast ML search Time: 3.779570 seconds

Slow ML Search 0 Likelihood: -1173.310588
Slow ML Search 1 Likelihood: -1173.310589
Slow ML Search 2 Likelihood: -1175.064868
Slow ML Search 3 Likelihood: -1175.593120
Slow ML optimization finished

Slow ML search Time: 5.050765 seconds
Thorough ML search Time: 1.417877 seconds

Final ML Optimization Likelihood: -1173.310506

Model Information:

Model Parameters of Partition 0, Name: No Name Provided, Type of Data: DNA
alpha: 0.488967
Tree-Length: 0.552316
rate A <-> C: 1.330465
rate A <-> G: 12.684163
rate A <-> T: 2.221978
rate C <-> G: 1.181203
rate C <-> T: 8.903008
rate G <-> T: 1.000000

freq pi(A): 0.189394
freq pi(C): 0.276902
freq pi(G): 0.314626
freq pi(T): 0.219079


ML search took 10.248898 secs or 0.002847 hours

Combined Bootstrap and ML search took 18.585914 secs or 0.005163 hours

Drawing Bootstrap Support Values on best-scoring ML tree ...



Found 1 tree in File /data/saurav/CDC/AJ/RAxML_output/RAxML_bestTree.cdc



Found 1 tree in File /data/saurav/CDC/AJ/RAxML_output/RAxML_bestTree.cdc

Program execution info written to /data/saurav/CDC/AJ/RAxML_output/RAxML_info.cdc
All 20 bootstrapped trees written to: /data/saurav/CDC/AJ/RAxML_output/RAxML_bootstrap.cdc

Best-scoring ML tree written to: /data/saurav/CDC/AJ/RAxML_output/RAxML_bestTree.cdc

Best-scoring ML tree with support values written to: /data/saurav/CDC/AJ/RAxML_output/RAxML_bipartitions.cdc

Best-scoring ML tree with support values as branch labels written to: /data/saurav/CDC/AJ/RAxML_output/RAxML_bipartitionsBranchLabels.cdc

Overall execution time for full ML analysis: 18.588471 secs or 0.005163 hours or 0.000215 days

