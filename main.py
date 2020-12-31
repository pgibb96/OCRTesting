import matplotlib.pyplot as plt

import os
import skimage

from skimage import io, data
from skimage.color import rgb2gray, rgba2rgb
from skimage.filters import threshold_mean

sudokus = []
directory = "./images/"
for filename in os.listdir(directory):
    sudokus.append(os.path.join(directory, filename))

for sudoku in sudokus:
    temp = io.imread(sudoku)
    grayscale = rgb2gray(rgba2rgb(temp))
    thresh = threshold_mean(grayscale)
    binary = grayscale > thresh
    io.imshow(binary)
    io.show()
