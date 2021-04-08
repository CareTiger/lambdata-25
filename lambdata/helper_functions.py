import numpy as np
import pandas as pd
import math
from sklearn.utils import shuffle

class HelperClass:

    dict = {'First Score':[100, 90, np.nan, 95],
            'Second Score': [30, 45, 56, np.nan],
            'Third Score':[np.nan, 40, 80, 98]}
    df_test = pd.DataFrame(dict)


    def __init__(self):
        pass

    """
    Check a dataframe for nulls and return the number of missing values.
    test data:
    dict = {'First Score':[100, 90, np.nan, 95],
            'Second Score': [30, 45, 56, np.nan],
            'Third Score':[np.nan, 40, 80, 98]}
    df = pd.DataFrame(dict)
    """
    def null_count(self, df=df_test):
        if isinstance(df, pd.DataFrame):
            return df.isnull().sum().sum()
        else:
            print("You have passed an invalid datatype. Please pass a Pandas DataFrame.")


    """
    Create a Train/Test split function for a dataframe and returns both the Training and Testing sets. Frac referes to the precent of data you would like to set aside for training.
    test data:
    frac=0.2
    df = pd.DataFrame({'num_legs': [2, 4, 8, 0],
                    'num_wings': [2, 0, 0, 0],
                    'num_specimen_seen': [10, 2, 1, 8]})
    """
    def train_test_split(self, df, frac):
        if isinstance(df, pd.DataFrame):
            df_length = len(df)
            cutoff = math.ceil(frac * df_length)

            # df = df.sample(frac=1)
            df = shuffle(df)
            df.reset_index(inplace=True, drop=True)
            return df[:cutoff], df[cutoff:]
        else:
            print("You have passed an invalid datatype. Please pass a Pandas DataFrame.")


    """
    Develop a randomization function that randomizes all of a dataframes cells then returns that randomized dataframe. This function should also take a random seed for reproducible randomization.
    test data:
    df = pd.DataFrame({'num_legs': [2, 4, 8, 0],
                    'num_wings': [2, 0, 0, 0],
                    'num_specimen_seen': [10, 2, 1, 8]})
    """
    def randomize(self, df, seed):
        # randomize index
        df = df.sample(frac=1, axis=0, random_state=seed)
        # randomize columns
        df = df.sample(frac=1, axis=1, random_state=seed)
        return df


    """
    Function to split dates of format "MM/DD/YYYY" into multiple columns (df['month'], df['day'], df['year']) and then return the same dataframe with those additional columns.
    test data:
    data = np.array(['02/28/2006', '03/09/2010', '06/12/1850'])
    ser = pd.Series(data, name='Dates')
    """
    def split_dates(self, ser):
        # get column name
        key_name = ser.name
        # convert series to data frame
        ser = ser.to_frame()
        ser[['month', 'day', 'year']] = ser[key_name].str.split("/", expand=True)
        return ser