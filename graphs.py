import heapq
import networkx as nx
from math import sqrt
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

def solve_bfs(maze_graph, source, target, greedy=False):
    # Returns a simple euclidian distance for greedy bfs
    def get_heuristic(node):
        return int(sqrt((node[0]-target[0])**2 + (node[1]-target[1])**2))

    # Get the graph we want to search
    passages_graph = maze_graph.get_graph(0)

    # Need a visited and parent dictionay, and initialise both.
    visited = dict()
    parent = dict()
    for node in passages_graph.nodes():
        visited[node] = False
        parent[node] = (0,0)
    parent[source] = (-1,-1)
    visited[source] = True

    # Create queue and add the source node.
    q = deque()
    q.append(source)

    # While the queue still has items, pop first and visit neighbours.
    while q:
        v = q.popleft()
        for n in nx.neighbors(passages_graph, v):
            if not visited[n]:
                if not greedy:
                    q.append(n)
                else: # Greedy bfs expands nodes with a better heuristic first
                    if len(q) > 0 and get_heuristic(n) <= get_heuristic(q[0]):
                        q.appendleft(n)
                    else:
                        q.append(n)
                visited[n] = True
                parent[n] = v
        if v == target:
            break

    # Create the path
    path = [target]
    parent_node = parent[target]
    while parent_node != (-1,-1):
        path.append(parent_node)
        parent_node = parent[parent_node]
    
    # Return the path and a list of visited nodes
    return (path, [n for n in visited.keys() if visited[n]])

def solve_gbfs(maze_graph, source, target):
    return solve_bfs(maze_graph, source, target, greedy=True)

def solve_astar(maze_graph, source, target, steps=False):
    # Priority queue for node exploration
    class PriorityQueue:
        def __init__(self):
            self.items = []
        def is_empty(self):
            return len(self.items)==0
        def put(self, item, priority):
            heapq.heappush(self.items, (priority, item))
        def get(self):
            return heapq.heappop(self.items)[1]
    
    # Returns the Manhattan distance between node and target
    def get_heuristic(node):
        return abs(node[0] - target[0]) + abs(node[1] - target[1])

    # Get the graph we want to search
    passages_graph = maze_graph.get_graph(0)

    # Create priority queue and add source
    open = PriorityQueue()
    open.put(source, 0)

    # Need a visited and parent dictionay, and initialise both.
    visited = dict()
    parent = dict()
    for node in passages_graph.nodes():
        visited[node] = False
        parent[node] = (0,0)
    parent[source] = (-1,-1)
    visited[source] = True

    # Explore neighbors and queue with priority
    while not open.is_empty():
        current_node = open.get()
        for n in nx.neighbors(passages_graph, current_node):
            if not visited[n]:
                priority = get_heuristic(n)
                open.put(n, priority)
                visited[n] = True
                parent[n] = current_node
        if current_node == target:
            break
    
    # Create the path
    path = [target]
    parent_node = parent[target]
    while parent_node != (-1,-1):
        path.append(parent_node)
        parent_node = parent[parent_node]
    
    # Return the path and a list of visited nodes
    return (path, [n for n in visited.keys() if visited[n]])