import svgwrite


# TODO: Re-implement to make smaller svg files, possibly render from graph.
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
        j = 0
        length = 0
        while j != width:
            if j + 1 < width and maze_array[i, j] == maze_array[i, j + 1]:
                length += 1
            else:
                value = maze_array[i, j]
                if value == 0:
                    color = 'white'
                elif value == 1:
                    color = 'black'
                elif value == 2:
                    color = 'red'

                if length == 0:
                    drawing.add(
                        svgwrite.shapes.Rect((j,i), fill=color)
                    )
                else:
                    drawing.add(
                        svgwrite.shapes.Rect((j - length,i), (length + 1, 1) , fill=color)
                    )
                length = 0
            j += 1
    
    return drawing


def save_svg(drawing, path):
    """Saves an svg to the specified path.

    Args:
        drawing: An svgwrite.Drawing object.
        path: A raw string with the path.
    """
    drawing.saveas(path)