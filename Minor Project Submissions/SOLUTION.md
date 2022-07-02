# SOLUTION

Colab Link - https://colab.research.google.com/drive/12MYXSk7ViFvcKOLYGfpIqDzs9wIHQ27A?usp=sharing 

# **DATASET** **IMPORTING**
* The data set was downloaded and uploaded on github within the repository.
* The link was extracted by converting the dataset into a raw data using https://raw.githubusercontent.com/mehakkumarmk/AI-ML-Month/main/Minor%20Project%20Submissions/country_wise_latest.csv


# **NULL VALUE HANDLING**

There are several useful methods for replacing or dropping null values in Pandas data structures. They are

1.   **dropna():** Return a filtered version of the data


```
data.dropna()
# data is the imported dataset

```

2.   **fillna():** Return a copy of the data with missing values filled or imputed


```
data.fillna(0)
# data is the imported dataset
```

* The method used in this EDA is `data.dillna(0, inplace=true)` because we don't want to drop any important data and replacing the NaN/null values with 0 will prevent information loss.

# **OBSERVATIONS ABOUT THE DATASET**
There are 15 columns in the dataset

* Country/Region 
* Confirmed
* Deaths
* Recovered
* Active
* New cases
* New deaths
* New recovered
* Deaths / 100 Cases
* Recovered / 100 Cases
* Deaths / 100 Recovered
* Confirmed last week
* 1 week change
* 1 week % increase
* WHO Region


# **WHO Region**

* This column represents the continent to which the country belongs to hence it WHO region

* A pie chart is best to represent this data to lay out the spread of the pandemic over different Continents and conrresponding WHO Regions whose guidelines are followed by these countries.

* The dataset takes unique values and countes of these WHO Regions and plot them in the pie chart using `matplotlib` library

# **Deaths / 100 Cases**

* This section provides the data regarding the Deaths per hundered cases for each country. 

* This is best represented by a horizontal bar graph to compare the quantity;

* The dataset takes up different countries and Deaths/100 cases corressponding to them and plot them in a horizontal bar graph

**Scales**

      X-axis: Countries/Regions

      Y-axis: Deaths/100 Cases

# **Recovered/ 100 Case**

* This section provides the data regarding the Recovered per hundered cases for each country. 
* This is best represented by a horizontal bar graph to compare the quantity;

* The dataset takes up different countries and Recovered/100 cases corressponding to them and plot them in a horizontal bar graph

**Scales**

      X-axis: Countries/Regions

      Y-axis: Recovered/100 Cases

# **Deaths / 100 Recovered**

* This section provides the data regarding the Deaths per hundered Recovered for each country. 

* This is best represented by a horizontal bar graph to compare the quantity;

* The dataset takes up different countries and Deaths/100 Recovered corressponding to them and plot them in a horizontal bar graph

**Scales**

      X-axis: Countries/Regions

      Y-axis: Deaths/100 Recovered

# **Deaths vs Recovered vs Active**

* The plot below measures three columns at once:

    1. Death Cases
    2. Recovered Cases
    3. Active Cases

* The comparison is represented by line graph where the peaks corresponds to different cases

* Different colored lines represent different quantities
    
    1. **BLUE:** Deaths
    2. **ORANGE:** Recovered
    3. **GREEN:** Active


**Scales**

      X-axis: Countries/Regions

      Y-axis: Case Quantities


# **Confirmed**

* This section gives the information about the confirmed cases in different countries.

* A scatter plot is plotted to define the scattering of quantities of cases across the globe.


**Scales: (per 10^6)**

      X-axis: Countries/Regions

      Y-axis: Confirmed Cases


**OBSERVATION:**

* There are more countries with confirmed cases near to a million cases except a few.

* The maximum number of confirmed cases are above 4 million.


# **REPRESENTATION OF DIFFERENT COUNTRIES IN THE DATA SET ON WORLDMAP**

* This section uses 2 libraries:
  1. Pygal for `wm =pygal.maps.world.World()`

  2. Pycountry to get country codes for data plotting.

* On processing an svg with name 'world.svg' will be saved in the files and can be opened by downloading it.


