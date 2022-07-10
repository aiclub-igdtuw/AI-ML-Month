# SOLUTION
Major Project - Employee Attrition
Colab link: https://colab.research.google.com/drive/1jQPPybRmA7kDmUeOVc0c_hBYVFBpvsKy?usp=sharing

Observations-
Major Project-Employee Attrition.

Attrition means when a large no of people retire or leave a work place.
I created three models :

Logistic Regression - The logistic model is a statistical model that models the probability of one event taking place by having the log-odds for the event be a linear combination of one or more independent variables.

Random Forest Classifer - The random forest is a classification algorithm consisting of many decisions trees. It uses bagging and feature randomness when building each individual tree to try to create an uncorrelated forest of trees whose prediction by committee is more accurate than that of any individual tree.

Gaussian NB - Gaussian Naive Bayes is a variant of Naive Bayes that follows Gaussian normal distribution and supports continuous data.

,to predict the accuracy and f1 score of these models.

We observe that out of the three models the accuracy of the logistic regression model is the highest whereas the accuracy of the gaussianNB model is the lowest. 
The accuracy can be calculated as accuracy_score or as ((TP+TN)/(TP+TN+FN+FP))

We further observe that out of the three models the accuracy of the logistic gaussianNB model is the highest whereas the accuracy of the Random Forest Classifier model is the lowest.
The f1 score canbe calculated as f1_scores or by using a formula -
2*(precision*recall)/(precision+recall).

OTHER OBSERVATIONS:

Males have high performance rating as compared to females.
There are maximum number of employees working in Research and Development department and so the count of people of Research & Development wrt Job Satisfaction is high.
People with Education level = 3 have highest performance rating whereas the people with education level =5 has less performance rating even though level = 5 people are more educated and are doctors.
