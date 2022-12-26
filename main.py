# This Python3 project will user several librarys for data analysis
# It is using a dataset collected at kaggle in this URL: https://www.kaggle.com/datasets/thedevastator/uncover-global-trends-in-mental-health-disorder?resource=download

# for algebra and data processing this are the imports:
import numpy as np
import pandas as pd

# the next imports are used for visualization methods
import matplotlib.pyplot as plt
import matplotlib as mpl

import random
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
print(df[df.isna().any(axis=1) == True])

# creating new_df for better clearance
new_df_head = ['Entity', 'Year', 'Schizophrenia (%)', 'Bipolar disorder (%)',
               'Eating disorders (%)', 'Anxiety disorders (%)',
               'Drug use disorders (%)', 'Depression (%)',
               'Alcohol use disorders (%)']


new_df = df[new_df_head]
print(new_df.head())

# checking new df
new_df.isna().any(axis=0).sum()
# drops null value from dataframe
new_df.dropna(axis=0, inplace=True)

# checking again for null values, if there is any remaining
print(new_df.isnull().sum())

# data check status
data_check_table = pd.DataFrame({
    'Unique': new_df.nunique(),
    'null': new_df.isna().sum(),
    'null percent': (new_df.isna().sum())/len(new_df*100),
    'Type': new_df.dtypes.values
})
print(data_check_table)


# converting data types


def str_to_float(x):
    if type(x) != float:
        if x[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return(float(x))
        return(float(0))
    return x


for i in new_df.columns[2:]:
    new_df[i] = new_df[i].apply(str_to_float)

for i in new_df.columns[2:]:
    print(i)


nation_group_issue_avg = new_df.groupby('Entity', as_index=False).agg({'Schizophrenia (%)': 'mean', 'Bipolar disorder (%)': 'mean', 'Eating disorders (%)': 'mean',  'Anxiety disorders (%)': 'mean', 'Drug use disorders (%)': 'mean',
                                                                       'Depression (%)': 'mean', 'Alcohol use disorders (%)': 'mean'})

for i in nation_group_issue_avg.columns[1:]:
    print(i)

colors = ['purple', 'red', 'yellow', 'blue']


for i in nation_group_issue_avg.columns[1:]:
    top10_nation = nation_group_issue_avg.sort_values(
        by=i, ascending=False).head(10)

    bar_colors = []
    for j in range(20):
        bar_colors.append(random.choice(colors))

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.bar(top10_nation['Entity'], top10_nation[i],
           width=0.35, label=i, color=bar_colors)

    ax.set_ylabel('Averege Mental Issue')
    ax.set_title(
        f"Top 10 avegrage mental issue visualization for '{i}' by nations")
    plt.xticks(rotation=90)
    ax.legend()
    plt.show()
