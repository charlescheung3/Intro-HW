#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu  
#Date: March 03, 2020
#This  program displays shelter population over time to ask the user to specify the input file, ask the user to specify the output file, make a plot of the fraction of the total population that are single over time from the data in input file, and store the plot in the output file the user specified.

import pandas as pd
import matplotlib.pyplot as plt

inputfilename = input("Enter name of input file:")
outputfilename = input("Enter name of output file:")

homeless = pd.read_csv(inputfilename)
homeless["Fraction Single"] = homeless["Total Single Adults in Shelter"]/homeless["Total Individuals in Shelter"]
homeless.plot(x = "Date of Census", y = "Fraction Single")
plt.show()

fig = plt.gcf()
fig.savefig(outputfilename)
