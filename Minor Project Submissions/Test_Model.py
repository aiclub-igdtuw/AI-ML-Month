#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from DyslexiaML_final import model
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler


# In[2]:


#Reading file without labels.
data=pd.read_csv('unlabeled_dysx.csv')
#Labels of this file will be predicted by the prepared model.
data.head()


# In[3]:


#Reading file with labels.
dataset = pd.read_csv('labeled_dysx.csv')
#Predictions made for the above file will be compared with labels present in this file.
y_given = dataset.Label #The type of y_given is Pandas Series.
dataset.head()


# In[4]:


#StandardScalar is used for preprocessing of data.
#'copy' is False, which means copies are avoid and inplace scaling is done instead.
sc=StandardScaler(copy=False)
sc.fit_transform(data)


# In[5]:


#Making predictions using RandomForest model with GridSearch in DyslexiaML_final file.
y_pred = model.predict(data)
#Return type of predict is numpy array.
#Type casting prediction into Pandas Series.
y_pred = pd.Series(y_pred)
y_pred.head()


# In[6]:


#Calculating the error between predicted values and the given values
model_error = mean_absolute_error(y_pred, y_given)
model_error


# In[7]:


print("On testing the model, we find that the model gives results with an error rate of %.2f" % (100 * model_error) 
      , '%.', sep = '')

