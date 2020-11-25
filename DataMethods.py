import matplotlib.pyplot as plt
import pandas as pd
version = 1.0 # version of the script module
"""
DataMethods (DM) v. 1.0
goal: provide simple to use methods to acces the data from the dataset, without all the fuss of pandas
"""

directory = r'./archive/'  # directory where all the data is stored

# Initializing =========================================================================================

print(f"DM: Loading modules...",end=' ')
from matplotlib import axes
import pandas as pd
print("done")

print(f"DM: loading data ({directory+'dataset.xlsx'})...", end=' ')
dataset = pd.read_excel(directory+'dataset.xlsx')
print("done")

# Dataset Modification =================================================================================

dataset = dataset.set_index('Patient ID')  # set index to Patient ID

# Methods ==============================================================================================

# gives a specific row of the dataset
# returns: dictionary with each entry being an atribute (column) of the row: 
# key: atrribute, val: any   ->   { atribute(string) : value (any) }
def getRow(Patient_ID=None, index=None):
    if (Patient_ID == None) and (index == None):
        raise ValueError (f"Either Patient_ID or index must be given, neither are: ({Patient_ID}, {index})")

    returndict = {}  # dictonairy with key: column and value: cells of the row of the property.
    for col in dataset.columns.values:
        if Patient_ID != None: returndict[col] = dataset[col][Patient_ID]
        if index != None: returndict[col] = dataset[col].iloc[index]

    return returndict

# gives a specific column of the dataset
# returns: array (when ID_index = False) or dictionary (when ID_index = True)
# where each value is an entry in the dataset for that column (atrribute)
# when ID_index = true, values are stored in a dictionary with their keys corresponding to their original index (Patient_ID)
def getColumn(Attribute, ID_index = False):
    if Attribute not in dataset.columns.values:
        errormessage = f"{Attribute} is not a valid property in the dataset.must be one of:{dataset.columns.values}"
        raise KeyError (errormessage)
    
    if ID_index: returner = {}
    else: returner = []

    for i in range(len(dataset.index)):
        if ID_index: returner[dataset[Attribute].iloc[[i]].index.values[0]] = dataset[Attribute].iloc[i]
        else: returner.append(dataset[Attribute].iloc[i])
    
    return returner

# gives a specfic value of a patient with (Patient_ID or index) for the specified property (column)
# returns: any (single value)
def getValByID(Patient_ID, property, index=None):
    if property not in dataset.columns.values:
        errormessage = f"{property} is not a valid property in the dataset.must be one of:{dataset.columns.values}"
        raise KeyError (errormessage)
    return dataset[property][Patient_ID]

# debugging ============================================================================================

# this means the code only get called when this script is called as the main script, not as a module
if __name__ == '__main__':  
    for key in getRow(index=8).keys():
        val = getRow(index=8)[key]
        print(key, ((60-len(str(key)))*" "), val )