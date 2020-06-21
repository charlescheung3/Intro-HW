#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: March 10, 2020
#This program given the 'Stars' dataset will do the following: Ask the user for the name of the input file, ask the user for the name of the star type, and print the radii of the largest and the smallest star for the given star type.

import pandas as pd

fileName = input("Enter file name:")
starType = input("Enter the name of the star type:")

sky = pd.read_csv(fileName)
bigStar = sky.groupby('Star type').get_group(starType).max()['Radius(R/Ro)']
smolStar = sky.groupby('Star type').get_group(starType).min()['Radius(R/Ro)']

print("The radius of the largest", starType, "is", bigStar)
print("The radius of the smallest", starType, "is", smolStar)
