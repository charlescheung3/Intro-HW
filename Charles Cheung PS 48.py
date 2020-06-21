#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: April 14, 2020
#This program repeatedly asks the user to enter a number as long as the cumulative average of these numbers is less than 50.


runningtotal = 0
numberterms = 0

while numberterms == 0 or runningtotal/numberterms < 50:
    runningtotal = runningtotal + int(input('Please enter number: '))
    numberterms = numberterms + 1    
print('The average is', runningtotal/numberterms)
