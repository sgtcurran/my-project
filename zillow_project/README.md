Regression Project - Zillow Home Value Prediction

# Project Overview & Goals:
To create a DataFrame from Zillow dataset that can be used to predict the value of a home though a regression model. I will be utilizating visualization, statistical testing, top drivers for home value, and data preperation to determine the best model to use. For train, validate, and test I have set the seed to 123.

# Question:
    * What is the correlation between the target (taxvalue) and the features?
    * What is the correlation between features to features?
    * What is the best regression model to use?


Data Dictionary:

| Features                       | Definition                                         | Data Type |
|:-------------------------------|:--------------------------------------------------:|:---------:|
| bedrooms                       | total number of bedrooms                           | category  |
| bathrooms                      | total number of bathrooms                          | category  |
| sqft_living                    | total sqft of living spaces | category             | float64   |
| sqft_lot                       | total sqft of property size                        | float64   |
| zip                            | property zipcode                                   | float64   |
| county                         | property county & state                            | category  |
| taxvaluedollarcnt              | total tax value of property                        | float64   |


Project Reproduction:
* You will need to have your own env.py to access zillow date with username and password for CodeUp Server
* Clone the repo on your local machine
* Import libraries from yellowbrick, sklearn, pandas, python 3.x, numpy, and matplotlib
* Follow steps in rough_draft.ipynb and final_draft.ipynb