import pandas as pd

df = pd.read_csv(r"C:\Users\DELL\mine\Data_dvc\data\newdata.csv")

df.drop('has_diabetes', inplace=True, axis=1)
#print(df)

diabetes_map = {True:1, False:0}
df['diabetes'] = df['diabetes'].map(diabetes_map)
#print(df.head())
df.drop('thickness', inplace=True, axis=1)
print(df.head())

