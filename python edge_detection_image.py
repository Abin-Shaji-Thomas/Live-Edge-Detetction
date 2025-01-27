# import libraries of python OpenCV
# where its functionality resides
import cv2

# np is an alias pointing to numpy library
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('test.jpg')    

# finds edges in the input image and
# marks them in the output map edges
edges = cv2.Canny(image,100,200)

# plot the original image
plt.subplot(121),plt.imshow(image,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

# plot the Edge image
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()