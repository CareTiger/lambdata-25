
def null_count(df):
    return df.isnull().sum().sum()


def train_test_split(df, frac):
    df_length = len(df)
    return df_length, frac

    # df = utils.shuffle(df)
    # df1 = df[0:3]
    # df2 = df[3:6]