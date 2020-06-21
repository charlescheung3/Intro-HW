#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: April 9, 2020
#This program takes as two parameters: the age group and the ticket type, and returns the price for admission to the American Museum of Natural History.

def computePrice(ageGroup, ticketType):
     """
     Takes as two parameters: the age group and the ticket type.
     Returns the AMNH admission price, as follows:
     If the ticket type is is "admission" and the age group is "adult", the price is $23.
     If the ticket type is is "admission" and the age group is  "child", the price is $13.
     If the ticket type is is "admission" and the age group is  "senior", the price is $18.
     If the ticket type is is "+exhibitions" and the age group is "adult", the price is $33.
     If the ticket type is is "+exhibitions" and the age group is  "child", the price is $20.
     If the ticket type is is "+exhibitions" and the age group is  "senior", the price is $27.
     """

     computePrice = -1
     
     if ticketType == "admission":
        if ageGroup == "adult":
            computePrice = 23
        elif ageGroup == "child":
            computePrice = 13
        elif ageGroup == "senior":
            computePrice = 18
        
     if ticketType == "+exhibitions":
        if ageGroup == "adult":
            computePrice = 33
        elif ageGroup == "child":
            computePrice = 20
        elif ageGroup == "senior":
            computePrice = 27

     return(float(computePrice))

def main():
     a = input('Enter the age group (child, adult, senior): ')
     t = input('Enter the ticket type (admission / +exhibitions): ').lower()
     price = computePrice(a,t)
     print('The price of your ticket is', price)

#Allow script to be run directly:
if __name__ == "__main__":
     main()
