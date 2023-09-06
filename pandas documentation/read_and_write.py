import pandas as pd

# Pandas supports many different file formats or data
# Sources out of the box each of them with the prefix read_*
titanic = pd.read_csv('./databases/titanic.csv')


""" Acessing first * rows in a pandas DataFrame """

print(titanic.head(n=6))


""" Checking on how Pandas interpreted each of the column data types """

# Dtypes is a atribute of titanic DataFrame instance
print(titanic.dtypes)


""" Converting CSV to XLSX and JSON """

titanic.to_json("titanic.json")
titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)

excel_titanic = pd.read_excel("./databases/Titanic.xlsx")
json_titanic = pd.read_json("./databases/Titanic.json")

print(excel_titanic.head(1))
print(json_titanic.head(2))


""" Taking a technical resume (metadata) of the DataFrame """

titanic.info()
print('\n\n', titanic.describe())
