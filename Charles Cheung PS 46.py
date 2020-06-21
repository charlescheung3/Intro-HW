#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: April 14, 2020
#This program asks the user for the name of a CSV file, name of the output file, and creates a map with markers for all the traffic collisions from the input file.

import folium
import pandas as pd

inputFile = input("Enter CSV file name:")
outputFile = input("Enter output file:")

collision = pd.read_csv(inputFile)

mapCollision = folium.Map(location=[40.75, -74.125], zoom_start=10)


for index,row in collision.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["TIME"]
    tiles="Cartodb Positron" 
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapCollision)

mapCollision.save(outputFile)
