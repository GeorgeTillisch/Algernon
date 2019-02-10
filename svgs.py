import svgwrite
import time

import graphs


def make_svg(height, width, maze_graph):
    """Makes an svg of a maze from a numpy array.

    Args:
        maze_array: A 2D numpy array.

    Returns:
        An svgwrite.Drawing object.
    """
    drawing = svgwrite.Drawing(size=(height, width), debug=False)

    command = 'M {0},{1} L {2},{3} '

    passage_path = svgwrite.path.Path(fill='none', stroke='white', stroke_linejoin='miter', stroke_linecap='square', transform='translate(0.5 0.5)')
    for edge in maze_graph.get_graph(0).edges():
        passage_path.push(command.format(edge[0][1], edge[0][0], edge[1][1], edge[1][0]))
    drawing.add(passage_path)

    wall_path = svgwrite.path.Path(fill='none', stroke='black', stroke_linejoin='miter', stroke_linecap='square', transform='translate(0.5 0.5)')
    for edge in maze_graph.get_graph(1).edges():
        wall_path.push(command.format(edge[0][1], edge[0][0], edge[1][1], edge[1][0]))
    drawing.add(wall_path)

    if len(maze_graph.get_graph(2).edges()) > 0:
        path_path = svgwrite.path.Path(fill='none', stroke='red', stroke_linejoin='miter', stroke_linecap='square', transform='translate(0.5 0.5)')
        for edge in maze_graph.get_graph(2).edges():
            path_path.push(command.format(edge[0][1], edge[0][0], edge[1][1], edge[1][0]))
        drawing.add(path_path)

    return drawing


def save_svg(drawing, path):
    """Saves an svg to the specified path.

    Args:
        drawing: An svgwrite.Drawing object.
        path: A raw string with the path.
    """
    print(drawing.debug)
    t1 = time.time()
    drawing.saveas(path)
    print(time.time() - t1)