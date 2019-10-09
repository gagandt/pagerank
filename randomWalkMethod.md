# Random Walk Method

> This method reflects the probability of landing on a random page. A page with more number of inlinks is likely to be rewarded a higher rank in this method. It uses two concepts: Random walk and Teleporatation and rewards points to the node whenever it arrives at that particular node.

The algorithm is as follows:
  - Initialise a points array to 0 corresponding to the nodes in the graph.
  - Choose a random starting point and increment its points by one.
  - Get the outlinks of this node.
  - Now, choose a random node from the set of outlinks.
  - Increment the points of this outlink and replace the previous outlinks by the outlinks of this node.
  - If a node does not has any outlink, again choose a random node from the graph. This step is *Teleporatation*.
  - Repeat this process for a large number of times.
  - Sort the nodes on the basis of the Random walk scores.