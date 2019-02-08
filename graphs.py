import networkx as nx


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
            if value != 0: # Only add eges for passages
                continue
            below = (i + 1, j)
            left = (i, j - 1)
            right = (i, j + 1)
            current = (i, j)
            if (i + 1) < height and value == maze_array[below]:
                passage_graph.add_edge(current, below)
            if (j - 1) >= 0 and value == maze_array[left]:
                passage_graph.add_edge(current, left)
            if (j + 1) < width and value  == maze_array[right]:
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
    values = {0:passage_graph, 1:wall_graph, 2:path_graph}

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

    return [passage_graph, wall_graph, path_graph]