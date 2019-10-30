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
EdDesertCBSA=gpd.read_file('/Users/sara/Desktop/MDST/education-deserts/CleanData/Shape_EducationDesertsCBSA/EducationDesertsByCBSA.shp')

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

# Sum up the education desert and non ed desert
DesertSum=pd.DataFrame(EdDesertCBSA.EducationD.value_counts())
DesertSum

# 605 deserts!
# 340 non deserts!

# Plot
DesertSum.plot(kind='bar')
plt.xlabel("Education desert binary", labelpad=14)
plt.ylabel("Counts", labelpad=14)
plt.title("Count of Education Deserts by CBSA", y=1.02);
plt.show()


# Read in income data
GDP=pd.read_csv('~/Desktop/MDST/education-deserts/CleanData/gdp_metro0918.csv')

# Read GEO id information
IDinfo=pd.read_csv('~/Desktop/MDST/education-deserts/CleanData/Core_GEO_ID_2017.csv', encoding = "ISO-8859-1")
IDinfo.head()
IDinfo.columns.values
GDP.head()

EdDesertCBSA.head()

# Check that the CBSA code in ID information matches the CBSA code of Ed desert data
IDinfo['CBSA Code'].isin(EdDesertCBSA.CBSAFP) # They match!

# Rename the CBSA Code to 'CBSAFP'
IDinfo.rename(columns={'CBSA Code': 'CBSAFP'}, inplace=True)
IDinfo.CBSAFP=IDinfo.CBSAFP.astype(int).astype('category')
EdDesertCBSA.CBSAFP=EdDesertCBSA.CBSAFP.astype(int).astype('category')

# Check that the CBSA code in ID information matches the CBSA code of Income  data
IDinfo['CBSA_Title'].isin(GDP.CBSA_Title) # Some match!

# Let merge some data now

# Combine desert polygon data with geo info data
EdDesertCBSA_2=EdDesertCBSA.merge(IDinfo[['CBSAFP','CBSA_Title']], on='CBSAFP')

# Combine GDP data with polygon desert data
EdDesertCBSA_2=EdDesertCBSA_2.merge(GDP, on='CBSA_Title')

# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #
# # Visualize data depending on whether it is an education desert


# Make a categorical variable out of the binary education desert info
EdDesertCBSA_2['EducationDesert']=EdDesertCBSA_2.EducationD.apply(lambda set_: 'Desert' if set_==0 else "NotDesert")

# pivot and plot
EdDesertCBSA_2.pivot(columns="EducationDesert", values="PerChangeGDP").plot.hist(bins=100, alpha = 0.5)
plt.xlabel("GDP change %", labelpad=14)
plt.title("Percent change in real GDP by metropolitan area",y=1.02)
plt.show()

# Plot education deserts and NON education deserts

fig, ax = plt.subplots(figsize=(14, 6))

fig=EdDesertCBSA_2[EdDesertCBSA_2.EducationD==0].plot(color="yellow",ax=ax) # Plot deserts yellow
EdDesertCBSA_2[EdDesertCBSA_2.EducationD==1].plot(color="lightblue",ax=ax) # Plot non deserts blue
ax.set_title('Education Deserts in the US Based on CBSA',fontdict={'fontsize': '25','fontweight': '3'}) # add title
ax.annotate('Data source: shape.file from TIGER.gov',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='black') # add data source

plt.show()

# Pairwise correlation between variables
# Seaborn visualization library
import seaborn as sns# Create the default pairplot

Subset=pd.DataFrame(EdDesertCBSA_2[['PerChangeGDP', 'NatResMining', 'Constr', 'DurGoManu','NonGoodManu', 'Trade', 'TransUtil','EducationDesert']])
       
sns.pairplot(Subset,hue='EducationDesert')

plt.show()



# Plot map chloropleth by GDP and then school points on top.
StatesShape = gpd.read_file("/Users/sara/Desktop/MDST/education-deserts/CleanData/states_21basic/states.shp")
StatesShape.head()

fig, ax = plt.subplots(figsize=(14, 6))
## first layer, all geometries included 
fig=StatesShape.plot(color="lightgrey",ax=ax) # Plot the US as grey
EdDesertCBSA_2.plot(ax=ax,column='PerChangeGDP',scheme="quantiles",legend=True,legend_kwds={'loc': 'lower left'}) # Fill in states with information by amount of pesticide applied, NOTE LEGEND LOCATION SPECIFIED HERE
SchNum.plot(ax=ax,color='red',markersize=0.1)

plt.show()

# PCA 

EdDesertFull=EdDesertCBSA_2.dropna()

from sklearn.preprocessing import StandardScaler
features = ['PerChangeGDP', 'NatResMining', 'Constr', 'DurGoManu',
       'NonGoodManu', 'Trade', 'TransUtil', 'Info',
       'FinInsRealEstRentLea', 'ProBusiServi', 'EdSerHealthSociAs',
       'ArtEntRec', 'OtherServices', 'Govern']# Separating out the features
x = EdDesertFull.loc[:, features].values# Separating out the target
y = EdDesertFull.loc[:,['EducationDesert']].values# Standardizing the features
x = StandardScaler().fit_transform(x)


from sklearn.decomposition import PCA
pca =PCA(n_components=3)
principalComponents = pca.fit_transform(x)

principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2','principal component 3'])

finalDf = pd.concat([principalDf, EdDesertFull[['EducationDesert']]], axis = 1)

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 

ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)
targets = ['Desert', 'NotDesert']
colors = ['b','orange']

for target, color in zip(targets,colors):
    indicesToKeep = finalDf['EducationDesert'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid('off')

plt.show()


var= pca.explained_variance_ratio_


#Explained variance
pca = PCA().fit(x)
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('number of components')
plt.ylabel('cumulative explained variance')
plt.show()

### Linear regression modeling
