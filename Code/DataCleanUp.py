# Cleaning up data 

import shapefile as shp
import geopandas as gpd
import pandas as pd
import numpy as np
import os



gpd.read_file("~/Desktop/MDST/RawData/tl_2017_us_cbsa/tl_2017_us_cbsa.shp")
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



# PCA preliminary


# 1- Use the data set 3
# 2- Remove NA's
# 3- Subset numerical data features and make F3I Level a category
# 3- Scale the data ^
# 4- Run PCA on scaled subset
# 5- Visualize the loading values per PC
# 6- Visualize individual PC's colored by F3I level, for PC1 and PC2

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Separating out the features
x = df.loc[:, features].values

### Notes: F3PSLLVL stores the F3ILEVEL value from the sample member's 
# record on the ELS third follow-up student- institution file where 
# F3ILASTINST=1. See F3ILASTINST for further information regarding 
# identification of the respondent's last/currently attended 
# postsecondary institution.