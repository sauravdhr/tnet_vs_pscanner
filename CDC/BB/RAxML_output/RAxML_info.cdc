

IMPORTANT WARNING: Sequences BB1_N848 and BB31_N873 are exactly identical


IMPORTANT WARNING: Sequences BB1_N848 and BB41_N887 are exactly identical


IMPORTANT WARNING: Sequences BB31_N880 and BB41_N886 are exactly identical


IMPORTANT WARNING: Sequences BB41_N884 and BB45_N987 are exactly identical

IMPORTANT WARNING
Found 4 sequences that are exactly identical to other sequences in the alignment.
Normally they should be excluded from the analysis.

Just in case you might need it, an alignment file with 
sequence duplicates removed is printed to file /data/saurav/CDC/BB/sequences.fasta.reduced


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


Alignment has 149 distinct alignment patterns

Proportion of gaps and completely undetermined characters in this alignment: 0.00%

RAxML rapid bootstrapping and subsequent ML search

Using 1 distinct models/data partitions with joint branch length optimization



Executing 20 rapid bootstrap inferences and thereafter a thorough ML search 

All free model parameters will be estimated by RAxML
GAMMA model of rate heterogeneity, ML estimate of alpha-parameter

GAMMA Model parameters will be estimated up to an accuracy of 0.1000000000 Log Likelihood units

Partition: 0
Alignment Patterns: 149
Name: No Name Provided
DataType: DNA
Substitution Matrix: GTR




RAxML was called as follows:

raxmlHPC -f a -m GTRGAMMA -p 12345 -x 12345 -s /data/saurav/CDC/BB/sequences.fasta -w /data/saurav/CDC/BB/RAxML_output -N 20 -n cdc -k 



Time for BS model parameter optimization 0.712114
Bootstrap[0]: Time 6.297089 seconds, bootstrap likelihood -2316.187424, best rearrangement setting 13
Bootstrap[1]: Time 6.100060 seconds, bootstrap likelihood -2636.886118, best rearrangement setting 13
Bootstrap[2]: Time 5.108772 seconds, bootstrap likelihood -2485.430997, best rearrangement setting 12
Bootstrap[3]: Time 5.888288 seconds, bootstrap likelihood -2312.097106, best rearrangement setting 15
Bootstrap[4]: Time 6.750026 seconds, bootstrap likelihood -2719.963262, best rearrangement setting 10
Bootstrap[5]: Time 4.253834 seconds, bootstrap likelihood -2643.929152, best rearrangement setting 10
Bootstrap[6]: Time 3.827023 seconds, bootstrap likelihood -2467.869396, best rearrangement setting 6
Bootstrap[7]: Time 4.432765 seconds, bootstrap likelihood -2428.821050, best rearrangement setting 14
Bootstrap[8]: Time 3.189231 seconds, bootstrap likelihood -2540.500878, best rearrangement setting 5
Bootstrap[9]: Time 4.278464 seconds, bootstrap likelihood -2144.659356, best rearrangement setting 7
Bootstrap[10]: Time 4.017972 seconds, bootstrap likelihood -2918.947493, best rearrangement setting 7
Bootstrap[11]: Time 3.447385 seconds, bootstrap likelihood -2139.048155, best rearrangement setting 5
Bootstrap[12]: Time 4.715166 seconds, bootstrap likelihood -2516.613275, best rearrangement setting 8
Bootstrap[13]: Time 4.681362 seconds, bootstrap likelihood -2678.862355, best rearrangement setting 7
Bootstrap[14]: Time 5.497777 seconds, bootstrap likelihood -2650.220367, best rearrangement setting 12
Bootstrap[15]: Time 5.429131 seconds, bootstrap likelihood -2242.326856, best rearrangement setting 15
Bootstrap[16]: Time 4.914543 seconds, bootstrap likelihood -2420.710268, best rearrangement setting 12
Bootstrap[17]: Time 4.992267 seconds, bootstrap likelihood -2376.356878, best rearrangement setting 12
Bootstrap[18]: Time 4.189077 seconds, bootstrap likelihood -2618.643529, best rearrangement setting 5
Bootstrap[19]: Time 6.030035 seconds, bootstrap likelihood -2236.536644, best rearrangement setting 8


Overall Time for 20 Rapid Bootstraps 98.061400 seconds
Average Time per Rapid Bootstrap 4.903070 seconds

Starting ML Search ...

Fast ML optimization finished

Fast ML search Time: 61.237328 seconds

Slow ML Search 0 Likelihood: -2633.153350
Slow ML Search 1 Likelihood: -2633.354620
Slow ML Search 2 Likelihood: -2631.653077
Slow ML Search 3 Likelihood: -2628.779414
Slow ML optimization finished

Slow ML search Time: 157.526059 seconds
Thorough ML search Time: 11.773536 seconds

Final ML Optimization Likelihood: -2628.579284

Model Information:

Model Parameters of Partition 0, Name: No Name Provided, Type of Data: DNA
alpha: 0.796828
Tree-Length: 1.400796
rate A <-> C: 1.055871
rate A <-> G: 3.380285
rate A <-> T: 0.861060
rate C <-> G: 0.787508
rate C <-> T: 2.298448
rate G <-> T: 1.000000

freq pi(A): 0.194328
freq pi(C): 0.308681
freq pi(G): 0.299324
freq pi(T): 0.197666


ML search took 230.537996 secs or 0.064038 hours

Combined Bootstrap and ML search took 328.599455 secs or 0.091278 hours

Drawing Bootstrap Support Values on best-scoring ML tree ...



Found 1 tree in File /data/saurav/CDC/BB/RAxML_output/RAxML_bestTree.cdc



Found 1 tree in File /data/saurav/CDC/BB/RAxML_output/RAxML_bestTree.cdc

Program execution info written to /data/saurav/CDC/BB/RAxML_output/RAxML_info.cdc
All 20 bootstrapped trees written to: /data/saurav/CDC/BB/RAxML_output/RAxML_bootstrap.cdc

Best-scoring ML tree written to: /data/saurav/CDC/BB/RAxML_output/RAxML_bestTree.cdc

Best-scoring ML tree with support values written to: /data/saurav/CDC/BB/RAxML_output/RAxML_bipartitions.cdc

Best-scoring ML tree with support values as branch labels written to: /data/saurav/CDC/BB/RAxML_output/RAxML_bipartitionsBranchLabels.cdc

Overall execution time for full ML analysis: 328.609211 secs or 0.091280 hours or 0.003803 days

