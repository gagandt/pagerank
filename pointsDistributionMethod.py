import networkx as nx
import random
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

def initialize_points(graph):
    points = [100 for i in range(graph.number_of_nodes())]
    return points

def distribute_points(graph, points):
    prev_points = points
    new_points = [0 for i in range(graph.number_of_nodes())]

    for i in graph.nodes():
        outlinks = graph.out_edges(i)
        if len(outlinks) == 0:
            new_points[i] += prev_points[i]
        else:
            share = (float)(prev_points[i]) / len(outlinks)
            for outlink in outlinks:
                new_points[outlink[1]] += share

    return graph, new_points

def handle_points_sink(graph, points):
    reduction_percentage = 0.8
    n = graph.number_of_nodes()

    for i in range(len(points)):
        points[i] = (float)(points[i])*reduction_percentage
    
    extra_points = ((float)(n)*100*(1 - reduction_percentage))/n
    for i in range(len(points)):
        points[i] += extra_points
    
    return points


def distribute_points_till_convergence(graph, points):
    prev_points = points
    while(1):
        graph, new_points = distribute_points(graph, prev_points)
        new_points = handle_points_sink(graph, new_points)

        char = input()
        if char == 'q':
            break
        prev_points = new_points
    
    return graph, new_points

def sort_nodes(points):
    points_array = np.array(points)
    sorted_nodes = np.argsort(-points_array)
    return sorted_nodes

def main():
    # Creating a directed graph
    graph = nx.DiGraph()
    graph.add_nodes_from([i for i in range(10)])
    graph = add_edges(graph, 0.3)

    # Distributing points to thhe nodes
    points = initialize_points(graph)

    # Keep distributing points
    graph, points = distribute_points_till_convergence(graph, points)

    # Sort the points
    sorted_nodes = sort_nodes(points)
    print(sorted_nodes)

    pagerank = nx.pagerank(graph)
    pagerank_sorted = sorted(pagerank.items(), key = lambda x:x[1], reverse = True)
    for i in pagerank_sorted:
        print(i[0])
    
main()