

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


Alignment has 99 distinct alignment patterns

Proportion of gaps and completely undetermined characters in this alignment: 0.00%

RAxML rapid bootstrapping and subsequent ML search

Using 1 distinct models/data partitions with joint branch length optimization



Executing 20 rapid bootstrap inferences and thereafter a thorough ML search 

All free model parameters will be estimated by RAxML
GAMMA model of rate heterogeneity, ML estimate of alpha-parameter

GAMMA Model parameters will be estimated up to an accuracy of 0.1000000000 Log Likelihood units

Partition: 0
Alignment Patterns: 99
Name: No Name Provided
DataType: DNA
Substitution Matrix: GTR




RAxML was called as follows:

raxmlHPC -f a -m GTRGAMMA -p 12345 -x 12345 -s /data/saurav/CDC/BA/sequences.fasta -w /data/saurav/CDC/BA/RAxML_output -N 20 -n cdc -k 



Time for BS model parameter optimization 0.878996
Bootstrap[0]: Time 3.153744 seconds, bootstrap likelihood -1634.300989, best rearrangement setting 13
Bootstrap[1]: Time 2.706526 seconds, bootstrap likelihood -1779.404193, best rearrangement setting 13
Bootstrap[2]: Time 2.291798 seconds, bootstrap likelihood -1792.491209, best rearrangement setting 12
Bootstrap[3]: Time 2.237513 seconds, bootstrap likelihood -1513.781647, best rearrangement setting 15
Bootstrap[4]: Time 2.347863 seconds, bootstrap likelihood -1824.437341, best rearrangement setting 10
Bootstrap[5]: Time 2.231751 seconds, bootstrap likelihood -1825.557890, best rearrangement setting 10
Bootstrap[6]: Time 2.051687 seconds, bootstrap likelihood -1646.471665, best rearrangement setting 6
Bootstrap[7]: Time 2.401933 seconds, bootstrap likelihood -1735.465470, best rearrangement setting 14
Bootstrap[8]: Time 1.943088 seconds, bootstrap likelihood -1775.772536, best rearrangement setting 5
Bootstrap[9]: Time 2.163185 seconds, bootstrap likelihood -1708.206145, best rearrangement setting 7
Bootstrap[10]: Time 2.409397 seconds, bootstrap likelihood -1870.028678, best rearrangement setting 7
Bootstrap[11]: Time 1.710428 seconds, bootstrap likelihood -1622.122842, best rearrangement setting 5
Bootstrap[12]: Time 2.419663 seconds, bootstrap likelihood -1537.880704, best rearrangement setting 8
Bootstrap[13]: Time 2.347682 seconds, bootstrap likelihood -1743.077570, best rearrangement setting 7
Bootstrap[14]: Time 2.413471 seconds, bootstrap likelihood -1702.293474, best rearrangement setting 12
Bootstrap[15]: Time 2.573969 seconds, bootstrap likelihood -1441.564800, best rearrangement setting 15
Bootstrap[16]: Time 2.381871 seconds, bootstrap likelihood -1666.364438, best rearrangement setting 12
Bootstrap[17]: Time 2.316752 seconds, bootstrap likelihood -1562.662867, best rearrangement setting 12
Bootstrap[18]: Time 2.054594 seconds, bootstrap likelihood -1953.587394, best rearrangement setting 5
Bootstrap[19]: Time 2.214768 seconds, bootstrap likelihood -1556.424135, best rearrangement setting 8


Overall Time for 20 Rapid Bootstraps 46.427278 seconds
Average Time per Rapid Bootstrap 2.321364 seconds

Starting ML Search ...

Fast ML optimization finished

Fast ML search Time: 35.707419 seconds

Slow ML Search 0 Likelihood: -1813.270720
Slow ML Search 1 Likelihood: -1813.104099
Slow ML Search 2 Likelihood: -1812.973372
Slow ML Search 3 Likelihood: -1819.328532
Slow ML optimization finished

Slow ML search Time: 50.667493 seconds
Thorough ML search Time: 7.502616 seconds

Final ML Optimization Likelihood: -1812.959659

Model Information:

Model Parameters of Partition 0, Name: No Name Provided, Type of Data: DNA
alpha: 0.299273
Tree-Length: 1.247154
rate A <-> C: 0.814452
rate A <-> G: 13.532000
rate A <-> T: 2.656709
rate C <-> G: 1.045825
rate C <-> T: 11.401065
rate G <-> T: 1.000000

freq pi(A): 0.202423
freq pi(C): 0.280625
freq pi(G): 0.294917
freq pi(T): 0.222034


ML search took 93.878504 secs or 0.026077 hours

Combined Bootstrap and ML search took 140.305816 secs or 0.038974 hours

Drawing Bootstrap Support Values on best-scoring ML tree ...



Found 1 tree in File /data/saurav/CDC/BA/RAxML_output/RAxML_bestTree.cdc



Found 1 tree in File /data/saurav/CDC/BA/RAxML_output/RAxML_bestTree.cdc

Program execution info written to /data/saurav/CDC/BA/RAxML_output/RAxML_info.cdc
All 20 bootstrapped trees written to: /data/saurav/CDC/BA/RAxML_output/RAxML_bootstrap.cdc

Best-scoring ML tree written to: /data/saurav/CDC/BA/RAxML_output/RAxML_bestTree.cdc

Best-scoring ML tree with support values written to: /data/saurav/CDC/BA/RAxML_output/RAxML_bipartitions.cdc

Best-scoring ML tree with support values as branch labels written to: /data/saurav/CDC/BA/RAxML_output/RAxML_bipartitionsBranchLabels.cdc

Overall execution time for full ML analysis: 140.313463 secs or 0.038976 hours or 0.001624 days

