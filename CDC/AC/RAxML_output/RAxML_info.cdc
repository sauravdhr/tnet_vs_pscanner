

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


Alignment has 95 distinct alignment patterns

Proportion of gaps and completely undetermined characters in this alignment: 0.00%

RAxML rapid bootstrapping and subsequent ML search

Using 1 distinct models/data partitions with joint branch length optimization



Executing 20 rapid bootstrap inferences and thereafter a thorough ML search 

All free model parameters will be estimated by RAxML
GAMMA model of rate heterogeneity, ML estimate of alpha-parameter

GAMMA Model parameters will be estimated up to an accuracy of 0.1000000000 Log Likelihood units

Partition: 0
Alignment Patterns: 95
Name: No Name Provided
DataType: DNA
Substitution Matrix: GTR




RAxML was called as follows:

raxmlHPC -f a -m GTRGAMMA -p 12345 -x 12345 -s /data/saurav/CDC/AC/sequences.fasta -w /data/saurav/CDC/AC/RAxML_output -N 20 -n cdc -k 



Time for BS model parameter optimization 0.413704
Bootstrap[0]: Time 1.426944 seconds, bootstrap likelihood -1250.716445, best rearrangement setting 13
Bootstrap[1]: Time 0.950958 seconds, bootstrap likelihood -1435.076162, best rearrangement setting 13
Bootstrap[2]: Time 1.042283 seconds, bootstrap likelihood -1448.418288, best rearrangement setting 12
Bootstrap[3]: Time 1.012750 seconds, bootstrap likelihood -1645.571736, best rearrangement setting 15
Bootstrap[4]: Time 0.920992 seconds, bootstrap likelihood -1543.443973, best rearrangement setting 10
Bootstrap[5]: Time 0.824255 seconds, bootstrap likelihood -1441.778361, best rearrangement setting 10
Bootstrap[6]: Time 1.095358 seconds, bootstrap likelihood -1332.831007, best rearrangement setting 6
Bootstrap[7]: Time 1.016993 seconds, bootstrap likelihood -1609.069921, best rearrangement setting 14
Bootstrap[8]: Time 0.896562 seconds, bootstrap likelihood -1582.919920, best rearrangement setting 5
Bootstrap[9]: Time 0.914093 seconds, bootstrap likelihood -1587.788061, best rearrangement setting 7
Bootstrap[10]: Time 0.858250 seconds, bootstrap likelihood -1456.694375, best rearrangement setting 7
Bootstrap[11]: Time 0.796570 seconds, bootstrap likelihood -1292.545587, best rearrangement setting 5
Bootstrap[12]: Time 0.954285 seconds, bootstrap likelihood -1338.843638, best rearrangement setting 8
Bootstrap[13]: Time 0.938455 seconds, bootstrap likelihood -1524.075343, best rearrangement setting 7
Bootstrap[14]: Time 0.810781 seconds, bootstrap likelihood -1458.360353, best rearrangement setting 12
Bootstrap[15]: Time 0.895185 seconds, bootstrap likelihood -1416.389799, best rearrangement setting 15
Bootstrap[16]: Time 0.965200 seconds, bootstrap likelihood -1405.770878, best rearrangement setting 12
Bootstrap[17]: Time 0.956428 seconds, bootstrap likelihood -1448.835119, best rearrangement setting 12
Bootstrap[18]: Time 0.837324 seconds, bootstrap likelihood -1445.520221, best rearrangement setting 5
Bootstrap[19]: Time 0.869359 seconds, bootstrap likelihood -1304.299334, best rearrangement setting 8


Overall Time for 20 Rapid Bootstraps 19.049175 seconds
Average Time per Rapid Bootstrap 0.952459 seconds

Starting ML Search ...

Fast ML optimization finished

Fast ML search Time: 11.617838 seconds

Slow ML Search 0 Likelihood: -1535.432122
Slow ML Search 1 Likelihood: -1535.432108
Slow ML Search 2 Likelihood: -1539.843499
Slow ML Search 3 Likelihood: -1535.432135
Slow ML optimization finished

Slow ML search Time: 29.246222 seconds
Thorough ML search Time: 3.432648 seconds

Final ML Optimization Likelihood: -1535.269476

Model Information:

Model Parameters of Partition 0, Name: No Name Provided, Type of Data: DNA
alpha: 0.334909
Tree-Length: 1.003787
rate A <-> C: 1.999325
rate A <-> G: 14.575650
rate A <-> T: 1.326978
rate C <-> G: 0.466667
rate C <-> T: 6.816013
rate G <-> T: 1.000000

freq pi(A): 0.176445
freq pi(C): 0.309197
freq pi(G): 0.297789
freq pi(T): 0.216570


ML search took 44.297546 secs or 0.012305 hours

Combined Bootstrap and ML search took 63.346767 secs or 0.017596 hours

Drawing Bootstrap Support Values on best-scoring ML tree ...



Found 1 tree in File /data/saurav/CDC/AC/RAxML_output/RAxML_bestTree.cdc



Found 1 tree in File /data/saurav/CDC/AC/RAxML_output/RAxML_bestTree.cdc

Program execution info written to /data/saurav/CDC/AC/RAxML_output/RAxML_info.cdc
All 20 bootstrapped trees written to: /data/saurav/CDC/AC/RAxML_output/RAxML_bootstrap.cdc

Best-scoring ML tree written to: /data/saurav/CDC/AC/RAxML_output/RAxML_bestTree.cdc

Best-scoring ML tree with support values written to: /data/saurav/CDC/AC/RAxML_output/RAxML_bipartitions.cdc

Best-scoring ML tree with support values as branch labels written to: /data/saurav/CDC/AC/RAxML_output/RAxML_bipartitionsBranchLabels.cdc

Overall execution time for full ML analysis: 63.351590 secs or 0.017598 hours or 0.000733 days

