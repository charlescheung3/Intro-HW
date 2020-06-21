#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: February 11, 2020
#This program demonstrates a shade of purple

import turtle

turtle.colormode(255)		#Allows colors to be given as 0...255
tess = turtle.Turtle()		#Create a turtle
tess.shape("turtle")		#Make it turtle shaped
tess.backward(100)		#Move her backwards, to give more space to draw

                                #For 0,10,20,...,250
for i in range(0,255,10):
     tess.forward(10)		#Move forward
     tess.pensize(i)		#Set the drawing size to be i (larger each time)
     tess.color(i,0,i)		#Set the red and blue channel to be i (brighter each time)
