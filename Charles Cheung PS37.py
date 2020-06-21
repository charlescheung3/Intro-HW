#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: March 10, 2020
#This program asks the user for a string, then counts and prints the number of characters that are uppercase letters, lowercase letters, numbers and special characters.

codeWord = input("Please enter a codeword:")
number = 0
upper = 0
lower = 0
special = 0

for i in codeWord:
    string = ord(i)
    if (48 <=string<=57):
        number = number +1
    elif (65 <=string<=90):
        upper = upper+1
    elif (97 <=string<=122):
        lower = lower+1
    else:
        special = special+1

print("Your codeword contains", upper,"uppercase letters,",lower,"lowercase letters,",number,"numbers",",and",special,"special characers.")
