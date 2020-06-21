#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: Juanuary, 31 2020
#This program draws a vortex

import turtle

tess = turtle.Turtle ()

for i in range (150):

    tess.forward (0.5*i)
    tess.penup ()
    tess.forward (0.5*i)
    tess.pendown ()
    tess.left (110)
        
