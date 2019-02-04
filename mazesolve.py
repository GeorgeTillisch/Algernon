import daedalus
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from PIL import Image
from make_image import make_image
from make_graph import make_graph


def main():
    maze = daedalus.Maze(201,201)
    maze.create_perfect()
    print(maze.entrance, maze.exit)

    maze_array = np.array(list(maze))
    print(maze_array)

    img = make_image(maze_array)
    img.save('maze.png')

    g = make_graph(maze_array)

    g_nodes = list(g.nodes())
    start = g_nodes[0]
    end = g_nodes[len(g_nodes) - 1]
    path = nx.shortest_path(g, source=start, target=end)
    print(path)

    for point in path:
        maze_array[point] = 2

    img2 = make_image(maze_array)
    img2.save('maze_s.png')



if __name__ == '__main__':
    main()