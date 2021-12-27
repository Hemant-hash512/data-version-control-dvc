import pandas as pd

df = pd.read_csv(r"D:\Data-version-control\data\data.csv")

df.drop('has_diabetes', inplace=True, axis=1)
#print(df)

diabetes_map = {True:1, False:0}
df['diabetes'] = df['diabetes'].map(diabetes_map)
#print(df.head())
df.drop('insulin', inplace=True, axis=1)
df.to_csv('data\data1.csv')
print(df.head())

