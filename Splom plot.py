from bokeh.models import ColumnDataSource
from bokeh.layouts import column, gridplot
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

dfPosAge = dfPositive['Patient age quantile']
dfNegAge = dfNegative['Patient age quantile']

del dfPositive['SARS-Cov-2 exam result']
del dfPositive['Patient age quantile']
del dfNegative['SARS-Cov-2 exam result']
del dfNegative['Patient age quantile']

print(dfPositive)

# set output file
output_file("test.html")

dcPositive = dfPositive.to_dict("list")
dcNegative = dfNegative.to_dict("list")

#print(dcBlood['Patient age quantile'])

list = list(dcPositive)

print(dcPositive[list[0]])

figures = []

for index in dcPositive:
    scatter = figure(title = index, plot_width=200, plot_height=200, tools = "save, pan, reset, wheel_zoom")
    scatter.circle(dfPosAge, dcPositive[index], size=5, color="green", alpha=0.5)
    scatter.circle(dfNegAge, dcNegative[index], size=5, color="red", alpha=0.5)

    figures.append(scatter)

splom = gridplot([[figures[0], figures[1], figures[2]],
                  [figures[3], figures[4], figures[5]],
                  [figures[6], figures[7], figures[8]],
                  [figures[9], figures[10], figures[11]]])

show(splom)
#goals: scatter plots of the blood laboratory tests next to each other. With the color showing positive and negative test results.