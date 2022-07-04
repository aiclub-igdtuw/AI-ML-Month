#!/usr/bin/env python
# coding: utf-8

# In[61]:


#importing python libraries
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[62]:


#Reading file in the directory
data = pd.read_csv("C:\\Users\\Kirti\\Downloads\\WA_Fn-UseC_-HR-Employee-Attrition.csv")
data.head()


# In[63]:


#Q1
#Determine the no. of employees between age 50 and 60 given that department should be sales and gender should be female
a=data[(data['Age']>50) & (data['Department']=="Sales") & (data['Gender']=="Female")]
n=len(a.value_counts(['Age','Department','Gender']))
print("No. of employees between the age of 50 and 60 given that department should be sales and gender should be female:",n)


# In[64]:


#Q2
#Plot a graph showing relation between education and department given education should be equal to 1 and hence show no. of employees in each department wrt their education which should be equal to 1
a=len(data[(data['Education']==1)&(data['Department']=='Sales')])
b=len(data[(data['Education']==1)&(data['Department']=='Research & Development')])
c=len(data[(data['Education']==1)&(data['Department']=='Human Resources')])
y = np.array([a, b, c])
mylabels = ["Sales", "Research & Development", "Human Resources"]

plt.pie(y, labels = mylabels)
plt.show() 
print("Employees with education equal to 1 in Sales Department:",a)
print("Employees with education equal to 1 in Research & Development Department:",b)
print("Employees with education equal to 1 in Human Resources Department:",c)


# # Explanation:
# 1)The blue part of the pie chart is showing employees having education 1 and no. of employees in Sales Department i.e. 50.
# 2)The orange part of the pie chart is showing employees having education 1 and no. of employees in Research & Development Department i.e.115.
# 3)The green part of the pie chart is showing employees having education 1 and no. of employees in Human Resource Department i.e.5 .
# # Conclusion:
# From the above pie chart we can see that most number of employee are from Research and Development Department followed by Sales department and Human Resources Department respectively. All employees have education equal to 1.

# In[65]:


#Q3
#Make a suitable plot showing relationship between performance rating and education. Also compute which gender has a very high performance rating
#Education vs Performance Rating
pd.crosstab(data['Education'],data['PerformanceRating']).plot(kind="bar",figsize=(10,6))
plt.title("Education vs Performance Rating")
plt.xlabel("Education")
plt.legend(["Excellent","Outstanding"])
plt.xticks(rotation=0)
#Gender vs Performance Rating
f=data.groupby('Gender')['PerformanceRating'].mean()
print(f)
print('Female have higher Performance Rating as compared to Male')


# # Explanation
# The above bar graph shows the relationship between performance rating and education of the employees.
# It also shows how many employees with a certain education are performing.
# # Conclusion
# From The above graph we can conclude that employees having education have high performance rating.
# it can also be concluded that Female employees have high performance rating than Male employees.

# In[66]:


#Q4
#Compute the median, average, modal monthly income for both male and female
import statistics
a=data.groupby('Gender')['MonthlyIncome'].median()
b=data.groupby('Gender')['MonthlyIncome'].mean()
c=data.groupby('Gender')['MonthlyIncome'].apply(statistics.mode)
print('Median\n',a)
print('Mean\n',b)
print('Mode\n',c)


# In[67]:


#Q5
#Determine the level of job satisfaction by most of the people and hence compute people of which department are most satisfied
m=data["JobSatisfaction"].max()
print("Job Satisfaction by most of the people=",m,"which means that they are highly satisfied.")
d=data[(data["JobSatisfaction"]==m)]
d1=a.value_counts(['Department'])
print(d1)
print("People of Sales department are most satisfied.")

