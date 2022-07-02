# SOLUTION

Colab link-https://colab.research.google.com/drive/1S35LVfEbb9NNR-f084kt6_m-KRlyw5m_#scrollTo=TxDfinjQG3RF

Topic:
Loan Default Prediction

Problem Statement:
The bank claims possession over the collateral against which the loan has been taken if the defaulters do not pay the EMI on time.The grace period given to the people depends upon their annual income and bank balance. If a person has an annual income greater than 100K and bank balance greater than 5k then the bank will give a grace period of 15 days, else grace period increases if and only if the person is unemployed else the bank charges a fine equivalent to 2.5% of bank balance per day.  

Problem Faced:
The dataset is not having all the criterias for producing proper deduction like it does not have conditions which satisfy the no grace period situation and thus no data or table is produced for it.

Ways of Enhancing:
a) Can include date of providing the loan so that using that attribute and present date can calculate when to give the EMI and when to start taking fine.
b)Can add data related to situations when a person do not get grace period.
