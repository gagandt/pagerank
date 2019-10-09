# PageRank using Points Distribution Method

> Points Ditribution Method  is a method to determine the rank of nodes a graph.

The algorithm of is as follows:
  - Distribute same points to all the nodes in a graph.
  - Keep distributing points iteratively to the nodes.
  - Stop the distribution of points till the points of the nodes converge.
  - Sort the nodes on basis of the points accumulated.
  - The rank of the node is determined using the sorted points.

The distribuition of points is done using the following algorithm:
  - Count the number of outlinks of a particular node.
  - The share to be divided is calculated as the points of the node divided by the number of outlinks.
  - This share is incremented in points of each of the outlinks.

The drawbacks of PDM are:

> **Points Sink**
> - If a node has no outlinks, then it keeps on getting points but does not distributes its own points.
> - Points are getting accumulated at one node or a set of nodes.
> - There is a loop between two nodes and no other outlinks.    

Solution to point sink problem is as follows:
  - Set a parameter 'S' (usually 0.2).
  - Now, after each iteration, a fraction of points from each node is taken and distributed equally amongst all the nodes.
  - This fraction is determined by the value 'S'.
  - The total points in a graph never change and they are just distributed amongst themselves.
