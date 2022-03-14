## Telco Churn Project 

# Project Description: 
Telco wished to determine why customers are leaving the company and what are the main drivers that lead to customers leaving. 

    Goals:
        1. Identify primary drivers why customer 
        2. Build Machine Learning Models to predict which customers will churn 

# Initial hypotheses 

Driving factors to customer churn 
    
    1. Customers who pay month to month have a higher churn rate comparied to those who pay automaticly
        Questions:
            1. Does customer churn becasue of aggressive collection practice?

    2. Customers with only dsl internet churn higher vs customers with fiber & phone
        Questions: 
            1. Is there a issue with service?

    3. Customers who opt out of paperless billing have a higher churn comparied to those who do not. 
        Questions: 
            1. Does paperless bill help remind customers to pay on time?
         
# Data Dictionary 

| Variable                             | Data Type  | Description                                                         |
|:-------------------------------------|:-----------|:--------------------------------------------------------------------|
customer_id                               object      Customer ID
senior_citizen                            int64       Is senior citizen
tenure                                    int64       Month been with company
internet_service_type_id                  int64       (1) DSL, (2) Fiber
contract_type_id                          int64       (1) Monthly, (2) one year, (3) two Year
payment_type_id                           int64       (1) Electronic Check, (2) check, (3) auto draft, (4) auto credit card
monthly_charges                           float64     monthly bill
total_charges                             float64     total amount billed
gender_Male                               uint8       (0) female, (1) male
partner_Yes                               uint8       (0) no, (1) yes
dependents_Yes                            uint8       (0) no, (1) yes
phone_service_Yes                         uint8       (0) no, (1) yes
multiple_lines_No phone service           uint8       (0) yes, (1) no
multiple_lines_Yes                        uint8       (0) no, (1) yes
online_security_No internet service       uint8       (0) yes, (1) no
online_security_Yes                       uint8       (0) no, (1) yes
online_backup_No internet service         uint8       (0) yes, (1) no
online_backup_Yes                         uint8       (0) no, (1) yes
device_protection_No internet service     uint8       (0) yes, (1) no
device_protection_Yes                     uint8       (0) no, (1) yes
tech_support_No internet service          uint8       (0) yes, (1) no
tech_support_Yes                          uint8       (0) no, (1) yes
streaming_tv_No internet service          uint8       (0) yes, (1) no
streaming_tv_Yes                          uint8       (0) no, (1) yes
streaming_movies_No internet service      uint8       (0) yes, (1) no
streaming_movies_Yes                      uint8       (0) no, (1) yes
paperless_billing_Yes                     uint8       (0) no, (1) yes
churn_Yes                                 uint8       (0) no, (1) yes

# Project Planning

    Define Initial hypotheses concerning the issue regarding customer churn and development of questions.

    Acquire date using get_telco function from acquire.py from CodeUp database and create functions to automate data prep and machine model. 

    Conduct data cleaning and wrangling using prepare.py and fuctions to automate process

    Train multiple machine models and preform hyperparameters cross validation using sklearn GridSearchCV

    Choose best model based on the top three performing models and

    Create csv file 

# Instructions on how someone else can repoduce results findings

    You will need your own env.py with cradintuals to access CodeUp database. Import tools and utilities that are in jupyter notebook. It is recommended that you make a copy of final, rough draft of the Telco Churn Project, aquire.py, and prepare.py. Also, the rough draft goes into more detail with hyperparameters to fine tune machine models.

# Key findings, recommendations, and takeaways from your project. 
    
    Key findings:
        
        1. The top three key drivers for customer churn is:
                a. Contract type Month to Month (value=1)
                b. Payment type Manual Electronic Check (value=1)
                c. Internet type DSL (value=2)
                d. Customer who opt-out of paperless billing (value=1)

    Recommendations:
               
        1. Raise monthly charges for Month to Month contracts for internet by $15 and offer a $10 discount to auto pay
        
        2. Offer added service to customers who opt into paperless billing
        
        3. Assess the customers service department handling of calls to inquire about late payments and collection practices.
        
        4. Send out a survey concerning happeness with services and offer a $5 discount on next billing cycle to promote participation

