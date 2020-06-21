#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: April 12, 2020
#This program charts attendance over time for school attendance csv files

import pandas as pd
import matplotlib.pyplot as plt

inputFile = input("Enter name of input file:")
outputFile = input("Enter name of output file:")

attendance = pd.read_csv(inputFile)
attendance["Date"] = pd.to_datetime(attendance["Date"].apply(str))

attendance["% Absent"] = attendance["Absent"]/attendance["Enrolled"]*100
attendance.plot(x = "Date", y = "% Absent")
plt.show()

fig = plt.gcf()
fig.savefig(outputFile)
