from env import host, user, password
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import os
from tabulate import tabulate

#%%
def get_telco_data():
    filename = 'telco_data.csv'
    
    if os.path.exists(filename):
        print('Reading from csv file...')
        return pd.read_csv(filename)
    
    database = 'telco_churn'
    url = f'mysql+pymysql://{user}:{password}@{host}/{database}'

    query = '''
    SELECT *
    FROM customers


    '''
    print('Getting a fresh copy from SQL database...')
    df = pd.read_sql(query, url)
    print('Saving to csv...')
    df.to_csv(filename, index=False)
    return df