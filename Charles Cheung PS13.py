#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: February 11, 2020
#This program puts a green filter over the image

#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

userinput = input("Enter name of the input file:")
useroutput = input("Enter name of the output file:")

img = plt.imread(userinput)   #Read in image from csBridge.png
plt.imshow(img)		           #Load image into pyplot
plt.show()                         #Show the image (waits until closed to continue)

img2 = img.copy()        #make a copy of our image
img2[:,:,0] = 0          #Set the red channel to 0
img2[:,:,2] = 0           #Set the blue channel to 0

plt.imshow(img2)         #Load our new image into pyplot
plt.show()               #Show the image (waits until closed to continue)

plt.imsave(useroutput, img2)  #Save the image we created to the file: reds.png
