#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: February 18, 2020
#This program will create a new image with that name and with the pixels colored blue depending on elevations


import numpy as np
import matplotlib.pyplot as plt

howblue = float(input("How blue is the ocean"))
outputname = input("What is the output file:")

elevations = np.loadtxt('elevationsNYC.txt')
              
mapShape = elevations.shape + (3,)


floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= -10:
            floodMap[row,col,0] = 0.2
            floodMap[row,col,1] = 0.2
            floodMap[row,col,2] = 0.2
        elif elevations[row,col] <= 0:
            floodMap[row,col,0] = 0
            floodMap[row,col,1] = 0
            floodMap[row,col,2] = howblue
        elif elevations[row,col]%10 == 0:
            floodMap[row,col,0] = 0
            floodMap[row,col,1] = 0
            floodMap[row,col,2] = 0
        else:
            floodMap[row,col,0] = 1.0   
            floodMap[row,col,1] = 1.0
            floodMap[row,col,2] = 1.0

plt.imshow(floodMap)
plt.show()

plt.imsave(outputname, floodMap)
