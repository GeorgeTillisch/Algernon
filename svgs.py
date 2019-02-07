import svgwrite


def make_svg(maze_array):
    """Makes an svg from a numpy array.

    Walls (1) are rendered black, passages (0) are rendered white,
    and paths (2) are rendered red.

    Args:
        maze_array: A 2D numpy array.

    Returns:
        An svgwrite.Drawing object.
    """
    height = maze_array.shape[0]
    width = maze_array.shape[1]
    drawing = svgwrite.Drawing(size=(height, width))

    for i in range(height):
        for j in range(width):
            if maze_array[i, j] == 0:
                color = 'white'
            elif maze_array[i, j] == 1:
                color = 'black'
            elif maze_array[i, j] == 2:
                color = 'red'
            drawing.add(
                svgwrite.shapes.Rect((j,i), fill=color)
            )
    
    return drawing


def save_svg(drawing, path):
    """Saves an svg to the specified path.

    Args:
        drawing: An svgwrite.Drawing object.
        path: A raw string with the path.
    """
    drawing.saveas(path)