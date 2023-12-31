# Conventionally pandas is imported as pd
import pandas as pd

""" DataFrame Visualization """

# When using a dictionary of lists, the dictionary keys will be
# used as column headers and the values in each list as DataFrame rows
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

print(df)

""" Acessing DataFrame columns (Series) """

name_column = df["Name"]
age_column = df["Age"]
sex_column = df["Sex"]

#  When selecting a single column from a DataFrame, the result is a Series object
print(name_column, age_column, sex_column, sep='\n\n')

""" Creating a Series (column) """

name = pd.Series("A B C".split(), name="Division")
ages = pd.Series([17, 18, 19], name="Age")
sex = pd.Series(sex for sex in ('Male', 'Female'))

print(name)
print(ages)
print(sex)

""" Some DataFrame methods """

print("\nMax in Age Column/Series", age_column.max(), sep='\n')
print(ages.max())

print("\nMedian in Age Column/Series", age_column.median(), sep='\n')
print(ages.median())

print("\nMin in Age Column/Series", age_column.min(), sep='\n')
print(ages.min())

# Describe() method provides a general and fast Vision of the numeric data one by one
print(df.describe())
