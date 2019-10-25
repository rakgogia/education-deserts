# Data exploration!
# Time to do some preliminary exploration on the data we created.

# Import relevant libraries
import fiona
import shapefile as shp
import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
from shapely.geometry import Point

# Lets start off with some SUPER simple maps.

SchoolNumber=pd.read_csv('~/Desktop/MDST/education-deserts/RawData/Colleges_and_Universities.csv')
EdDesertCBSA=gpd.read_file('/Users/sara/Desktop/MDST/education-deserts/CleanData/EducationDesertsByCBSA.shp')

# Make school number a geo data frame to plot and work with

points = SchoolNumber.apply(lambda row: Point(row.X, row.Y), axis=1)
SchNum = gpd.GeoDataFrame(SchoolNumber, geometry=points)
SchNum.crs = {'init': 'epsg:4326'}

SchNum.head()

fig, ax = plt.subplots()
ax=EdDesertCBSA.plot(color='white', edgecolor='black',ax=ax)
SchNum.geometry.plot(ax=ax, marker='o', color='red', markersize=.25)
plt.show()

# We should filter out the points that are outside of the US, i.e., with an X greater

SchNum.shape
# (7150, 46)
SchNum =SchNum[(SchNum.X < -50) & (SchNum.Y > 0)]
SchNum.shape # Removed the rows
# (7150, 46)

# Replot
fig, ax = plt.subplots()
ax=EdDesertCBSA.plot(color='white', edgecolor='black',ax=ax)
SchNum.geometry.plot(ax=ax, marker='o', color='red', markersize=.25)
plt.show()