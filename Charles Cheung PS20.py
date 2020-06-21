#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: February 18, 2020
#This program will ask the user for the size of your image, the name of the output file, and create a .png file of stripes.

import matplotlib.pyplot as plt
import numpy as np

imgsize = input("Enter the size:")
outputfile = input("Enter output file:")

img = np.ones((int(imgsize),int(imgsize),3))

img[:,::2,2] = 1
img[:,::2,1] = 0
img[:,::2,0] = 0

plt.imshow(img)
plt.show

plt.imsave(outputfile, img)
