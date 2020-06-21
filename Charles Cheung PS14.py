#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: February 11, 2020
#This program creates a university logo

import numpy as np
import matplotlib.pyplot as plt

img = np.ones((30,30,3))

img[:30,:10,0] = 1
img[:30,:10,1] = 0
img[:30,:10,2] = 0

img[20:30,:30,0] = 1
img[20:30,:30,1] = 0
img[20:30,:30,2] = 0

img[:30,20:30,0] = 1
img[:30,20:30,1] = 0
img[:30,20:30,2] = 0

plt.imshow(img)
plt.show()

plt.imsave('logo.png', img)
