#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: February 25, 2020
#This is a program that computes the minimum, maximum, average and standard deviation of the population over time for a borough (entered by the user). Your program should assume that the NYC historical population data file, nycHistPop.csv is in the same directory.

#Libraries for plotting and data processing:
import matplotlib.pyplot as plt
import pandas as pd

#Open the CSV file and store in pop
pop = pd.read_csv('nycHistPop.csv',skiprows=5)

enterborough = input("Enter borough:")

print("Minimum population:", pop[enterborough].min())
print("Maximum population:", pop[enterborough].max())
print("Average population:", pop[enterborough].mean())
print("Standard deviation:", pop[enterborough].std())
