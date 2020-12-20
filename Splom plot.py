import pandas as pd

from bokeh.models import ColumnDataSource, Jitter, Legend, LegendItem
from bokeh.layouts import column, gridplot
from bokeh.models.annotations import Legend
from bokeh.plotting import figure, output_file, show
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
del dfNegative['SARS-Cov-2 exam result']

print(dfPositive)

# set output file
output_file("test.html", title = "Scatter visualization of blood tests")

dcPositive = dfPositive.to_dict("list")
dcNegative = dfNegative.to_dict("list")

#print(dcBlood['Patient age quantile'])

list = list(dcPositive)

list.remove('Patient age quantile')

figures = []

sourcePos = ColumnDataSource(dfPositive)
sourceNeg = ColumnDataSource(dfNegative)

posLeg = []
negLeg = []

colorPositive = "blue"
colorNegative = "red"

for index in list:
    scatter = figure(title = index, plot_width=500, plot_height=300, tools = "save, pan, reset, wheel_zoom", x_axis_label='age quantile', y_axis_label='standardized test result')

    p = scatter.circle(x=jitter("Patient age quantile", 0.5), y= index, size=4, color=colorPositive, alpha=0.5, source = sourcePos, muted_alpha=0.1)
    n = scatter.circle(x=jitter("Patient age quantile", 0.5), y= index, size=4, color=colorNegative, alpha=0.5, source = sourceNeg, muted_alpha=0.1)

    posLeg.append(("Covid-19 positive", [p]))
    negLeg.append(("Covid-19 negative", [n]))

    legend = Legend(items=posLeg + negLeg)

    legend.click_policy = "mute"

    scatter.add_layout(legend, 'right')

    posLeg.clear()
    negLeg.clear()

    figures.append(scatter)

splom = gridplot([[figures[0], figures[1], figures[2]],
                  [figures[3], figures[4], figures[5]],
                  [figures[6], figures[7], figures[8]],
                   [figures[9], figures[10], figures[11]]])

show(splom)
#goals: scatter plots of the blood laboratory tests next to each other. With the color showing positive and negative test results.