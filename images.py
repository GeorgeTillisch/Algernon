import numpy as np
from PIL import Image


def make_image(maze_array):
    """Makes an image from a numpy array.

    Walls (1) are rendered black, passages (0) are rendered white,
    and paths (2) are rendered red.

    Args:
        maze_array: A 2D numpy array.

    Returns:
        A PIL image object in RGB.
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


def make_images(maze_array_list):
    """Makes a list of images from a list of numpy arrays

    Args:
        maze_array_list: A list of 2D numpy arrays.
    Returns:
        A list of PIL image objects.
    """
    images = []

    for maze_array in maze_array_list:
        images.append(make_image(maze_array))

    return images


def save_image(image, path, format='BMP'):
    """Saves an image to the specified path.

    Args:
        image: A PIL image object.
        path: A raw string with the path.
        format: Optional format, defaults to BMP. 
    """

    image.save(path, format=format)


def save_gif(image_list, path):
    """Saves an animated GIF.

    Args:
        image_list: A list of PIL image objects.
        path: A raw string with the path.
    """

    first_frame = image_list[0]
    first_frame.save(
        path,
        format='gif',
        save_all=True,
        append_images=image_list[1:],
        loop=0
    )
