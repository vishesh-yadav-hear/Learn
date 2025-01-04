import pandas as pd

data =pd.read_csv('data.csv')
a = input("enter : ")
b = input("enter : ")
data.loc[len(data)] = [a,b]
data.to_csv('data.csv', index = False)
print(data)