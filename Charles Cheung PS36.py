#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: March 10, 2020
#This program  should then print out the total number of permits in the file, the count of permits for each borough, and the five most popular locations (stored in the column: "Parking Held").

import pandas as pd

fileName = input("Enter file name:")

permits = pd.read_csv(fileName)

totalPermits = permits["EventID"].count()
boroughPermits = permits['Borough'].value_counts()

popLocation = permits["ParkingHeld"].value_counts()[:5]

print("There were", totalPermits, "film permits.")
print(boroughPermits)
print("The five most popular filming locations were", popLocation)
