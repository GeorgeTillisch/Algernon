import numpy as np
from PIL import Image


def make_image(maze_array):
    """
    Takes a 2D maze array and returns an RGB image with 
    black representing walls, white representing a passage, 
    and red representing a path.
    """
    
    data = np.zeros(
        (maze_array.shape[0], maze_array.shape[1], 3),
        dtype=np.uint8
    )

    for i in range(maze_array.shape[0]):
        for j in range(maze_array.shape[1]):
            if maze_array[i, j] == 0:
                data[i, j] = [255, 255, 255]
            elif maze_array[i, j] == 2:
                data[i, j] = [255, 0, 0]

    return Image.fromarray(data, 'RGB')
