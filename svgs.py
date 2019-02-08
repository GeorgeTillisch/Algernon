import svgwrite

import graphs


def make_svg(maze_array):
    height = maze_array.shape[0]
    width = maze_array.shape[1]
    drawing = svgwrite.Drawing(size=(height, width))

    sections = graphs.make_section_graphs(maze_array)

    passage_path = svgwrite.path.Path(fill='none', stroke='white', stroke_linejoin='miter', stroke_linecap='square', transform='translate(0.5 0.5)')
    for edge in sections[0].edges():
        command = f'M {edge[0][1]},{edge[0][0]} L {edge[1][1]},{edge[1][0]}'
        passage_path.push(command)
    drawing.add(passage_path)

    wall_path = svgwrite.path.Path(fill='none', stroke='black', stroke_linejoin='miter', stroke_linecap='square', transform='translate(0.5 0.5)')
    for edge in sections[1].edges():
        command = f'M {edge[0][1]},{edge[0][0]} L {edge[1][1]},{edge[1][0]}'
        wall_path.push(command)
    drawing.add(wall_path)

    if len(sections[2].edges()) > 0:
        path_path = svgwrite.path.Path(fill='none', stroke='red', stroke_linejoin='miter', stroke_linecap='square', transform='translate(0.5 0.5)')
        for edge in sections[2].edges():
            command = f'M {edge[0][1]},{edge[0][0]} L {edge[1][1]},{edge[1][0]}'
            path_path.push(command)
        drawing.add(path_path)

    return drawing


def save_svg(drawing, path):
    """Saves an svg to the specified path.

    Args:
        drawing: An svgwrite.Drawing object.
        path: A raw string with the path.
    """
    drawing.saveas(path)