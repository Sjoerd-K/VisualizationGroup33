from bokeh.models import ColumnDataSource
from bokeh.layouts import column
from bokeh.models.annotations import Legend
from bokeh.plotting import figure, output_file, show
import pandas as pd
from bokeh.transform import jitter

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

dfPositive = df_blood[df_blood['SARS-Cov-2 exam result'] == "positive"]
dfNegative = df_blood[df_blood['SARS-Cov-2 exam result'] == "negative"]

dfNegative.drop(columns = ['SARS-Cov-2 exam result'])
dfPositive.drop(columns = ['SARS-Cov-2 exam result'])

# set output file
output_file("test.html")

dcPositive = dfPositive.to_dict("list")
dcNegative = dfNegative.to_dict("list")

#print(dcBlood['Patient age quantile'])

splom = figure(title = "Decathlon: Discus x Javeline")
splom.circle(jitter(dcPositive['Patient age quantile'], 0.1), dcPositive['Eosinophils'], size=20, color="green", alpha=0.5)
splom.circle(jitter(dcNegative['Patient age quantile'], 0.1), dcNegative['Eosinophils'], size=20, color="red", alpha=0.5)

show(splom)
#goals: scatter plots of the blood laboratory tests next to each other. With the color showing positive and negative test results.