#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: February 11, 2020
#This program asks the user for a message and then prints the message out, five copies of each character per line surrounded by three stars '***' on each side.

Enterhere = input("Enter a message:")

for i in Enterhere:
        print("*** "+i+" "+i+" "+i+" "+i+" "+i+" ***")
