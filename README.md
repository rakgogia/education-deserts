# README 

Here is our folder of the MDST Project, 'Education deserts'. Background and information of subfolders is provided below.

All analysis were carried out in **Python 3.7.3 64-bit**

# Background
“Education Deserts” are places far from post-secondary educational institutions, where “college opportunities are few and far between”. In this paper from researchers at UW-Madison, education deserts are defined as places with either of these two conditions:

Zero colleges or universities are located nearby, or one community college is the only public broad-access institution nearby.

It seems (and may even be obvious) that geography plays a huge role in people’s educational pursuits and decisions, even in a digital, globally connected world. After all, we attend a huge state university with a large impact on its surrounding community. But just how large an impact does it make?

## Background reading
See pdf file, 'Klasik et al. - 2018 - Out of the Education Desert How Limited Local Col.pdf'


## Clean Data
The clean data folder has any processed version of the 'Raw Data', such as filtered and merged datasets. 

#### GDP 		

-   gdp_metro0918.csv Table 3. Contributions to Percent Change in Real Gross Domestic Product (GDP) by Metropolitan Area, 2017*	
**KEY** 
* = Advance statistics														
Source: U.S. Bureau of Economic Analysis	
													
(D) Not shown to avoid disclosure of confidential information, but the estimates for this item are included in the totals.				

#### Education desert polygon data
-   Shape_EducationDesertsCBSA _Shapefiles created after combining school and college data with the CBSA data.

## Code
The python code used to process and analyze the data. 

-   DataCleanUp.py _data cleaning code_

-   DataExploration.py _preliminary data exploration_

## Figures
The figure images that will be used for presentations etc.


## Notes
In this folder are a series of markdown files with notes on the work pipeline for the Education Desert Project. The idea behind this is to provide a week to week pipeline so people 'trickling' in and out of the project can easliy follow along--also, it ensures reproduciblity.

- Week 1: Work on setting up a GitHub for the Education Desert Project. Set general goals for the semester, and links related to the former as need be (e.g., wikipages on exploratory data analysis).

## Raw Data
In this folder is the raw data prior to any processing (e.g., remove 'NAs', data merging).

### ELS data set

Source: Downloaded from link:
    This is data from Education Longitudinal Study of 2002, more information here https://catalog.data.gov/dataset/education-longitudinal-study-of-2002.

General information can be found here: https://catalog.data.gov/dataset/education-longitudinal-study-of-2002

 #### F2Student‐InstitutionFil (attendedandapplied‐toasofF2
-   els_02_12_f2inst_v1_0.csv
    -   MetaData: Student_institution-F2.pdf

#### Education Longitudinal Study of 2002, High School Sophomores (ELS:2002)
-   els_02_12_byf1sch_v1_0.csv
    -   MetaData: Education Longitudinal Study of 2002, High School Sophomores (ELS:2002)

_This data set provides very detailed information of the 10th graders (e.g., financial background, extracurriculars...)_

#### F3Student‐InstitutionFile
-   els_02_12_f3inst_v1_0.csv
    -   MetaData: Student_institution-F3.pdf  

#### TIGER/Line Shapefile, 2017, nation, U.S., Current Metropolitan Statistical Area/Micropolitan Statistical Area (CBSA) National 

-   tl_2017_us_cbsa

_NOTE these are shape file, and require '.shp', '.shx', and '.prj'._

#### MAINC1 Personal Income Summary: Personal Income, Population, Per Capita Persona

- MAINC1_2012-2017.csv

*   Broomfield County, CO, was created from parts of Adams, Boulder, Jefferson, and Weld counties effective November 15, 2001. Estimates for Broomfield county begin with 2002.
*   Virginia combination areas consist of one or two independent cities with 1980 populations of less than 100,000 combined with an adjacent county. The county name appears first, followed by the city name(s). Separate estimates for the jurisdictions making up the combination area are not available. Bedford County, VA includes the independent city of Bedford for all years.
*Note--* All dollar estimates are in millions of current dollars (not adjusted for inflation). Calculations are performed on unrounded data.
*Metropolitan Areas are defined (geographically delineated) by the Office of Management and Budget bulletin no. 18-03 issued April 10, 2018.*
Last updated: March 6, 2019; revised statistics for 1969-2000. 

#### GDP 		

-   gdp_metro0918.xls														



# Core statistical areas, ID info

-   Core_GEO_ID_2017.csv List 1. CORE BASED STATISTICAL AREAS (CBSAs), METROPOLITAN DIVISIONS, AND COMBINED STATISTICAL AREAS (CSAs), AUGUST 2017

Note: The 2010 OMB Standards for Delineating Metropolitan and Micropolitan Statistical Areas are at <https://www.gpo.gov/fdsys/pkg/FR-2010-06-28/pdf/2010-15605.pdf> and <https://www.gpo.gov/fdsys/pkg/FR-2010-07-07/pdf/2010-16368.pdf>.											
Source: File prepared by U.S. Census Bureau, Population Division, based on Office of Management and Budget, August 2017 delineations <https://www.whitehouse.gov/sites/whitehouse.gov/files/omb/bulletins/2017/b-17-01.pdf>.											
Internet Release Date: January 2018											

## Reports

In this folder are any report files (e.g., slides, summary statistics printed in PDF) generated by the team.


## Data sources

bea financial data from www.bea.gov
geography data https://www.census.gov/geographies/reference-files/time-series/demo/metro-micro/delineation-files.html



