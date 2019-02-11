import networkx as nx
from collections import deque


def make_passage_graph(maze_array):
    """Makes a networkx graph of the passages from a numpy array.

    Args:
        maze_array: A 2D numpy array.

    Returns:
        A networkx Graph object with passages in the maze
        represented as nodes joined by edges.
    """
    passage_graph = nx.Graph()
    height = maze_array.shape[0]
    width = maze_array.shape[1]

    for i in range(height):
        for j in range(width):
            value = maze_array[i, j]
            if value != 0:  # Only add eges for passages
                continue
            below = (i + 1, j)
            left = (i, j - 1)
            right = (i, j + 1)
            current = (i, j)
            if (i + 1) < height and value == maze_array[below]:
                passage_graph.add_edge(current, below)
            if (j - 1) >= 0 and value == maze_array[left]:
                passage_graph.add_edge(current, left)
            if (j + 1) < width and value == maze_array[right]:
                passage_graph.add_edge(current, right)

    return passage_graph


def make_section_graphs(maze_array):
    """Makes a networkx graph for each 'section' of the maze from a numpy array.

    Args:
        maze_array: A 2D numpy array.

    Returns:
        A list of networkx Graph objects, one for each 'section' of the maze.
        Graphs are named according to the array code, e.g. passages graphs have name='0'.
    """
    passage_graph = nx.Graph(name='0')
    wall_graph = nx.Graph(name='1')
    path_graph = nx.Graph(name='2')

    height = maze_array.shape[0]
    width = maze_array.shape[1]
    values = {0: passage_graph, 1: wall_graph, 2: path_graph}

    for i in range(height):
        for j in range(width):
            value = maze_array[i, j]
            below = (i + 1, j)
            left = (i, j - 1)
            right = (i, j + 1)
            current = (i, j)
            if (i + 1) < height and value == maze_array[below]:
                values.get(value).add_edge(current, below)
            if (j - 1) >= 0 and value == maze_array[left]:
                values.get(value).add_edge(current, left)
            if (j + 1) < width and value == maze_array[right]:
                values.get(value).add_edge(current, right)

    return values

class MazeGraph:
    """Class for handling maze graphs"""

    def __init__(self, maze_array):
        self.graphs = make_section_graphs(maze_array)

    def get_graphs(self):
        return self.graphs

    def get_graph(self, value):
        return self.graphs.get(value)

    def update_graphs(self, maze_array):
        self.graphs = make_section_graphs(maze_array)

    def update_graph(self, value, edges):
        self.graphs.get(value).add_edges_from(edges)

def solve_bfs(maze_graph, source, target):
    passages_graph = maze_graph.get_graph(0)

    visited = dict()
    parent = dict()
    for node in passages_graph.nodes():
        visited[node] = False
        parent[node] = (0,0)
    parent[source] = (-1,-1)

    q = deque()
    q.append(source)
    visited[source] = True

    while q:
        v = q.popleft()
        for n in nx.neighbors(passages_graph, v):
            if not visited[n]:
                q.append(n)
                visited[n] = True
                parent[n] = v

    path = [target]
    parent_node = parent[target]
    while parent_node != (-1,-1):
        path.insert(0, parent_node)
        parent_node = parent[parent_node]
    
    return (path, [n for n in visited.keys() if visited[n]])


def solve_astar(maze_graph, source, target, steps=False):
    pass