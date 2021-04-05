import numpy as np
import pandas as pd

"""
Check a dataframe for nulls and return the number of missing values.
"""
def null_count(df):
    if isinstance(x, pd.DataFrame):
        return df.isnull().sum().sum()
    else:
        print("Invalid datatype")

"""
Create a Train/Test split function for a dataframe and returns both the Training and Testing sets. Frac referes to the precent of data you would like to set aside for training.
"""
def train_test_split(df, frac):
    df_length = len(df)
    cutoff = round(frac * df_length)
    return df[:cutoff], df[cutoff:]

"""
Develop a randomization function that randomizes all of a dataframes cells then returns that randomized dataframe. This function should also take a random seed for reproducible randomization.
"""
def randomize(df, seed):
    # randomize index
    df = df.sample(frac=1, axis=0, random_state=seed)
    # randomize columns
    df = df.sample(frac=1, axis=1, random_state=seed)
    return df

"""
Function to split dates of format "MM/DD/YYYY" into multiple columns (df['month'], df['day'], df['year']) and then return the same dataframe with those additional columns.
data = np.array(['02/28/2006', '03/09/2010', '06/12/1850'])
ser = pd.Series(data)
"""
def split_dates(pd_series):
    df = pd.DataFrame()
    data = np.array(['02/28/2006', '03/09/2010', '06/12/1850'])
    ser = pd.Series(data=data, name='Dates')
    df[['month', 'day', 'year']] = ser['Dates'].str.split("/")
    return df