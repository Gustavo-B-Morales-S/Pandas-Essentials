import pandas as pd

titanic = pd.read_csv("./databases/titanic.csv")


""" Acessing specific columns """

# A pandas Series is One-Dimensional and only the number of rows is returned
ages = titanic["Age"]
print(ages.head(), f"\nType of a single column object: {type(ages)}\n")

# To select multiple columns, use a list of column names within the selection brackets []
age_sex = titanic[["Age", "Sex"]]
print(age_sex.head(), '\n')

# To know how many columns and rows have in table
lines, columns = age_sex.shape
print(f"Lines of age_sex dataframe: {lines}")
print(f"Columns of age_sex dataframe: {columns}")
print(f"Type of Age_Sex: {type(age_sex)}")

""" Filtering values in a dataframe """

above_35 = titanic[(titanic["Age"] > 35) & (titanic["Survived"] == 1)]
print(above_35.head())

class_23 = titanic[titanic["Pclass"].isin([2, 3])]
print(class_23.head())

age_no_nan = titanic[titanic["Age"].notna()]
print(age_no_nan.head())
