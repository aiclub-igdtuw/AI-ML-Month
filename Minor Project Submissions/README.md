# Mini project : HONEY PRODUCTION

COLAB LINK:https://colab.research.google.com/drive/1T6GfFf_x42cl0kwiIMT6tvZT1GmXSsdz?usp=sharing

Q.1. EXPLORE QUANTITATIVE VARIABLES AND QUALITATIVE VARIABLEA IN THE DATASET.

ANS.QUALITATIVE VARIABLES OR CATEGORICAL VARIABLES: These are variables that take on names or lables and can fit into categories. Qualitative variables are divided into two types: nominal and ordinal. (a) QUALITATIVE NOMINAL VARIABLE is a variable where no ordering is possible or implied in the levels. Examples: the variable eye color is nominal variale because there is no order among blue, brown or red eyes. A nominal variable can have: (i) two levels(eligible?yes/no, or married? yes/no etc.) (ii) a large number of levels(what is your college major? Each major is a level in that case). A qualtative variable with exactly 2 levels is referred as a binary or dichotomous variable.

(b) QUALITATIVE ORDINAL VARIABLES is a qualitative variable with an order implied in the levels. For example, health, which can take values such as poor, reasonable, good, or excellent. Again, there is clear order in these levels so health is in this case a qualitative ordinal variable.

QUANTITATIVE VARIABLES OR NUMERICAL VARIABLES: These are variables that reprent a measurable quantity.A quantitative variables represents a measure and is numerical. Quantitative variables are divided into two types: discrete and continuous.

(a) QUANTITATIVE DISCRETE VARIABLES are variables for which the values it can take are countable and have a finite number of possibilities. The values are often(but not always) integers. Examples of quantitative discrete variables are: no. of students in a particular course, no. of subjects/classes per semester etc.

(b) QUANTITATIVE CONTINOUS VARIABLES are variables for which the values are not countable and have an infinite number of possiblities. Examples of quantitative continous variables: age, weight, height etc.

In the given dataset, there are eight total varibles in which seven of them are quantitive variables ('numcol', 'yieldpercol', 'totalprod', 'stocks', 'priceperlb','prodvalue', 'year') and one of them is quanlitative('state').


Q.2 FIND THE RELATIONSHIP BETWEEN NUMERICAL VARIABLES USING PAIR PLOT AND CORRELATION PLOTS.EXPLAIN WHAT YOU INFER FROM THESE PLOTS.

To plot multiple pairwise bivariate distributions in a dataset, you can use the pairplot() function. This shows the relationship for (n, 2) combination of variable in a DataFrame as a matrix of plots and the diagonal plots are the univariate plots.
The correlation coefficient is bound to be in between -1 and 1 and tells us the linear relationship.
The correlation stablize the dergee of relationship between the two variables. The correlation coefficient is bound to be in between -1 and 1 and tells us the linear relationship.


Q.3. LOOK AT THE OVERALL TREND OF HONEY PRODUCTION IN THE US OVER THE YEARS.

we observe from the above graph that the overall trend of totalprod decrease as the year increases from year 1998 to year year 2021.

Q.4. ARE THERE ANY PATTERNS THAT CAN BE OBSERVED BETWEEN TOTAL HONEY PRODUCTION AND VALUE OF PRODUCTION EVERY YEAR?HOW HAS THE VALUE OF PRODUCTION , WHICH IN SOME SENSE COULD BE TIED TO DEMAND , CHANGED EVERY YEAR?

we observe from the above graph that the overall trend of totalprod decrease as the year increases from year 1998 to year year 2021 and the overall trend of prodvalue increase as the year increases from year 1998 to year year 2021.
we observe from the above graphs that as the year increase from year 1998 to year 2012, the value of the stock decreases and the value of product increases.


Q.5. OBSERVE THE VARIATION IN THE NUMBER OF COLONIES OVER THE YEAR.
we observe from the above graph that there is a decrease in number of colonies from year 1998 till 2001,then increase from year 2001 till 2004,then decrease from year 2004 till 2008, then there is steeply increase in no. of colonies from year 2008 till 2010 and then decreases form year 2010 to year 2011.

Q.6 ANALYZE THE VARIATION OF YIELD PER COLONY OVER THE YEARS AND PRODUCTION TREND AT STATE LEVEL; AND BRIEF OUT WHAT YOU OBSERVED.
Q.6.(i) ANALYZE THE VARIATION OF YIELD PER COLONY OVER THE YEARS
As the slope of the graph is negative, the overall trend in yeildpercol decreases as the year increase.

Q.6.(ii) PRODUCTION TREND AT STATE LEVEL
there is no particular trend observe in above graph.

Q.7. ANALYZE WHAT EFFECT THE DECLINING PRODUCTION TREND HAS HAD ON THE VALUE OF PRODUCTION
we observe from the above graph that the overall trend in prodvalue increase as the totalprod increases. So the effect of declining production trend will have decrease in the value of production also.

