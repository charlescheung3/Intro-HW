#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: February 18, 2020
#This program will color the region of the map with elevation greater than 6 feet and less than or equal 20 feet above sea level the color grey (50% red, 50% green, and 50% blue).

import numpy as np
import matplotlib.pyplot as plt

elevations = np.loadtxt('elevationsNYC.txt')

#Take the shape (dimensions) of the elevations
#  and add another dimension to hold the 3 color channels:
mapShape = elevations.shape + (3,)

#Create a blank image that's all zeros:
floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0:
            #Below sea level
           floodMap[row,col,2] = 1.0     #Set the blue channel to 100%
        elif elevations[row,col] <= 6:
            #Below the storm surge of Hurricane Sandy (flooding likely)
           floodMap[row,col,0] = 1.0     #Set the red channel to 100%
        elif elevations[row,col] <=20:
            floodMap[row,col,0:] = 0.5
        else:
            #Above the 6 foot storm surge and didn't flood
            floodMap[row,col,1] = 1.0   #Set the green channel to 100%

#Load the flood map image into matplotlib.pyplot:
plt.imshow(floodMap)

#Display the plot:
plt.show()

#Save the image:
plt.imsave('floodMap.png', floodMap)
