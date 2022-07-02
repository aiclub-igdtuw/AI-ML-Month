# Mini project :

## Problem Statements

![Minor Project Problem Statements(1)-1](https://user-images.githubusercontent.com/77978729/174480488-d7cb66be-ff7c-4e9c-bc50-e3afa73df761.png)<br>

Covid-19 Dataset: https://www.kaggle.com/code/parulpandey/eda-on-covid-19-clinical-trials/data <br>

                
                
                COLAB LINK : https://colab.research.google.com/drive/1BdzpGxhmstxKX-0iblFx2dIKhLhDqgrB?usp=sharing
                

Ques : Mention all the method use to replace null value in a data? 

There are several useful functions for detecting, removing, and replacing null values in Pandas DataFrame :
    isnull()
    notnull()
    dropna()                                                
    fillna()
    replace()
    interpolate()
    
          *  we use a function isnull() and notnull(). Both functions help in checking whether a value is NaN or not.

          *  We use fillna(), replace() and interpolate() functions. These functions replace NaN values with some value of their own.
            fill the missing values using mean(), std(), single value, etc.

          *  In order to drop null values from a dataframe, we used dropna() function. This function drops Rows/Columns of datasets with Null values. 

          *  In this covid dataset, I use the dropna() function for those columns which contain more than 95% null values.


Ques : Give reason why you think this is best plot for particular study: 

      *  Histogram is a common variation of column charts used to present distribution and relationships of a single variable over a set of categories.
        
      *  Column chart is best used to compare different values when specific values are important, and it is expected that users will look up and compare               individual values between each column.
        With column charts you could compare values for different categories or compare value changes over a period of time for a single category.
        
      *  A pie chart typically represents numbers in percentages, used to visualise a part to whole relationship or a composition. Pie charts are not meant to           compare individual sections to each other or to represent exact values.


Ques : What Conditions are these Studies treating?

      *  The disease, disorder, syndrome, illness, or injury that is being studied.
        Observations:

      *  The keywords are : COVID, Coronavirus, SARS, CoV indicating major research being done to find a cure for these diseases
        Less Common conditions are Hypoxemia, Viral Pneumonia, Pregnancy.


Ques : Where are these studies taking place?
  Observations:
     * Most Studies take place in USA (517).
     * Next highest count is in France (349).


Ques : What Age Bracket and Gender are these Studies considering?
  Observations:
    *  Most Studies involve (Adult, Older Adult) Population.
    *  Only Child studies are very few.
    *  Most studies have taken data from All Genders.
    *  In (Adult) and (Child,Adult) Category there is significant number of Female patients considered for the studies.




