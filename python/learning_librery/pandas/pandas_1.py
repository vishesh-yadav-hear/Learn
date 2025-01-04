import pandas as pd
import numpy as np

# Creating a Serise

list1 = ["one","two","three","four"]

sr = pd.Series(list1)


print(sr)
print(type(sr))



# Create a DataFrame

dic1 = {
    "name": ['harry', 'rohan', 'skill', 'shubh'],
    "marks": [12, 34, 24, 67],
    "city": ['rampur', 'kolkata', 'bareilly', 'goa']
}

df = pd.DataFrame(dic1)

# Save the DataFrame to a CSV file
#df.to_csv('dic2.csv', index=False)

# Read the CSV file
#df = pd.read_csv('dic2.csv')
df['marks'][0]=23
df.index = ['hi','hi2','hi3','hi4']
print(df)
print(df.describe())
print(df.index)
df = df.T
print(df)
df = df.T
print(df)
df = df.loc['hi','name']
print(df)


df = pd.DataFrame(dic1)
df = df.iloc[0,0]
print(df)


df = pd.DataFrame(dic1)

df1 = df.drop(0).copy()
print(df)
print(df1)
df1 = df1.reset_index(drop=True)
print(df1 + 12)