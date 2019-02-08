import daedalus
import networkx as nx
import numpy as np

import images
import svgs
import graphs


PATH = 'imgs/'
FILENAME = 'maze'
SOLVED_EXTENSION = '_s'
IMG_EXTENSION = '.bmp'
SVG_EXTENSION = '.svg'


# TODO: Delete and implement different search algorithms
def simple_solve(maze_graph, start, end):
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
        self.maze_graph = graphs.make_passage_graph(self.maze_array)
        count = 0
        for p in self.maze_array[0]:
            if p == 0:
                start = (0, count)
                break
            count += 1
        count = 0
        for p in self.maze_array[-1]:
            if p == 0:
                end = (self.maze_array.shape[0] - 1, count)
                break
            count += 1
        path = simple_solve(self.maze_graph, start, end)
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
