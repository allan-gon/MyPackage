import pandas as pd
from sklearn.model_selection import train_test_split

# this is for testing pretty_null
DF = pd.read_csv("https://raw.githubusercontent.com/allan-gon/Unit-2-Build/master/the_model_code/DATA/anime.csv")


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
    return


def add_time(df, col_name):
    """
    Adds columns month, day, year to the dataframe and drops the original columns
    :param df: A pandas Dataframe
    :param col_name: A string of a column's name in the dataframe which is in datetime format
    :return: Dataframe with
    """
    df['year'] = df[col_name].dt.year
    df['month'] = df[col_name].dt.month
    df['day'] = df[col_name].dt.day
    df.drop(col_name, axis=1, inplace=True)


def train_val_test_split(df, target_col, test_size, val_size, random_state=None):
    """
    Preforms a train test val split on the data
    :param df: A pandas dataframe
    :param target_col: A string which is the target column's name
    :param test_size: A float, what percent of the data you want the train set to be
    :param val_size: A float, what percent of the data you want the validation set to be
    :param random_state: An integer, will be used for random state in sklearn's train test split
    :return: X_train, X_val, X_test, y_train, y_val, y_test
    """
    features = df.drop(target_col, axis=1)
    target = df[target_col]
    X, X_test, y, y_test = train_test_split(features, target, test_size=test_size, random_state=random_state)
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=val_size, random_state=random_state)
    return X_train, X_val, X_test, y_train, y_val, y_test

if __name__ == "__main__":
    X_train, X_val, X_test, y_train, y_val, y_test = train_val_test_split(DF, 'genre', .09, .1)
    print(f"X_train: {X_train.shape}")
    print(f"X_val: {X_val.shape}")
    print(f"X_test: {X_test.shape}")
    print(f"y_train: {y_train.shape}")
    print(f"y_train: {y_val.shape}")
    print(f"y_test: {y_test.shape}")
    # print(DF.columns)
    # train_val_test_split(DF, 'genre', .09, .1)
