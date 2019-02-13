import daedalus
import networkx as nx
import numpy as np

import images
import svgs
import graphs


PATH = 'imgs/'
FILENAME = 'maze'
SOLVED_EXTENSION = '_s'

SOLVE_TYPES = {'bfs':graphs.solve_bfs, 'gbfs':graphs.solve_gbfs, 'astar':graphs.solve_astar}

# TODO: Remove magic numbers.
class Solver:
    """Class for handling maze solving and output"""

    def __init__(self, maze_rows, maze_cols, output, solvetype):
        self.maze = daedalus.Maze(maze_rows, maze_cols)
        self.maze.create_perfect()

        self.height = maze_rows
        self.width = maze_cols

        self.maze_arrays = [np.array(list(self.maze))]
        self.maze_graph = graphs.MazeGraph(self.maze_arrays[0])

        self.source, self.target = self.get_source_and_target()

        self.solvetype = solvetype
        self.solved = False

        self.output = output
        self.steps = False
        if output == 'gif':
            self.steps = True

    def reset(self):
        self.maze.create_perfect()
        self.maze_arrays = [np.array(list(self.maze))]
        self.maze_graph = graphs.MazeGraph(self.maze_arrays[0])
        self.solved = False

    def solve(self):
        if self.solved:
            self.reset()
        path, visited = SOLVE_TYPES.get(self.solvetype)(self.maze_graph, self.source, self.target)
        self.update_maze_arrays(path, visited)
        self.maze_graph.update_graphs(self.maze_arrays[0])
        self.solved = True

    def save_state(self):
        if self.output == 'bmp' or self.output == 'png':
            if self.solved:
                path = PATH + FILENAME + '_' + self.solvetype + SOLVED_EXTENSION + '.' + self.output
            else:
                path = PATH + FILENAME + '_' + self.solvetype + '.' + self.output
            img = images.make_image(self.maze_arrays[0])
            images.save_image(img, path, self.output)
        elif self.output == 'svg':
            if self.solved:
                path = PATH + FILENAME + '_' + self.solvetype + SOLVED_EXTENSION + '.' + self.output
            else:
                path = PATH + FILENAME + '_' + self.solvetype + '.' + self.output
            drawing = svgs.make_svg(self.height, self.width, self.maze_graph)
            svgs.save_svg(drawing, path)
        elif self.output == 'gif':
            if not(self.solved): # Gif output only makes sense when solved with steps.
                self.solve()
            imgs = images.make_images(self.maze_arrays)
            path = PATH + FILENAME + '_' + self.solvetype + '.' + self.output
            images.save_gif(imgs, path)

    def get_source_and_target(self):
        maze_array = self.maze_arrays[0]
        for x, y in enumerate(maze_array[0]):
            if y == 0:
                source = (0, x)
        last_row = maze_array.shape[0] - 1
        for x, y in enumerate(maze_array[last_row]):
            if y == 0:
                target = (last_row, x)
        return (source, target)

    def update_maze_arrays(self, path, visited):
        if not self.steps:
            for p in path:
                self.maze_arrays[0][p] = 2
        else:
            current_array = np.copy(self.maze_arrays[0])
            for v in sorted(visited):
                current_array[v] = 3
                self.maze_arrays.append(np.copy(current_array))
            for p in path:
                current_array[p] = 2
                self.maze_arrays.append(np.copy(current_array))

