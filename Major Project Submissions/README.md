# Major project : 


TEAM MEMBERS :

    * Mansi Sundriyal (04101022019)
    * Anjali Kumari (01101022019)

Problem Statements -

    ![7](https://user-images.githubusercontent.com/77978729/177378861-ffaeb5d2-42bd-40f2-b2cc-49f6ff3e30cc.png)


Diabetes Prediction Dataset:

     https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database <br>

COLAB LINK :

    https://colab.research.google.com/drive/1v3uZaOs9mwC1YzNG7GOi4S4BsB0cCE31?usp=sharing

KNN ALGORITHM:

    * K-Nearest Neighbours algorithm (or KNN) is one of the most used learning algorithms due to its simplicity.
    * KNN is a lazy learning, non-parametric algorithm. It uses data with several classes to predict the classification of the new sample point. KNN is non-         parametric since it doesn’t make any assumptions on the data being studied, i.e., the model is distributed from the data. 
    * KNN can be used in both regression and classification predictive problems.

How does KNN work?

    * The k-nearest neighbour algorithm stores all the available data and classifies a new data point based on the similarity measure (e.g., distance                 functions). This means when new data appears. Then it can be easily classified into a well-suited category by using the K- NN algorithm. 
    * Suppose there are two classes, i.e., Class A and Class B, and we have a new unknown data point, so this data point will lie in which of these classes. To       solve this problem, we need a K-NN algorithm. With the help of K-NN, we can easily identify the class of a particular dataset. The data point is               classified by a majority vote of its neighbours, with the data point being assigned to the class most common amongst its K nearest neighbours 
      measured by a distance function.

Why did we use KNN?

    a. We have properly labelled data. For example, here in this dataset if we are predicting someone is having diabetes or not the final label can be 1 or 0.        It cannot be NaN or -1.
    b. Data is noise-free. For this diabetes data set we cannot have a Glucose level as 0 or 10000. It’s practically impossible.
Some Advantages of KNN:

      * Simple to implement and intuitive to understand
      * Can learn non-linear decision boundaries when used for classification and regression. Can come up with a highly flexible decision boundary adjusting           the value of K.
      * No Training Time for classification/regression: The KNN algorithm has no explicit training step and all the work happens during prediction
      * Constantly evolves with new data: Since there is no explicit training step, as we keep adding new data to the dataset, the prediction is adjusted               without having to retrain a new model.
      * Single Hyperparameters: There is a single hyperparameter, the value of K. This makes hyper parameter tuning easy.
      * Choice of distance metric: There are many distance metrics to choose from. Some popular distance metrics used are Euclidean, Manhattan, Minkowski,             hamming distance and so on.
      * Quick calculation time
      * Versatile – useful for regression and classification
      * High accuracy – you do not need to compare with better-supervised learning models
      * No assumptions about data – no need to make additional assumptions, tune several parameters, or build a model. This makes it crucial in nonlinear data         case. 

