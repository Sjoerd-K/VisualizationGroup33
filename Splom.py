import pandas as pd

from bokeh.models import ColumnDataSource, LegendItem
from bokeh.layouts import gridplot
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
    # 'Serum Glucose', <-- averaged around 4 values per quantile, too few
]

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
output_file("test.html", title="Scatter visualization of blood tests")

dcPositive = dfPositive.to_dict("list")
dcNegative = dfNegative.to_dict("list")

# print(dcBlood['Patient age quantile'])

bloodvaluelist = list(dcPositive)

bloodvaluelist.remove('Patient age quantile')

figures = []

sourcePos = ColumnDataSource(dfPositive)
sourceNeg = ColumnDataSource(dfNegative)

posneg_list = []
colorPositive = "blue"
colorNegative = "red"

for index in bloodvaluelist:
    #  for the first one don't use x_range, the remaining all will use the same x_range
    if index != "Hematocrit":
        scatter = figure(title=index, plot_width=400, plot_height=300, x_range=figures[0].x_range,
                         y_range=figures[0].y_range,
                         tools="save, pan, reset, wheel_zoom", x_axis_label='age quantile',
                         y_axis_label='standardized test result')
    else:
        scatter = figure(title=index, plot_width=400, plot_height=300, y_range=(-4, 4),
                         tools="save, pan, reset, wheel_zoom", x_axis_label='age quantile',
                         y_axis_label='standardized test result')
    p = scatter.circle(x=jitter("Patient age quantile", 0.5), y=index, size=4, color=colorPositive, alpha=0.5,
                       source=sourcePos, muted_alpha=0.1)
    n = scatter.circle(x=jitter("Patient age quantile", 0.5), y=index, size=4, color=colorNegative, alpha=0.5,
                       source=sourceNeg, muted_alpha=0.1)

    posneg_list += [p]
    posneg_list += [n]

    figures.append(scatter)

# Lines with the same color will share a same legend item
legend_items = [LegendItem(label="Covid-19 positive",
                           renderers=[thing for thing in posneg_list if thing.glyph.line_color == colorPositive]),
                LegendItem(label="Covid-19 negative",
                           renderers=[thing for thing in posneg_list if thing.glyph.line_color == colorNegative])]

# use a dummy figure for the legend
dum_fig = figure(plot_width=300, plot_height=600, outline_line_alpha=0, toolbar_location=None)
# set the components of the figure invisible
for fig_component in [dum_fig.grid[0], dum_fig.ygrid[0], dum_fig.xaxis[0], dum_fig.yaxis[0]]:
    fig_component.visible = False
# The points referred by the legend need to be present in the figure ,so add them to figure renderers
dum_fig.renderers += posneg_list
# set the figure range outside of the range of all glyphs
dum_fig.x_range.end = 1005
dum_fig.x_range.start = 1000
# add the legend
dum_fig.add_layout(Legend(click_policy='mute', location='top_left', border_line_alpha=0, items=legend_items))

# copy list to make it later possible to delete/ add items for the list without using original list (NOT YET USED)
show_figures = figures

splom = gridplot(show_figures, ncols=3, toolbar_location='right')
final = gridplot([[splom, dum_fig]], toolbar_location=None)

show(final)
# goals: scatter plots of the blood laboratory tests next to each other.
# With the color showing positive and negative test results.
