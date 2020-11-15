from matplotlib import image
import numpy as np
from enum import Enum
from os import path


# decorator to check the input file
def check_file_valid(ext=None):
    def check_path_exist(func):
        def function_wrapper(*args, **kwargs):
            if not path.exists(args[0]):
                print("The specified file " + args[0] + " does not exist")
                raise FileNotFoundError
            if ext is not None:
                if not args[0].endswith(ext):
                    print("The file is not a valid " + ext + " file")
                    raise Exception("File type not valid")
            return func(*args, **kwargs)
        return function_wrapper
    return check_path_exist


class GEOMETRY(Enum):
    POINTS = 1
    MESH = 2


@check_file_valid("jpg")
def load_image(image_path):
    """load the image data from an image path

    :param image_path: image file path
    :type image_path: str
    :returns: the image data(width, height, rgb)
    :rtype: numpy.array

    """
    return image.imread(image_path)


@check_file_valid("off")
def load_geometry_from_object_file_format(off_file_path, geometry_type=GEOMETRY.POINTS):
    """load the geometry data from an image path

    :param off_file_path: off file path
    :type off_file_path: str
    :param geometry_type: the type of geometry to be load
    :type geometry_type: Enum
    :returns: the geometry data(Points or Mesh)

    """
    with open(off_file_path, 'r') as reader:
        # check if it is valid .off format
        if reader.readline().rstrip() != "OFF":
            return
        # get the vertex, face, edge count
        vertex_count, face_count, edge_count = [int(i) for i in reader.readline().split()]
        contents = reader.readlines()
        # the points coordinates starts from the 3rd line
        points = np.array([line.split() for line in contents[3:vertex_count]], dtype=np.float)
        if geometry_type == GEOMETRY.POINTS:
            return points
        else:
            print("Not supported yet")
            return
