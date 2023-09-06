import pandas as pd

titanic = pd.read_csv("./databases/titanic.csv")

""" Loc DataFrame method """

# The part before the comma is the rows that you want, and the
# part after the comma is the columns you want to select
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
print(adult_names)


# Multiple conditional expressions can be made
# and multiple columns can be selected
names_and_ids_of_survived_minors = titanic.loc[
    (titanic["Survived"] == 1) & (titanic["Age"] < 18), ["Name", "PassengerId"]
]
print(names_and_ids_of_survived_minors)

slicing_rows_and_columns = titanic.loc[5:10, "PassengerId":"Name"]
print(slicing_rows_and_columns)


""" Iloc DataFrame method """

# When specifically interested in certain rows and/or columns
# based on their position in the table, use the iloc operator
print(titanic.iloc[9:25, 2:5])
