import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

# to get a concise summary of the dataframe.
df.info()

#To get the shape of Pandas DataFrame
df.shape

#To get column names
df.columns

#Renaming DiabetesPredictionFunction column  to DPF
df.rename({'DiabetesPedigreeFunction':'DPF'},inplace = True,axis =1)

#Renaming BloodPressure column to BP
df.rename({'BloodPressure':'BP'},inplace = True,axis =1)

df.head()

# OUTCOME:  0 --> Non-Diabetic  
#           1 --> Diabetic

# To get description of dataset with some statistical measures
df.describe()

#Datatype of each column
df.dtypes

#Checking for null values
df.isnull().sum()

#Checking duplicate values
df.duplicated().sum()

#No. of People having diabetes or not
df['Outcome'].value_counts()
#0 for non-diabetic
#1 for diabetic

#Mean of different quantities for corresponding individual outcome 
df.groupby('Outcome').mean()

#Countplot for no. of People having diabetes or not
sns.countplot(df['Outcome'], palette = "Set2")

#Boxplot for indicating outliers
plt.figure(figsize = (12,12))
for i, col in enumerate(['Pregnancies', 'Glucose', 'BP', 'SkinThickness', 'Insulin',
       'BMI', 'DPF', 'Age', 'Outcome']):
       plt.subplot(3,3,i+1)
       sns.boxplot(x = col, data = df, color='skyblue')
plt.show()

#Pregnancy outliers.
df['Pregnancies'].describe()

plt.boxplot(df.Pregnancies, showmeans=True, vert=False, sym='r+')

#Function for treating outliers of all columns
def std_resolve(col_name,df):
    mean = df[col_name].mean()
    std = df[col_name].std()
    bar = std * 3
    lower, upper = mean - bar, mean + bar
    df_1 = df[(df[col_name] < upper) & (df[col_name] > lower)]
    return df_1
  
 #Treating the Pregnancy outliers
df = std_resolve('Pregnancies', df)

plt.boxplot(df.Pregnancies, showmeans=True, vert=False, sym='r+')

BP Outliers
df.BP.describe()

plt.boxplot(df.BP, showmeans=True, vert=False, sym='k+')

#Resolving BP = 0 outlier
df.BP = df.BP.replace(0,df.BP.median())
df.head()

df  = std_resolve('BP',df)

#Glucose Outliers
df['Glucose'].describe()

plt.boxplot(df.Glucose, showmeans=True, vert=False, sym='r+')

#Resolving Glucose = 0 outlier
df.Glucose = df.Glucose.replace(0,df.Glucose.median())
df.head()

plt.boxplot(df.Glucose, showmeans=True, vert=False, sym='r+')

#Skin thickness Outliers
df.SkinThickness.describe()
plt.boxplot(df.SkinThickness, showmeans=True, vert=False, sym='y+')

#SkinThickness = 0 is an outlier

df.SkinThickness = df.SkinThickness.replace(0,df.SkinThickness.mean())
df.head()

#Resolving SkinThickness = 0 outlier
df = std_resolve("SkinThickness",df)

plt.boxplot(df.SkinThickness, showmeans=True, vert=False, sym='y+')

#Insulin Outliers
df.Insulin.describe()

plt.boxplot(df.Insulin, showmeans=True, vert=False, sym='b+')

#Resolving outliers Insulin = 0
df = std_resolve('Insulin',df)

plt.boxplot(df.Insulin, showmeans=True, vert=False, sym='b+')

#BMI Outliers
df.BMI.describe()

plt.boxplot(df.BMI, showmeans=True, vert=False, sym='g+')

#Resolving outlier BMI = 0
df.BMI = df.BMI.replace(0,df.BMI.mean())
df.head()

plt.boxplot(df.BMI, showmeans=True, vert=False, sym='g+')

#DPF(DIABETES PREDICTION FUNCTION) OUTLIER
df.DPF.describe()

plt.boxplot(df.DPF, showmeans=True, vert=False, sym='c+')

#Outliers present to right of boxplot

df = std_resolve('DPF',df)
plt.boxplot(df.DPF, showmeans=True, vert=False, sym='c+')

#Age Outliers
df.Age.describe()

plt.boxplot(df.Age, showmeans=True, vert=False, sym='m+')

#Pairplot for the dataset
sns.pairplot(df, hue='Outcome', palette='husl')
plt.show()

#HistPlot for the dataset
plt.figure(figsize = (12,12))
for i, col in enumerate(['Pregnancies', 'Glucose', 'BP', 'SkinThickness', 'Insulin','BMI', 'DPF', 'Age', 'Outcome']):
       plt.subplot(3,3,i+1)
       sns.histplot(x = col, data = df, kde = True)
plt.show()   

#HeatMap for the dataset
corr = df.corr()
features = corr.index
plt.figure(figsize=(10,10))
ax = sns.heatmap(df[features].corr(), annot=True)

#relation between Pregnancies and Outcme(Diabetic or Non-Diabetic)
sns.set_style('darkgrid')
sns.countplot(x='Pregnancies',hue='Outcome',data=df,palette='plasma')

#PART 2 : THREE MODELS
#MODEL 1 : SUPPORT VECTOR MACHINE (SVM)
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

# Separating data in 'X' & labels as 0 or 1 in 'Y'
X = df.drop(columns = 'Outcome', axis = 1)      # axis=1, to drop a particular column   ; axis=0, to drop a particular row
Y = df['Outcome']      #Model

# Standardizing Data
Scaler = StandardScaler()
Scaler.fit(X)
StdData = Scaler.transform(X)              #To scale the training data
X = StdData                            #Data : With this data (in range of 0s & 1s) we're able to get better predictions.

# Splitting training & test data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, stratify = Y, random_state = 2) 
#0.2 -> taking only 20% of actual data for testing,
#stratify :  to ensure that both the train and test sets have the proportion of examples in each class that is present in the provided “Y” array.
#random_state :  controls the shuffling process.

# Training our Model
Clssifier = svm.SVC(kernel = 'linear')
Clssifier.fit(X_train, Y_train)

# Evaluation of our Model : ACCURACY SCORE

#For training data
Pred_for_X_train = Clssifier.predict(X_train)
TrainD_accuracy = accuracy_score(Y_train, Pred_for_X_train)
print('Accuracy score on training data = ',TrainD_accuracy)

#For test data
Pred_for_X_test = Clssifier.predict(X_test)
TestD_accuracy1 = accuracy_score(Y_test, Pred_for_X_test)
print('Accuracy score on test data = ',TestD_accuracy1)

# CONFUSION MATRIX PLOT : SVM

import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import confusion_matrix

Cf_matrix = confusion_matrix(Y_test, Pred_for_X_test)
print(Cf_matrix)
# Print the confusion matrix using Matplotlib

fig, ax = plt.subplots(figsize=(6, 6))
ax.matshow(Cf_matrix, cmap=plt.cm.Oranges, alpha=0.3)
for i in range(Cf_matrix.shape[0]):
    for j in range(Cf_matrix.shape[1]):
        ax.text(x=j, y=i,s=Cf_matrix[i, j], va='center', ha='center', size='xx-large')
 
plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix : SVM', fontsize=18)
plt.show()

#CALCULATIONS FOR SUPPORT VECTOR MACHINE (SVM)
#TN = 88, FP = 8, FN = 20, TP = 29

#Accuracy Score= (TN + TP)/(TN + TP + FN + FP) = 0.8068965517241379
# F1 SCORE FOR LOGISTIC SVM

from sklearn.metrics import f1_score                                
FS1 = f1_score(Y_test, Pred_for_X_test, average='macro')                                     # used macro because treats all classes equally
print(FS1)

#MODEL 2 : KNN (K-NEAREST NEIGHBOUR)

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import xgboost as xgb
from sklearn.metrics import classification_report,confusion_matrix, accuracy_score

ss=StandardScaler()
ss.fit(df.drop(['Outcome'], axis=1))
scaled=ss.transform(df.drop(['Outcome'], axis=1))
scaled_df=pd.DataFrame(data=scaled, columns=df.columns[:-1])
X=scaled_df
y=df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

error_rate=[]
for n in range(1,40):
    knc=KNeighborsClassifier(n_neighbors=n)
    knc.fit(X_train, y_train)
    prediction_knn=knc.predict(X_test)
    error_rate.append(np.mean(prediction_knn!=y_test))
print(error_rate)
plt.figure(figsize=(10,6))
plt.plot(list(range(1,40)), error_rate,color='midnightblue', marker='o', linewidth=2, markersize=12, markerfacecolor='lightcoral', markeredgecolor='lightcoral' )
plt.xlabel('Number of Neighbors', fontsize=10)
plt.ylabel('Error Rate', fontsize=10)
plt.title('Error Rate Versus Number of Neighbors by Elbow Method', fontsize=10)
plt.show()

knc=KNeighborsClassifier(n_neighbors=15)
knc.fit(X_train, y_train)
prediction_knn=knc.predict(X_test)
print('CONFUSION MATRIX:')
print('\n')
print(confusion_matrix(y_test,prediction_knn))
print('\n')
print(classification_report(y_test,prediction_knn))
TestD_accuracy2 = accuracy_score(y_test,prediction_knn)
print('Accuracy Score: ',round(TestD_accuracy2, ndigits=2))

# CONFUSION MATRIX PLOT : K NEAREST NEIGHBOUR MODEL

Cf_matrix = confusion_matrix(y_test,prediction_knn)
print(Cf_matrix)
# Print the confusion matrix using Matplotlib

fig, ax = plt.subplots(figsize=(6, 6))
ax.matshow(Cf_matrix, cmap=plt.cm.Oranges, alpha=0.3)
for i in range(Cf_matrix.shape[0]):
    for j in range(Cf_matrix.shape[1]):
        ax.text(x=j, y=i,s=Cf_matrix[i, j], va='center', ha='center', size='xx-large')
 
plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix : KNN', fontsize=18)
plt.show()

#CALCULATIONS FOR KNN
#TN = 94, FP = 9, FN = 22, TP = 20

#Accuracy Score= (TN + TP)/(TN + TP + FN + FP) =0.79
# F1 SCORE FOR KNN

FS2 = f1_score(Y_test, prediction_knn, average='macro')                                     # used macro because treats all classes equally
print(FS2)

#MODEL 3 : LOGISTIC REGRESSION

from sklearn.linear_model import LogisticRegression

# Separating data in 'X' & labels as 0 or 1 in 'Y'
X = df.drop(columns = 'Outcome', axis = 1)      # axis=1, to drop a particular column   ; axis=0, to drop a particular row
Y = df['Outcome']      #Model

# Standardizing Data
Scaler = StandardScaler()
Scaler.fit(X)
StdData = Scaler.transform(X)              #To scale the training data
X = StdData                            #Data : With this data (in range of 0s & 1s) we're able to get better predictions.

# Splitting training & test data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, stratify = Y, random_state = 2) 

# Training our Model
Model = LogisticRegression()
Model.fit(X_train, Y_train)

# Evaluation of our Model : ACCURACY SCORE

#For training data
Pred_for_X_train = Model.predict(X_train)
TrainD_accuracy = accuracy_score(Pred_for_X_train, Y_train)
print('Accuracy score on training data = ',TrainD_accuracy)

#For test data
Pred_for_X_test = Model.predict(X_test)
TestD_accuracy3 = accuracy_score(Pred_for_X_test, Y_test)
print('Accuracy score on test data = ',TestD_accuracy3)

# CONFUSION MATRIX PLOT : LOGISTIC REGRESSION MODEL

Cf_matrix = confusion_matrix(Y_test, Pred_for_X_test)
print(Cf_matrix)
# Print the confusion matrix using Matplotlib

fig, ax = plt.subplots(figsize=(6, 6))
ax.matshow(Cf_matrix, cmap=plt.cm.Oranges, alpha=0.3)
for i in range(Cf_matrix.shape[0]):
    for j in range(Cf_matrix.shape[1]):
        ax.text(x=j, y=i,s=Cf_matrix[i, j], va='center', ha='center', size='xx-large')
 
plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix : Logistic Regression', fontsize=18)
plt.show()

#CALCULATIONS FOR LOGISTIC REGRESSION
#TN = 87, FP = 9, FN = 20, TP = 29

#Accuracy Score= (TN + TP)/(TN + TP + FN + FP) =0.8
# F1 SCORE FOR LOGISTIC REGRESSION MODEL

FS3 = f1_score(Y_test, Pred_for_X_test, average='macro')                                     # used macro because treats all classes equally
print(FS3)

#graph to study the accuracy and f1-score of these models and then choose the best model.

import matplotlib.pyplot as plt
from matplotlib import rcParams

w=0.4
x = ['SVM','KNN','Logistic Regression']
Accuracies = [TestD_accuracy1, TestD_accuracy2, TestD_accuracy3]
F1_Scores = [FS1, FS2, FS3]

bar1 = np.arange(len(x))
bar2 = [i+w for i in bar1]

plt.bar(bar1, Accuracies, w, label = 'Accuracy Score', color='black')
plt.bar(bar2, F1_Scores, w, label = 'F1 Score', color='orange')

plt.xlabel('SVM                        KNN                         Logistic Regression ')
plt.ylabel('SCORE')
plt.title('Study of accuracy and f1 score of used models.')
rcParams['figure.figsize'] = 6,10
plt.legend()

#to show the accuracy of predictions of the model.
#MODEL : SVM

#Prediction Code
#TAKEN AN EXAMPLE FROM ROW '1' AND THE LADY IS DIABETIC :

print("TAKEN AN EXAMPLE FROM ROW 1 AND THE LADY IS DIABETIC : OUTCOME SHOULD BE 1")
input = (6, 148, 72, 35.000000, 0, 33.6, 0.627, 50)           #Row 1 data

# Changing data to Numpy Array
Npinput = np.asanyarray(input)

# Reshaping array for prediction of 1 instance
RS_input = Npinput.reshape(1,-1)

# Standardization of input data
std_input = Scaler.transform(RS_input)

Predic = Clssifier.predict(std_input)
print('PREDICTION BY SVM MODEL = ',Predic)   
