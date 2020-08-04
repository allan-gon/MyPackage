import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/allan-gon/Unit-2-Build/master/the_model_code/DATA/anime.csv")

def pretty_null(df):
    """
    Takes a dataframe and only prints the columns with null values and the amount
    of nulls
    :param df: Dataframe
    :return: None
    """
    cols = df.columns
    nulls = df.isnull().sum()
    print("Columns".ljust(20, " "), "Number of Nans")  # some right justified words
    if all(_ == 0 for _ in nulls):
        print('There are no nans in the dataframe')
    else:
        for i in range(len(cols)):
            if nulls[i] > 0:
                print(f"{cols[i].ljust(20, ' ')} {nulls[i]}")
    return ""

def add_col_from_list(df, iterable, col_name):
    """
    Adds a column to a dataframe
    :param df: Dataframe
    :param iterable: A 1 dimensional list like object
    :param col_name: the desired name for the new column
    :return: The DataFrame with a new column
    """
    df[col_name] = pd.Series(iterable)
    return df