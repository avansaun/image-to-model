import numpy as np
from skimage import io
from array import *
#from stl import mesh

img = io.imread('sus.png')

# define image boundaries
imgDimensions = img.shape
iWidth = imgDimensions[0]
iHeight = imgDimensions[1]
x = 0
y = 0

# init new numpy array
#meshData = np.array([])
#for x in y:
    #a = np.append(a, x)

pixelColors = [[]]
# loop through all pixels in the image and store in 2D array
for y in range(0,iHeight):
    for x in range(0, iWidth):
        #print(img[x,y])
        pixelColors.insert(y, img[x,y])
        x += 1
    y += 1

# TODO: Use numpy-stl to feed the data to and create an STL file
# (note: I think I could do something like the height of each layer in the STL file would be
# pixel color brightness value / 25, so something like 100 darkness/25 = 4mm high in the model)


print(f"Color values at pixel (125,125) are {img[125, 125]}")