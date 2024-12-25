# -----TASK--------
#Ek CSV file create karo jis mein students ke naam, marks (subjects-wise), aur attendance ho.
#Pandas ka use karke:
#   Average marks calculate karo.
#   Kis student ka performance best hai aur kaunsa improve karna chahiye.
#   Students ko grade assign karo.
#   Data ko CSV ya Excel file mein save karo.


import pandas as pd
import numpy as np

data = pd.read_csv('./learning_librery/pandas/projects/1/student_data.csv')

data_df = pd.DataFrame(data)

data_df['Average'] = data_df[['English','Hindi','Maths','GK','Computer']].mean(axis=1)

toper_st = data.loc[data_df['Average'].idxmax(), "Name"]
not_toper_st = data.loc[data_df['Average'].idxmin(), "Name"]

def avreg(avg):
    if avg >= 90:
        return "A"
    elif avg >=70:
        return "B"
    elif avg >= 45:
        return "C"
    else:
        return "D"
data_df['Grade'] = data_df['Average'].apply(avreg)

print(data_df)
print(f"Toper : {toper_st}")
print(f"Losser : {not_toper_st}")

data_df.to_csv('./learning_librery/pandas/projects/1/student_data_after_update.csv')