#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: February 04, 2020
#This program prints an encryted word with each letter 16 letters away from the original letter of the word


Typehere=input("Type Here")
codedmessage=""


for ch in Typehere:
    
    offset=ord(ch)-ord("a")+16
    wrap=offset%26
    newchar = chr(ord("a")+wrap)
    codedmessage=codedmessage+newchar
    
print(codedmessage)
