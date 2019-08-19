This file contains general helpful information about the GEMF output.

=== output.txt ===
This is the main file of interest. It contains the GEMF simulation output. The columns of the output file are as follows (in the exact order):
* Time of event
* Total rate
* Node that was infected
* Previous state of the node
* New state of node
* Number of nodes in each state (one column per state)
* Comma-delimited lists of inducer nodes from each state (one state per list)

=== State Number Translations ===
S = 0
I = 1
T = 2
R = 3
V = 3
