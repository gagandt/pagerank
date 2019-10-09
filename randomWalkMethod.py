import networkx as nx
import random
from random import choice

import numpy as np

def add_edges(graph, probablity):
    for i in graph.nodes():
        for j in graph.nodes():
            if i == j:
                continue
            rand = random.random()
            if rand <= probablity:
                graph.add_edge(i, j)
            
    return graph

def random_walk(graph):
    nodes = graph.nodes()
    points = [0 for i in range(graph.number_of_nodes())]

    r = random.choice(list(nodes))
    points[r] += 1
    outlinks = graph.out_edges(r)

    c = 0
    while(c != 10000):
        if len(outlinks) == 0:
            focus = random.choice(list(nodes))
        else:
            r1 = random.choice(list(outlinks))
            focus = r1[1]
        points[focus] += 1
        outlinks = graph.out_edges(focus)
        c += 1
    return points

def sort_nodes(points):
    points_array = np.array(points)
    sorted_nodes = np.argsort(-points_array)
    return sorted_nodes

def main():
    # Creating a directed graph
    graph = nx.DiGraph()
    graph.add_nodes_from([i for i in range(10)])
    graph = add_edges(graph, 0.3)

    # Perform Random Walk on the graph
    points = random_walk(graph)

    # Sort the points
    sorted_nodes = sort_nodes(points)
    print(sorted_nodes)

    pagerank = nx.pagerank(graph)
    pagerank_sorted = sorted(pagerank.items(), key = lambda x:x[1], reverse = True)
    for i in pagerank_sorted:
        print(i[0])

main()