#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: February 18, 2020
#This program will tell you how many coins your cents input will return

centsinput = int(input("Enter number of cents as an integer"))

quarters = centsinput // 25
print("Quarters:", quarters)

rem = centsinput % 25
dimes = rem // 10
print("Dimes:", dimes)

rem = rem % 10
nickels = rem // 5
print("Nickels:", nickels)

cents = rem % 5
print("Cents:", cents)
    


            
