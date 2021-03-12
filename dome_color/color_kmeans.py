# USAGE python color_kmeans.py --image Screenshot_10.png --clusters 3
# python3 color_kmeans.py --image images/jp.png --clusters 3

# import the necessary packages
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
from dome_color import utils
import cv2

# construct the argument parser and parse the arguments

# load the image and convert it from BGR to RGB so that
# we can dispaly it with matplotlib
image = cv2.imread('pic1.jpeg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# show our image 
plt.figure()
plt.axis("off")
plt.imshow(image)

# reshape the image to be a list of pixels
image = image.reshape((image.shape[0] * image.shape[1], 3))

# cluster the pixel intensities
clt = KMeans(n_clusters = 3)
clt.fit(image)

# build a histogram of clusters and then create a figure
# representing the number of pixels labeled to each color
hist = utils.centroid_histogram(clt)
bar = utils.plot_colors(hist, clt.cluster_centers_)

# show our color bart
plt.figure()

plt.axis("off")

plt.imshow(bar)
plt.savefig('test3.png')
#plt.show()
