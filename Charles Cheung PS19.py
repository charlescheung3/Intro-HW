#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: February 18, 2020
#This program will manipulate turtles to stamp alternating in a spiral

import turtle


commander = int(input("Please enter the number of turtle stamps:"))

charlie = turtle.Turtle()
charlie.shape('turtle')
charlie.penup()
steps = 20

for i in range(commander):
    charlie.stamp()
    steps = steps + 2
    charlie.forward(steps)
    charlie.right(24)
    

