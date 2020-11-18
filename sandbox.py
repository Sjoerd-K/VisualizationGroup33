# --------------
datapath = r'./archive/dataset.xlsx'

print("importing modules...",end='')
from matplotlib import axes
import pandas as pd
print("done")

print(f"loading data ({datapath})...", end=' ')
dataset = pd.read_excel(datapath)
print("done")

print("showing info")

tabs = " "
for column in dataset.loc[:]:
    print(f"{column} :{(50 - len(column))*tabs} {5644 - dataset[column].isna().sum()}")