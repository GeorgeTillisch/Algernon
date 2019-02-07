import daedalus
import networkx as nx
import numpy as np

import images
import svgs

PATH = 'imgs/'
FILENAME = 'maze'
SOLVED_EXTENSION = '_s'
IMG_EXTENSION = '.bmp'
SVG_EXTENSION = '.svg'


def make_graph(maze_array):
    """Makes a networkx graph from a numpy array.

    Args:
        maze_array: A 2D numpy array.

    Returns:
        A networkx Graph object with passages in the maze
        represented as nodes joined by edges.
    """

    maze_graph = nx.Graph()

    for i in range(maze_array.shape[0]):
        for j in range(maze_array.shape[1]):
            if maze_array[i, j] == 0:
                maze_graph.add_node((i, j))

    nodes = maze_graph.nodes()

    for node in nodes:
        below = (node[0]+1, node[1])
        left = (node[0], node[1] - 1)
        right = (node[0], node[1] + 1)
        if below in nodes:
            maze_graph.add_edge(node, below)
        if left in nodes:
            maze_graph.add_edge(node, left)
        if right in nodes:
            maze_graph.add_edge(node, right)

    return maze_graph


# TODO: Delete and implement different search algorithms
def simple_solve(maze_graph):
    nodes = list(maze_graph.nodes())
    start = nodes[0]
    end = nodes[len(nodes) - 1]
    path = nx.shortest_path(maze_graph, source=start, target=end)
    return path


class Solver():
    """Class for handling maze solving and output"""

    def __init__(self, maze_rows, maze_cols):
        self.maze = daedalus.Maze(maze_rows, maze_cols)
        self.maze.create_perfect()
        self.maze_array = np.array(list(self.maze))
        self.maze_graph = nx.Graph()
        self.solved = False

    def reset(self):
        self.maze.create_perfect()
        self.maze_array = np.array(list(self.maze))
        self.maze_graph = nx.Graph()
        self.solved = False

    def solve(self, solvetype='simple'):
        self.maze_graph = make_graph(self.maze_array)
        path = simple_solve(self.maze_graph)
        for p in path:
            self.maze_array[p] = 2
        self.solved = True

    def save_state(self, output='i'):
        if output == 'i':
            img = images.make_image(self.maze_array)
            if self.solved:
                path = PATH + FILENAME + SOLVED_EXTENSION + IMG_EXTENSION
            else:
                path = PATH + FILENAME + IMG_EXTENSION
            images.save_image(img, path)
        elif output == 'svg':
            drawing = svgs.make_svg(self.maze_array)
            if self.solved:
                path = PATH + FILENAME + SOLVED_EXTENSION + SVG_EXTENSION
            else:
                path = PATH + FILENAME + SVG_EXTENSION
            svgs.save_svg(drawing, path)
