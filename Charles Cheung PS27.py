#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: February 25, 2020
#This program should ask the user for the borough, an name for the output file, and then display the fraction of the population that has lived in that borough, over time.

#Libraries for plotting and data processing:
import matplotlib.pyplot as plt
import pandas as pd

boroughname = input("Enter borough name")
outputname = input("Enter output file name")

#Open the CSV file and store in pop
pop = pd.read_csv('nycHistPop.csv',skiprows=5)

#Compute the fraction of the population in the Bronx, and save as new column:
pop['Fraction'] = pop[boroughname]/pop['Total']

#Create a plot of year versus fraction of pop. in Bronx (with labels):
pop.plot(x = 'Year', y = 'Fraction')


#Save to the file:  fractionBX.png
fig = plt.gcf()
fig.savefig(outputname)
