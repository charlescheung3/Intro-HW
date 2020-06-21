#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: April 14, 2020
#This program uses folium to create a map of NY with a marker for Hunter College

import folium
import pandas as pd

mapCUNY = folium.Map(location=[40.75, -74.125], zoom_start=10)
folium.Marker(location = [40.768731, -73.964915], popup = "Hunter College").add_to(mapCUNY)

mapCUNY.save(outfile='nycMap.html')
