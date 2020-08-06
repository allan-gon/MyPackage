# What is it?
A cool package with some DS helper functions

Adds small functionality to pandas and sklearn
# Main features
Pandas can show how many nulls exist in each columns with .isnull().sum() but this kinda sucks when you have a ton of columns but only a few with nulls in them so what my pretty_null function does it it only shows what columns have nulls and how many.

It also instead prints out "There are no nans in the dataframe" if it finds no nans in any column


The function train_val_test_split is an extension of sklearn's train test split. It instead does 3 splits one for trainig, testing, and validation.
