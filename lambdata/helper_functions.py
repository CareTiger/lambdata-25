
def null_count(df):
    return df.isnull().sum().sum()


def train_test_split(df, frac):
    df_length = len(df)
    cutoff = round(frac * df_length)
    return df[:cutoff], df[cutoff:]