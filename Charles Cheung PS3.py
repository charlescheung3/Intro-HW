#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: January 30, 2020
#This program will have a pink background color and have tess draw a blue square and alex draw a triangle

import turtle
screen = turtle.Screen()             # Set up the window and its attributes
screen.bgcolor("pink")


tess = turtle.Turtle()           # create tess and set some attributes
tess.color("blue")
tess.pensize(5)

alex = turtle.Turtle()           # create alex

for i in range (4):          # complete the triangle
    tess.forward(80)
    tess.left(90)
    
tess.right(180)                  # turn tess around
tess.forward(100)                 # move her away from the origin

for i in range (3):
    alex.forward(50)                 # make alex draw a square
    alex.left(120)

screen.exitonclick()
