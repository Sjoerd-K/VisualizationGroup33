import bokeh
from bokeh.models import ColumnDataSource
from bokeh.models.annotations import Legend
from bokeh.plotting import figure, output_file, show
from numpy.lib.utils import source
import pandas as pd

# configurables =======================================================================================================


SELECTION = [
    'Patient age quantile',  # patient age quantile is often usefull as index
    'SARS-Cov-2 exam result',
    'Patient addmited to regular ward (1=yes, 0=no)',
    'Patient addmited to semi-intensive unit (1=yes, 0=no)',
    'Patient addmited to intensive care unit (1=yes, 0=no)'
    # OTHER IMPORTS FROM DATASET HERE
]

GROUP = ['Patient age quantile']  # column to group data by

COLORS = ["red"] * (len(SELECTION)-2)  # defealt all colors are red
print(COLORS)


# data operations =====================================================================================================
print("Performing initial data operations...", end='\n');

# read data from excel file
print(f"Loading data: {SELECTION} from dataset.xlsx...",end='')
df = pd.read_excel("dataset.xlsx")  
data = df[SELECTION].copy()                         # removing not interesting attributes
print("done!")

# removing entries that don't contain enough data
print("removing NULL values...",end='')
blacklist = []                                      # list containing the indexes of entries to be removed
for i in range(len(data.index)):
    continue
    if data.iloc[i].isna().sum() > 2:
        blacklist.append(i)                         # select all rows where there are more than 2 entries missing

# remove the blacklisted entries by index
print(f"removing {len(blacklist)} entries...",end='')
data = data.drop(blacklist, axis='index')
print("done!")

# data splitting
data_positive = data[ data['SARS-Cov-2 exam result'] == 'positive' ].reset_index(drop=True)  # only postive test results
data_negative = data[ data['SARS-Cov-2 exam result'] == 'negative' ].reset_index(drop=True)  # only negative test results

# data grouping
data_positive = data_positive.groupby(GROUP)
data_negative = data_negative.groupby(GROUP)
print(f"postive test result:\n{data_positive.head()}\n")
print(f"negative test result:\n{data_negative.head()}\n")



# data packaging ======================================================================================================
print("Packaging data...",end='\n')

label_map = {  # decides which column in the dataset goes to which row in the package
    'Patient addmited to regular ward (1=yes, 0=no)'        : 'regular ward',
    'Patient addmited to semi-intensive unit (1=yes, 0=no)' : 'semi-intensive ward',
    'Patient addmited to intensive care unit (1=yes, 0=no)' : 'intensive care ward'
}

percentage_wards_positive = {                        # the structure of the data to be given to the plot function
    'regular ward'        : None,       # to be list of values for each x-axis entry
    'semi-intensive ward' : None,       # to be list of values for each x-axis entry
    'intensive care ward' : None,       # to be list of values for each x-axis entry

    'color'               : COLORS,     # to be list of colors to plot the bars in
    'labels'              : None,       # to be list of names for the legend
    'x-axis'              : [],         # to be list of values for the x-axis
    'y-axis'              : []          # to be list of value names for the y-axis
}
percentage_wards_negative = {                       # the structure of the data to be given to the plot function
    'regular ward'        : None,       # to be list of values for each x-axis entry
    'semi-intensive ward' : None,       # to be list of values for each x-axis entry
    'intensive care ward' : None,       # to be list of values for each x-axis entry

    'color'               : COLORS,     # to be list of colors to plot the bars in
    'labels'              : None,       # to be list of names for the legend
    'x-axis'              : [],         # to be list of values for the x-axis
    'y-axis'              : []          # to be list of value names for the y-axis
}

# positive dataset
for group_name, group in data_positive:
    percentage_wards_positive['x-axis'].append(group_name)

    for col in label_map.keys():
        percentage_wards_positive['y-axis'].append(col)
        percentage_wards_positive[label_map[col]] = 100 * sum(group[col].values)/len(group[col].values)

# negative dataset
for group_name, group in data_negative:
    percentage_wards_negative['x-axis'].append(group_name)
    for col in label_map.keys():
        percentage_wards_negative['y-axis'].append(col)
        percentage_wards_negative[label_map[col]] = 100 * sum(group[col].values)/len(group[col].values)

print("done!")
# =====================================================================================================================

output_file('barstest.html')

p = figure(plot_height=250, plot_width=600, title="positive test results")
p.vbar_stack('y-axis', x='x-axis', color = 'color', source = percentage_wards_positive)

show(p)