#IMPORTING LIBRARIES
import os
#os.environ['KAGGLE_CONFIG_DIR'] = '/content/drive/MyDrive/Kaggle'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

#DOWNLOADING DATASET
!kaggle datasets download -d jessicali9530/honey-production
#UNZIPPING ZIP FOLDER
!unzip \* && rm *.zip

DataHP = pd.read_csv('honeyproduction.csv')

#To get 1st 5 rows to get an idea of dataset 
DataHP.head() 

# WILL RETURN A TUPLE (ROWS,COLUMNS)
DataHP.shape

# COLUMN NAMES WITH INDEXES
DataHP.columns

#to find the unique value counts of each element in the given Series object.
DataHP['state'].value_counts()
DataHP['numcol'].value_counts()
DataHP['yieldpercol'].value_counts()
DataHP['totalprod'].value_counts()
DataHP['stocks'].value_counts()
DataHP['priceperlb'].value_counts()
DataHP['prodvalue'].value_counts()
DataHP['year'].value_counts()

#PLOT 1
#LINE CHART 
#plt.title('CORRELATION')
sns.pairplot(DataHP, hue ='state')

#PLOT2
# Using Seaborn library to plot a bar graph.
rcParams['figure.figsize'] = 10,6
sns.barplot(x="year",y="totalprod", data=DataHP)

# Using Seaborn library to plot a bar graph.
rcParams['figure.figsize'] = 8,4
sns.barplot(x="year",y="totalprod", data=DataHP)

rcParams['figure.figsize'] = 8,4
sns.barplot(x="year",y="prodvalue", data=DataHP)

#PLOT3
# Using Seaborn library to plot a bar graph.
rcParams['figure.figsize'] = 10,6
sns.barplot(x="year",y="numcol", data=DataHP)

# Using Seaborn library to plot a bar graph.
rcParams['figure.figsize'] = 15,8
sns.barplot(x="year",y="yieldpercol", data=DataHP)

# Using Seaborn library to plot a bar graph.
rcParams['figure.figsize'] = 15,10          #Altering size of plot
sns.barplot(x="state",y="totalprod", data=DataHP)

# Using Seaborn library to plot a bar graph.
rcParams['figure.figsize'] = 15,8                        #Altering size of plot
sns.barplot(x="year",y="totalprod", data=DataHP)

# Using Seaborn library to plot a bar graph.
rcParams['figure.figsize'] = 15,8
sns.barplot(x="year",y="prodvalue", data=DataHP)

yr =DataHP['year']
tp =DataHP['totalprod']
pv =DataHP['prodvalue'] 
plt.plot(yr,tp,color="green",label='Production')
plt.plot(yr,pv,color="red",label='Value')
plt.legend()
plt.show()
