import matplotlib.pyplot as plt
from skimage import data, filters
from skimage.color import rgb2gray
from FileUtil import load_image


def convert_rgb_to_gray(rgb_image):
    """load the image data from an image path

    :param rgb_image: the rgb image
    :type rgb_image: numpy.array
    :returns: the gray image
    :rtype: numpy.array

    """
    return rgb2gray(rgb_image)