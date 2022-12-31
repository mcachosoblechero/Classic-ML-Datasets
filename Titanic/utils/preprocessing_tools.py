def perc_missing_vals(df):
    """
    Print the percentage of missing values on a dataset
    :param df: Dataframe with all records in a dataset
    """
    missing_vals_train = df.isnull().sum() / df.shape[0] * 100
    print(missing_vals_train.sort_values(ascending=False))