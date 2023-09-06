import pandas as pd

# Pandas supports many different file formats or data
# sources out of the box each of them with the prefix "read_*""
titanic = pd.read_csv('./databases/titanic.csv')


# Acessing first N rows in a pandas DataFrame 
print(titanic.head(n=6))

# Checking on how Pandas interpreted each of the column data types 
print(titanic.dtypes)


# Converting CSV to XLSX and JSON 
titanic.to_json("titanic.json")
json_titanic = pd.read_json("./databases/Titanic.json")

titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
excel_titanic = pd.read_excel("./databases/Titanic.xlsx")

print(excel_titanic.head())
print(json_titanic.head())


""" Taking a technical resume (metadata) of the DataFrame """

titanic.info()
print(titanic.describe())
