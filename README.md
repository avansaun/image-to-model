# image-to-model
A Python project that converts a 2-dimensional image into a 3-dimensional .stl file for 3D printing. This is accomplished by using the scikit Python library to analyze the "darkness" of each pixel of the image and assigning a z-value to different regions of the image. Then, using the Python library stl, the regions will be convereted into 3D polygons that will form the final .stl model.

The end result should be a slightly 3-dimensional model (like a topographic map) that can be printed with a 3D printer.
