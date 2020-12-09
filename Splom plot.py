from bokeh.models import ColumnDataSource
from bokeh.models.annotations import Legend
from bokeh.plotting import figure, output_file, show
import pandas as pd

pd.set_option('display.max_columns', None)


# import the dataset
df = pd.read_excel("dataset.xlsx")

# select the data that is going te be plotted
SELECTION = [
    'SARS-Cov-2 exam result',
    'Patient age quantile',
    'Hematocrit',
    'Hemoglobin',
    'Platelets',
    'Red blood Cells',
    'Lymphocytes',
    'Mean corpuscular hemoglobin concentration (MCHC)',
    'Leukocytes',
    'Basophils',
    'Mean corpuscular hemoglobin (MCH)',
    'Eosinophils',
    'Mean corpuscular volume (MCV)',
    'Monocytes',
    'Red blood cell distribution width (RDW)',
    #'Serum Glucose', <-- averaged around 4 values per quantile, too few
    ]

# set of colors to be used for the lines & markers in the graph
COLORS = ['#C0C0C0','#808080','#800000','#FFFF00','#808000','#00FF00','#008000','#00FFFF','#008080','#0000FF','#000080','#FF00FF','#800080']

# title of the plot
TITLE = "Several blood chemicals versus Age quantile"

''' Data cleaning =============================================================='''
# selecting the required data
df_blood = df[SELECTION].copy()
print(df_blood)

# use pandas function to group the values by age, and then compute the mean
print(df_blood.groupby(['Patient age quantile']).mean())

# set output file
output_file("vis1.html")

# set source of the data to the selected data grouped by age
datasource = ColumnDataSource(df_blood.groupby(['Patient age quantile']))

print(datasource)

//goals: scatter plots of the blood laboratory tests next to each other. With the color showing positive and negative test results.