def perc_missing_vals(df):
    """
    Print the percentage of missing values on a dataset
    :param df: Dataframe with all records in a dataset
    """
    missing_vals_train = df.isnull().sum() / df.shape[0] * 100
    print(missing_vals_train.sort_values(ascending=False))

def titanic_feature_extraction(df):
    """
    Perform the feature extraction for the Titanic dataset, as discussed in the EDA notebook
    :param df: Dataframe with all records
    :return: Dataframe with new features
    """
    # Extract whether the passenger has a cabin
    df['hasCabin'] = df.Cabin.notnull().apply(lambda x: 1 if x==True else 0)
    # Extract the passenger cabin letter
    df['cabinLetter'] = df.loc[df.Cabin.notnull()].Cabin.str[0]
    df['cabinLetter'] = df.cabinLetter.fillna(value="No Cabin")
    # Extract the number of cabins
    df['numCabins'] = df.loc[df.Cabin.notnull()].Cabin.str.split(" ").apply(len)
    df['numCabins'] = df.numCabins.fillna(value=0)
    # Determine the passenger is a female
    df['isFemale'] = df.Sex.apply(lambda x: 1 if x=="female" else 0)
    return df