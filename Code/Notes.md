# NOTES

Running code requires:
-   Python3.7.3 64 bit 
-   Install packages: geopandas, fiona and shapely
-   Code was developed on MacOS --may need to tweak for other platforms such as windows.

Before combining GIS data it is important to check the data's datum and projection. 
These should be the same, or you will have some small to huge error important to data
visualization and analysis.

The 'DataExploratory.py' file includes code for preliminary data exploration. _Note_
the two figure maps below, before and after excluding some points in the far west extent.
Many coordinates at sea should not be there. This is probably due to combining GIS data that
_i.e.,_ use different geographic coordinates and should be corrected!


![](/Users/sara/Desktop/MDST/education-deserts/Figures/Map1_prelim_EdDes_CBSA.jpg)

![](/Users/sara/Desktop/MDST/education-deserts/Figures/Map2_prelim_EdDes_CBSA.jpg)
