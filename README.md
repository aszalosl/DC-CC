# DC-CC
Divide and Conquer - Correlation Clustering

Software part of [FEDCSIS WCO](https://fedcsis.org/2016/wco) conference paper: 
_L. Aszalós, M. Bakó - Correlation clustering: divide and conquer_.

The [correlation clustering](https://en.wikipedia.org/wiki/Correlation_clustering) 
is an NP-hard problem, hence its solving methods do not scale well. 
The contraction method and its improvement enable us to construct a divide and conquer algorithm, 
which could help us to clustering bigger sets.

Here you can find the Python3 programs for 
* generating random signed graphs (Erdős-Rényi and Barabási-Albert)
* handling Union-Find data structure
* clustering with dict of dict
* testing speed and accuracy of clustering.
