#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: April 14, 2020
#This program makes a turtle walk 100 times. Each "walk" is 20 steps forward and the turtle can turn 0, 5, 10, 15,..., 360 degrees (chosen randomly) at the beginning of each walk.

import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

for i in range(100):
  trey.forward(20)
  a = random.randrange(0,360,5)
  trey.right(a)
