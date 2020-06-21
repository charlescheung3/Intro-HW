#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: February 18, 2020
#This program will print a list of names with an abbreviated initial for the first name

names = input("Please enter your list of names")

sever = names.split(", ")

for i in sever:
    abbrev = i.split(" ")
    print(abbrev[1][0]+".", abbrev[0])
    
