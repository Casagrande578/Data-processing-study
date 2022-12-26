# This Python3 project will user several librarys for data analysis
# It is using a dataset collected at kaggle in this URL: https://www.kaggle.com/datasets/thedevastator/uncover-global-trends-in-mental-health-disorder?resource=download

# for algebra and data processing this are the imports:
import numpy as np
import pandas as pd

# the next imports are used for visualization methods
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

# Opening the csv file as df
df = pd.read_csv('Mental health Depression disorder Data.csv')
df.drop('index', axis=1, inplace=True)

# Printing the head of the csv analysis but droping a index column that will be useless for the analysis
print(df.head())

# checking data types across the file
print(df.dtypes)


# checking for the existence of duplicates
print(df.duplicated().sum())

duplicated_data = df[df.duplicated(keep='first') == True]
duplicated_data.count()

# droping duplicates that will be useless for this analysis
df.drop_duplicates(keep='first', inplace=True)

# checking for null data
print(df.isnull().sum())

# drops null value from dataframe
df.dropna(axis=0, inplace=True)

# checking again for null values, if there is any remaining
print(df.isnull().sum())

# creating new_df for better clearance
new_df_head = ['Entity', 'Year', 'Schizophrenia (%)', 'Bipolar disorder (%)', 'Eating disorders (%)', 'Anxiety disorders (%)',
               'Drug use disorders (%)', 'Depression (%)', 'Alcohol use disorders (%)']

new_df = df[new_df_head]
print(new_df.head())


# data check status
data_check_table = pd.DataFrame({
    'Unique': df.nunique(),
    'null': df.isna().sum(),
    'null percent': (df.isna().sum())/len(df*100),
    'Type': df.dtypes.values
})
print(data_check_table)

# converting data types


def str_to_float(x):
    if type(x) != float:
        if x[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return(float(x))
        return(float(0))


for i in new_df.columns[2:]:
    new_df[i] = new_df[i].apply(str_to_float)

for i in new_df.columns[2:]:
    print(i)
