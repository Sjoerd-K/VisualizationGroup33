# goals: scatter plots of the blood laboratory tests next to each other. With the color showing positive and negative test results.

# Import modules
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
    #'Serum Glucose', <-- averaged around 4 values per quantile, which is not enough
    ]

colorPositive = "blue"      # color of the positive markers
colorNegative = "red"       # color of the negative markers

# title of the plot
TITLE = "Several blood chemicals versus Age quantile"

''' Data cleaning =============================================================='''
# selecting the required data
df_blood = df[SELECTION].copy()
print(df_blood)

# seperating dataset by negative and positive test results
dfPositive = df_blood[df_blood['SARS-Cov-2 exam result'] == "positive"]
dfNegative = df_blood[df_blood['SARS-Cov-2 exam result'] == "negative"]

# seperating age quantiles of negative and positive patients
dfPosAge = dfPositive['Patient age quantile']
dfNegAge = dfNegative['Patient age quantile']

# removing datasets that are no longer needed
del dfPositive['SARS-Cov-2 exam result']
del dfNegative['SARS-Cov-2 exam result']

print(dfPositive)

# set output file
output_file("test.html", title = "Scatter visualization of blood tests")

# convert dataframes to dictionaries
dcPositive = dfPositive.to_dict("list")
dcNegative = dfNegative.to_dict("list")

#print(dcBlood['Patient age quantile'])

list = list(dcPositive)                         # create list with all columns names of the dataset (which also includes age)
list.remove('Patient age quantile')             # remove ages from list, as they are already seperated into their own variable

figures = []                                    # list of figures to be made

# convert dataframes to datasources for the figures
sourcePos = ColumnDataSource(dfPositive)
sourceNeg = ColumnDataSource(dfNegative)


for index in list:                                  # for every blood column in the dataset...

    # lists for the Legends of the plot
    posLeg = []
    negLeg = []

    scatter = figure(                                   # make a scatterplot with the following properties...
        title = index,                                  # sets the titel of the plot to the name of the column
        plot_width=500,                                 # plot width in pixels
        plot_height=300,                                # plot height in pixels
        tools = "save, pan, reset, wheel_zoom",         # interaction tools with the plot
        x_axis_label='age quantile',                    # x-axis data from the source
        y_axis_label='standardized test result'         # y-axis data from the source
    )

    # paint data in the 'index' column as scattered circles
    p = scatter.circle(                                 # ... make point for the scatterplots with...
        x = jitter("Patient age quantile", 0.5),        # ... 'Patient age quantile' as x-coordinate
        y = index,                                      # ... 'index' (current blood chemical) as y-coordinate
        size = 4,                                       # size of the circles in pixels
        color = colorPositive,                          # color of the dots
        alpha = 0.5,                                    # opacity of the dots
        source = sourcePos,                             # datasource for the dots (positive patients only)
        muted_alpha = 0.1                               # opacity of dots that are disabled by the user when clicking on the legend item
    )
    n = scatter.circle(                                 # ... make point for the scatterplots with...
        x=jitter("Patient age quantile", 0.5),          # ... 'Patient age quantile' as x-coordinate
        y= index,                                       # ... 'index' (current blood chemical) as y-coordinate
        size=4,                                         # size of the circles in pixels
        color=colorNegative,                            # color of the dots
        alpha=0.5,                                      # opacity of the dots
        source = sourceNeg,                             # datasource for the dots (negative patients only)
        muted_alpha=0.1                                 # opacity of dots that are disabled by the user when clicking on the legend item
    )

    # add the painted dots to the Legend
    posLeg.append(("Covid-19 positive", [p]))
    negLeg.append(("Covid-19 negative", [n]))

    # construct the legend
    legend = Legend(items=posLeg + negLeg)              # create Legend object
    legend.click_policy = "mute"                        # specify what happens when the user click on a legend item
    scatter.add_layout(legend, 'right')                 # position of the Legend relative to the corresponding plot

    figures.append(scatter)                             # ... add the scatterplot to the list of figures

# create grid of plots using a list comprehension, this creates a list of lists where each inner list contains 3 consequtive elements from 'figures',
# !! this only works if the length of 'figures' is exactly divisable by 3.  !!
splom = gridplot([ [figures[i], figures[i+1], figures[i+2] ] for i in range(0, len(figures)-1, 3) ])

show(splom)  # show the plots on the page
