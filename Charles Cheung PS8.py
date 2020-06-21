#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: February 04, 2020
#This program prints the user input backwards

Typehere = input("Enter message here")

for i in range(len(Typehere)-1,-1,-1):
    print(Typehere[i], end='')

