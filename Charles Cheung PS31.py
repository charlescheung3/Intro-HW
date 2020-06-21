#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: February 25, 2020
#This program takes a string as input and uses that string to control what the turtle draws on the screen (inspired by code.org's graph paper programming). Currently, the program processes the following commands:

import turtle

charlie = turtle.Turtle()

turtlecommands = str(input("Enter commands here"))

for command in turtlecommands:
    
    if command == 'F':
        charlie.forward(50)
    elif command == 'L':
        charlie.left(90)
    elif command == 'R':
        charlie.right(90)
    elif command == '^':
        charlie.penup()
    elif command == 'v':
        charlie.pendown()
    elif command == 'r':
        charlie.color('red')
    elif command == 'g':
        charlie.color('green')
    elif command == 'b':
        charlie.color('blue')
    elif command == 'S':
        charlie.stamp()
    elif command == 'D':
        charlie.dot()
    elif command == 'B':
        charlie.backward(50)
    else :
        charlie.color('purple')
