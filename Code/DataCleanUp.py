# Cleaning up data 
import fiona
import shapefile as shp
import geopandas as gpd
import pandas as pd
import numpy as np
import os

### Combine shape files and school location information

# Read shape file
CBSA=gpd.read_file("/Users/sara/Desktop/MDST/education-deserts/RawData/tl_2017_us_cbsa/tl_2017_us_cbsa.shp")
CBSA.head() # Preview data

# Read school info data
SchoolNumber=pd.read_csv('~/Desktop/MDST/education-deserts/RawData/Colleges_and_Universities.csv')
SchoolNumber.head() # Preview data

# Transform SchoolNumber data as a GeoPandas Dataframe

gdf = gpd.GeoDataFrame(
    SchoolNumber, geometry=gpd.points_from_xy(SchoolNumber.X, SchoolNumber.Y))
gdf.head()

# We will ask the question is there at least more than one school within a particular polygon (point in polygon)?
# Yes--> Not education desert
# No --> Education desert

# Single case study:
CBSA.geometry.iloc[1,].contains(gdf['geometry'].iloc[1,])

# Make a copy because I'm going to drop points as I
# assign them to polys, to speed up subsequent search.
pts = gdf.copy() 
polygons=CBSA

# We're going to keep a list of how many points we find.
pts_in_polys = []

# Loop over polygons with index i.
for i, poly in polygons.iterrows():

    # Keep a list of points in this poly
    pts_in_this_poly = []

    # Now loop over all points with index j.
    for j, pt in pts.iterrows():
        if poly.geometry.contains(pt.geometry):
            print('started')
            # Then it's a hit! Add it to the list,
            # and drop it so we have less hunting.
            pts_in_this_poly.append(pt.geometry)
            pts = pts.drop([j])
            
            print('finished')

    # We could do all sorts, like grab a property of the
    # points, but let's just append the number of them.
    pts_in_polys.append(len(pts_in_this_poly))

# Add the number of points for each poly to the dataframe.
polygons['SchoolNumber'] = gpd.GeoSeries(pts_in_polys)

# Lets have a variable called 'EducationDesert', 0 = education desert, 1 = not an education desert based
# on the rule that less than two schools in a specific CBSAFP site is a desert.
polygons['EducationDesert']= polygons.SchoolNumber.apply(lambda set_: 1 if set_>2 else 0) 

# Save the updated polygon data set including information of our defenition of education desert in the clean data folder.
import os
import fiona; fiona.supported_drivers
os.chdir('/Users/sara/Desktop/MDST/education-deserts/CleanData') # Set to your own directory!
polygons.to_file('EducationDesertsByCBSA.shp')

### ELS data sets (in progress!)

Data1=pd.read_csv("~/Desktop/MDST/EducationDeserts_MDST/RawData/ELS_2002-12_PETS_v1_0_Other_CSV_Datasets/els_02_12_byf1sch_v1_0.csv")
Data2=pd.read_csv("~/Desktop/MDST/EducationDeserts_MDST/RawData/ELS_2002-12_PETS_v1_0_Other_CSV_Datasets/els_02_12_f2inst_v1_0.csv")
Data3=pd.read_csv("~/Desktop/MDST/EducationDeserts_MDST/RawData/ELS_2002-12_PETS_v1_0_Other_CSV_Datasets/els_02_12_f3inst_v1_0.csv")

Data1.head()
Data1.columns.values
Data2.head()
Data3.head()


# Force the first couple of columns as category.

# Rename student ID column so they match across data sets.
Data3.rename(columns={'Stu_ID': 'STU_ID'}, inplace=True)


# Combine the data 2, and pat of data 3 sets by 'STU_ID'
Combined1=pd.merge(Data2,Data3.loc[:,['STU_ID','F3ISTATE','F3IIPED']],on='STU_ID')
# Data dimensions overall
Combined1.shape

# 58341 rows and 51 columns
Combined1.head()

# Missing data?

# Separating out the features
x = df.loc[:, features].values

### Notes: F3PSLLVL stores the F3ILEVEL value from the sample member's 
# record on the ELS third follow-up student- institution file where 
# F3ILASTINST=1. See F3ILASTINST for further information regarding 
# identification of the respondent's last/currently attended 
# postsecondary institution.