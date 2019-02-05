import networkx as nx
import numpy as np

def make_graph(maze_array):
    """
    Takes a 2D maze array and returns an graph representing
    the path squares in the maze as nodes with edges joining
    each path point.
    """
    path_graph = nx.Graph()
    path_points = []
    for i in range(maze_array.shape[0]):
        for j in range(maze_array.shape[1]):
            if maze_array[i,j] == 0:
                path_points.append((i,j))
    for p in path_points:
        path_graph.add_node(p)
    nodes = path_graph.nodes()
    for node in nodes:
        below = (node[0]+1, node[1])
        left = (node[0], node[1] - 1)
        right = (node[0], node[1] + 1)
        if below in nodes:
            path_graph.add_edge(node, below)
        if left in nodes:
            path_graph.add_edge(node, left)
        if right in nodes:
            path_graph.add_edge(node, right)
    return path_graph
