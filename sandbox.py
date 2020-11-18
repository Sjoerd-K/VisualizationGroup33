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
    goodvalues = 5644 - dataset[column].isna().sum()
    print(f"{column} :{(55 - len(column))*tabs} {goodvalues} :{(5 - len(str(goodvalues)))*tabs} {round(100*goodvalues/5644, 3)} %")