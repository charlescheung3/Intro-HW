#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: February 18, 2020
#This program will make an octagon spiral

import turtle
charlie = turtle.Turtle()

turnsinput = int(input("Enter number of turns"))

for i in range (0,turnsinput,2):
    charlie.forward(i)
    charlie.right(45)

    
