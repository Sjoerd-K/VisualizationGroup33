from bokeh.models import ColumnDataSource, Legend
from bokeh.plotting import figure, output_file, show
from bokeh.models.widgets import Panel, Tabs
from bokeh.layouts import column, row, layout, widgetbox, grid, GridBox, gridplot
from bokeh.models import CustomJS, Slider, Toggle, Dropdown, MultiChoice, Spinner, Select
from bokeh.transform import dodge
from bokeh.palettes import RdBu as colors
from bokeh.models import ColorBar, LinearColorMapper, HoverTool, BoxSelectTool
import pandas as pd
import bisect
from bokeh.io import output_file,show
from math import pi
from numpy import arange
from itertools import chain
from collections import OrderedDict
import holoviews as hv
import holoviews.plotting.bokeh
import numpy as np
import param
import panel as pn
import altair as alt
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import hvplot.pandas
pn.extension('vega', 'plotly')

from bokeh.io import output_file, show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Div
from bokeh.models.widgets import Paragraph
from bokeh.models.widgets import PreText



#disable default plotly theme
import plotly.io as pio
pio.templates.default = None

plot = figure(tools="pan,wheel_zoom,box_zoom,reset")
plot.add_tools(BoxSelectTool(dimensions="width"))
output_file("test.html")
df = pd.read_excel(
    r'C:\Users\20182025\Documents\Jaar 3 PT\JBI100\Python\dataset.xlsx')

# tab 1 - Assignment 4 visualisation
regularWardPos = [0, 0, 0, 0, 0]
semiIntensivePos = [0, 0, 0, 0, 0]
intensivePos = [0, 0, 0, 0, 0]

totalAgePos = [0, 0, 0, 0, 0]

regularWardNeg = [0, 0, 0, 0, 0]
semiIntensiveNeg = [0, 0, 0, 0, 0]
intensiveNeg = [0, 0, 0, 0, 0]

totalAgeNeg = [0, 0, 0, 0, 0]

for index, row in df.iterrows():
    if df.iloc[index, 1] == 0 or df.iloc[index, 1] == 1 or df.iloc[index, 1] == 2 or df.iloc[index, 1] == 3:
        if df.iloc[index, 2] == "positive":
            totalAgePos[0] += 1
            if df.iloc[index, 3] == 1:
                regularWardPos[0] += 1
            elif df.iloc[index, 4] == 1:
                semiIntensivePos[0] += 1
            elif df.iloc[index, 5] == 1:
                intensivePos[0] += 1

        if df.iloc[index, 2] == "negative":
            totalAgeNeg[0] += 1
            if df.iloc[index, 3] == 1:
                regularWardNeg[0] += 1
            elif df.iloc[index, 4] == 1:
                semiIntensiveNeg[0] += 1
            elif df.iloc[index, 5] == 1:
                intensiveNeg[0] += 1

    elif df.iloc[index, 1] == 4 or df.iloc[index, 1] == 5 or df.iloc[index, 1] == 6 or df.iloc[index, 1] == 7:
        if df.iloc[index, 2] == "positive":
            totalAgePos[1] += 1
            if df.iloc[index, 3] == 1:
                regularWardPos[1] += 1
            elif df.iloc[index, 4] == 1:
                semiIntensivePos[1] += 1
            elif df.iloc[index, 5] == 1:
                intensivePos[1] += 1

        if df.iloc[index, 2] == "negative":
            totalAgeNeg[1] += 1
            if df.iloc[index, 3] == 1:
                regularWardNeg[1] += 1
            elif df.iloc[index, 4] == 1:
                semiIntensiveNeg[1] += 1
            elif df.iloc[index, 5] == 1:
                intensiveNeg[1] += 1

    elif df.iloc[index, 1] == 8 or df.iloc[index, 1] == 9 or df.iloc[index, 1] == 10 or df.iloc[index, 1] == 11:
        if df.iloc[index, 2] == "positive":
            totalAgePos[2] += 1
            if df.iloc[index, 3] == 1:
                regularWardPos[2] += 1
            elif df.iloc[index, 4] == 1:
                semiIntensivePos[2] += 1
            elif df.iloc[index, 5] == 1:
                intensivePos[2] += 1

        if df.iloc[index, 2] == "negative":
            totalAgeNeg[2] += 1
            if df.iloc[index, 3] == 1:
                regularWardNeg[2] += 1
            elif df.iloc[index, 4] == 1:
                semiIntensiveNeg[2] += 1
            elif df.iloc[index, 5] == 1:
                intensiveNeg[2] += 1

    elif df.iloc[index, 1] == 12 or df.iloc[index, 1] == 13 or df.iloc[index, 1] == 14 or df.iloc[index, 1] == 15:
        if df.iloc[index, 2] == "positive":
            totalAgePos[3] += 1
            if df.iloc[index, 3] == 1:
                regularWardPos[3] += 1
            elif df.iloc[index, 4] == 1:
                semiIntensivePos[3] += 1
            elif df.iloc[index, 5] == 1:
                intensivePos[3] += 1

        if df.iloc[index, 2] == "negative":
            totalAgeNeg[3] += 1
            if df.iloc[index, 3] == 1:
                regularWardNeg[3] += 1
            elif df.iloc[index, 4] == 1:
                semiIntensiveNeg[3] += 1
            elif df.iloc[index, 5] == 1:
                intensiveNeg[3] += 1

    elif df.iloc[index, 1] == 16 or df.iloc[index, 1] == 17 or df.iloc[index, 1] == 18 or df.iloc[index, 1] == 19:
        if df.iloc[index, 2] == "positive":
            totalAgePos[4] += 1
            if df.iloc[index, 3] == 1:
                regularWardPos[4] += 1
            elif df.iloc[index, 4] == 1:
                semiIntensivePos[4] += 1
            elif df.iloc[index, 5] == 1:
                intensivePos[4] += 1

        if df.iloc[index, 2] == "negative":
            totalAgeNeg[4] += 1
            if df.iloc[index, 3] == 1:
                regularWardNeg[4] += 1
            elif df.iloc[index, 4] == 1:
                semiIntensiveNeg[4] += 1
            elif df.iloc[index, 5] == 1:
                intensiveNeg[4] += 1

percentageRegularWardPos = [0, 0, 0, 0, 0]
percentageSemiIntensivePos = [0, 0, 0, 0, 0]
percentageIntensivePos = [0, 0, 0, 0, 0]

percentageRegularWardNeg = [0, 0, 0, 0, 0]
percentageSemiIntensiveNeg = [0, 0, 0, 0, 0]
percentageIntensiveNeg = [0, 0, 0, 0, 0]

for i in range(len(regularWardPos)):
    percentageRegularWardPos[i] = regularWardPos[i] / (totalAgePos[i]+totalAgeNeg[i]) * 100
    percentageSemiIntensivePos[i] = semiIntensivePos[i] / (totalAgePos[i]+totalAgeNeg[i]) * 100
    percentageIntensivePos[i] = intensivePos[i] / (totalAgePos[i]+totalAgeNeg[i]) * 100

    percentageRegularWardNeg[i] = regularWardNeg[i] / (totalAgePos[i]+totalAgeNeg[i]) * 100
    percentageSemiIntensiveNeg[i] = semiIntensiveNeg[i] / (totalAgePos[i]+totalAgeNeg[i]) * 100
    percentageIntensiveNeg[i] = intensiveNeg[i] / (totalAgePos[i]+totalAgeNeg[i]) * 100

wardDevision = ["regular ward", "semi-intensive unit", "intensive care"]

ageDevision = ["child and teen", "young adult and adult", "middle aged", "senior", "elderly"]

positiveReg = ["regular ward positive", "regular ward negative"]
positiveSemi = ["semi-intensive unit positive", "semi-intensive unit negative"]
positiveIntens = ["intensive care positive", "intensive care negative"]

bdictDataReg = {'age group': ageDevision,
                "regular ward positive": percentageRegularWardPos,
                "regular ward negative": percentageRegularWardNeg}

bdictDataSemi = {'age group': ageDevision,
                 "semi-intensive unit positive": percentageSemiIntensivePos,
                 "semi-intensive unit negative": percentageSemiIntensiveNeg}

bdictDataIntens = {'age group': ageDevision,
                   "intensive care positive": percentageIntensivePos,
                   "intensive care negative": percentageIntensiveNeg}

ndictDataReg = {'age group': ageDevision,
                "regular ward negative": percentageRegularWardNeg}

ndictDataSemi = {'age group': ageDevision,
                 "semi-intensive unit negative": percentageSemiIntensiveNeg}

ndictDataIntens = {'age group': ageDevision,
                   "intensive care negative": percentageIntensiveNeg}

pdictDataReg = {'age group': ageDevision,
                "regular ward positive": percentageRegularWardPos}

pdictDataSemi = {'age group': ageDevision,
                 "semi-intensive unit positive": percentageSemiIntensivePos}

pdictDataIntens = {'age group': ageDevision,
                   "intensive care positive": percentageIntensivePos}

sourceReg = ColumnDataSource(data=bdictDataReg)
sourceSemi = ColumnDataSource(data=bdictDataSemi)
sourceIntens = ColumnDataSource(data=bdictDataIntens)

colorsReg = ["#2874A6", "#85C1E9"]
colorsSemi = ["#B03A2E", "#F5B7B1"]
colorsIntens = ["#B7950B", "#F9E79F"]

p1 = figure(x_range=ageDevision,
            title="Percentage of age group in hospital ward", toolbar_location=None,
            tools="", y_axis_label = "Age group specific percentage per hospital ward  ")

# dodge('age group', -0.25, range=chart.x_range)
list_stack = []
pos_reg_stack = p1.vbar_stack(positiveReg, x=dodge('age group', -0.25, range=p1.x_range), width=0.2, source=sourceReg,
              color=colorsReg, legend_label=positiveReg)
 # list_stack.append((pos_reg_stack), [pos_reg_stack])

pos_semi_stack= p1.vbar_stack(positiveSemi, x=dodge('age group', 0.0, range=p1.x_range), width=0.2, source=sourceSemi,
              color=colorsSemi, legend_label=positiveSemi)

pos_intens_stack = p1.vbar_stack(positiveIntens, x=dodge('age group', 0.25, range=p1.x_range), width=0.2, source=sourceIntens,
              color=colorsIntens, legend_label=positiveIntens)


p1.y_range.start = 0
p1.x_range.range_padding = 0.1
p1.xgrid.grid_line_color = None

p1.legend.location ="top_center"
# legend = Legend(items=list_stack)
# p1.add_layout(Legend(), 'right')
# p1.legend.location = "top_left"
p1.legend.orientation = "vertical"

# SELECT menu GUI
selectoptions = ["Postive tested on Covid-19 virus", "Negative tested on Covid-19 virus", "Show both"]
resultSelect = Select(title="What to show", options=selectoptions)


def update_plot(attrname, old, new):
    if resultSelect.value == 'Postive tested on Covid-19 virus':
        newReg = pdictDataReg
        newIntens = pdictDataIntens
        newSemi = pdictDataSemi
    if resultSelect.value == "Negative tested on Covid-19 virus":
        newReg = ndictDataReg
        newIntens = ndictDataIntens
        newSemi = ndictDataSemi
    if resultSelect.value == "Show both":
        newReg = bdictDataReg
        newIntens = bdictDataIntens
        newSemi = bdictDataSemi
    sourceReg.data = newReg
    sourceIntens.data = newIntens
    sourceSemi.data = newSemi


resultSelect.on_change("value", update_plot)

# def source_selector(selection):
#     if selection == "Postive tested on Covid-19 virus":
#         actualselection = positive
#     elif selection == "Negative tested on Covid-19 virus":
#         actualselection = negative
#     elif selection == "Show both":
#         actualselection = both
#     return actualselection
#
#
# def X_switch_selection_and_source(attr, old, new):
#     if new == '':
#         sourceReg = ColumnDataSource(data=dictDataReg)
#         sourceSemi = ColumnDataSource(data=dictDataSemi)
#         sourceIntens = ColumnDataSource(data=dictDataIntens)
#     new_x_values = source_selector(new)
#     sourcedf = pd.DataFrame({"X": new_x_values})
#     sourceReg = ColumnDataSource(data=dictDataReg)
#     sourceSemi = ColumnDataSource(data=dictDataSemi)
#     sourceIntens = ColumnDataSource(data=dictDataIntens)
#
#
# selectoptions.on_change("value", X_switch_selection_and_source)


# Visualisation 2 - Bar chart - Assignment 3
positiveAge = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
totalAge = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
percentageAge = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for index, row in df.iterrows():
    if df.iloc[index, 1] == 0:
        totalAge[0] += 1
        if df.iloc[index, 2] == "positive":
            positiveAge[0] += 1
    elif df.iloc[index, 1] == 1:
        totalAge[1] += 1
        if df.iloc[index, 2] == "positive":
            positiveAge[1] += 1
    elif df.iloc[index, 1] == 2:
        totalAge[2] += 1
        if df.iloc[index, 2] == "positive":
            positiveAge[2] += 1
    elif df.iloc[index, 1] == 3:
        totalAge[3] += 1
        if df.iloc[index, 2] == "positive":
            positiveAge[3] += 1
    elif df.iloc[index, 1] == 4:
        totalAge[4] += 1
        if df.iloc[index, 2] == "positive":
            positiveAge[4] += 1
    elif df.iloc[index, 1] == 5:
        totalAge[5] += 1
        if df.iloc[index, 2] == "positive":
            positiveAge[5] += 1
    elif df.iloc[index, 1] == 6:
        totalAge[6] += 1
        if df.iloc[index, 2] == "positive":
            positiveAge[6] += 1
    elif df.iloc[index, 1] == 7:
        totalAge[7] += 1
        if df.iloc[index, 2] == "positive":
            positiveAge[7] += 1
    elif df.iloc[index, 1] == 8:
        totalAge[8] += 1
        if df.iloc[index, 2] == "positive":
            positiveAge[8] += 1
    elif df.iloc[index, 1] == 9:
        totalAge[9] += 1
        if df.iloc[index, 2] == "positive":
            positiveAge[9] += 1
    elif df.iloc[index, 1] == 10:
        totalAge[10] += 1
        if df.iloc[index, 2] == "positive":
            positiveAge[10] += 1
    elif df.iloc[index, 1] == 11:
        totalAge[11] += 1
        if df.iloc[index, 2] == "positive":
            positiveAge[11] += 1
    elif df.iloc[index, 1] == 12:
        totalAge[12] += 1
        if df.iloc[index, 2] == "positive":
            positiveAge[12] += 1
    elif df.iloc[index, 1] == 13:
        totalAge[13] += 1
        if df.iloc[index, 2] == "positive":
            positiveAge[13] += 1
    elif df.iloc[index, 1] == 14:
        totalAge[14] += 1
        if df.iloc[index, 2] == "positive":
            positiveAge[14] += 1
    elif df.iloc[index, 1] == 15:
        totalAge[15] += 1
        if df.iloc[index, 2] == "positive":
            positiveAge[15] += 1
    elif df.iloc[index, 1] == 16:
        totalAge[16] += 1
        if df.iloc[index, 2] == "positive":
            positiveAge[16] += 1
    elif df.iloc[index, 1] == 17:
        totalAge[17] += 1
        if df.iloc[index, 2] == "positive":
            positiveAge[17] += 1
    elif df.iloc[index, 1] == 18:
        totalAge[18] += 1
        if df.iloc[index, 2] == "positive":
            positiveAge[18] += 1
    elif df.iloc[index, 1] == 19:
        totalAge[19] += 1
        if df.iloc[index, 2] == "positive":
            positiveAge[19] += 1

for i in range(len(positiveAge)):
    percentageAge[i] = positiveAge[i] / totalAge[i] * 100

print(positiveAge)
print(totalAge)
print(percentageAge)

ageQuantile = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18",
               "19"]

p2 = figure(x_range=ageQuantile, plot_height=250, title="Percentage positive tests per age quartile",
            toolbar_location=None, tools="", x_axis_label="Age quantiles", y_axis_label = "Percentage positive tests of all people per age group")

p2.vbar(x=ageQuantile, top=percentageAge, width=0.5)
# p2.line(ageQuantile, percentageAge, line_width = 2, line_color = 'red')
# p2.circle(ageQuantile, percentageAge, fill_color="red",line_color='red', size=8)

p2.xgrid.grid_line_color = None
p2.y_range.start = 0

# Visualisation 3 - Heat map - Assignment 3
dfVirus = df.iloc[:, 21:38]
dfVirus["SARS-Cov-2 exam result"] = df["SARS-Cov-2 exam result"]
del dfVirus['Mycoplasma pneumoniae']

for i in range(16):
    dfVirus.iloc[:, i] = dfVirus.iloc[:, i].replace(["not_detected"], 0)
    dfVirus.iloc[:, i] = dfVirus.iloc[:, i].replace(["detected"], 1)

dfVirus.iloc[:, 16] = dfVirus.iloc[:, 16].replace(["negative"], 0)
dfVirus.iloc[:, 16] = dfVirus.iloc[:, 16].replace(["positive"], 1)

correlation = dfVirus.corr()

colors = list(reversed(colors[11]))  # we want an odd number to ensure 0 correlation is a distinct color
labels = dfVirus.columns
nlabels = len(labels)


def get_bounds(n):
    """Gets bounds for quads with n features"""
    bottom = list(chain.from_iterable([[ii] * nlabels for ii in range(nlabels)]))
    top = list(chain.from_iterable([[ii + 1] * nlabels for ii in range(nlabels)]))
    left = list(chain.from_iterable([list(range(nlabels)) for ii in range(nlabels)]))
    right = list(chain.from_iterable([list(range(1, nlabels + 1)) for ii in range(nlabels)]))
    return top, bottom, left, right


def get_colors(corr_array, colors):
    """Aligns color values from palette with the correlation coefficient values"""
    ccorr = arange(-1, 1, 1 / (len(colors) / 2))
    color = []
    for value in corr_array:
        ind = bisect.bisect_left(ccorr, value)
        color.append(colors[ind - 1])
    return color


p3 = figure(plot_width=600, plot_height=600,
            x_range=(0, nlabels), y_range=(0, nlabels),
            title="Correlation Coefficient Heatmap",
            tools="save", toolbar_location="right")

p3.xgrid.grid_line_color = None
p3.ygrid.grid_line_color = None
p3.xaxis.major_label_orientation = pi / 4
p3.yaxis.major_label_orientation = pi / 4

top, bottom, left, right = get_bounds(nlabels)  # creates sqaures for plot
color_list = get_colors(correlation.values.flatten(), colors)

p3.quad(top=top, bottom=bottom, left=left,
        right=right, line_color='white',
        color=color_list)

# Set ticks with labels
ticks = [tick + 0.5 for tick in list(range(nlabels))]
tick_dict = OrderedDict([[tick, labels[ii]] for ii, tick in enumerate(ticks)])
# Create the correct number of ticks for each axis
p3.xaxis.ticker = ticks
p3.yaxis.ticker = ticks
# Override the labels
p3.xaxis.major_label_overrides = tick_dict
p3.yaxis.major_label_overrides = tick_dict

# Setup color bar
mapper = LinearColorMapper(palette=colors, low=-1, high=1)
color_bar = ColorBar(color_mapper=mapper, location=(0, 0))
p3.add_layout(color_bar, 'right')

# Spinner GUI
spinner = Spinner(title="Size", low=0, high=4, step=0.1, value=1, width=80)
# spinner.js_link('value', points.glyph, 'radius')

# Dropdown menu GUI
menu = [("Postive tested on Covid-19 virus", "item_1"), ("Negative tested on Covid-19 virus", "item_2"), None,
        ("Show both", "item_3")]
dropdown = Dropdown(label="Dropdown button", button_type="warning", menu=menu)
dropdown.js_on_event("menu_item_click", CustomJS(code="console.log('dropdown: ' + this.item, this.toString())"))

# Toggle button GUI
toggle = Toggle(label="Button", button_type="success")
toggle.js_on_click(CustomJS(code="""
    console.log('toggle: active=' + this.active, this.toString())
"""))
OPTIONS = ["Attribute1", "Attribute2", "Attribute3", "Attribute4"]
multi_choice = MultiChoice(value=["foo", "baz"], options=OPTIONS)
multi_choice.js_on_change("value", CustomJS(code="""
    console.log('multi_choice: value=' + this.value, this.toString())
"""))

# CheckboxGroup
# columns = ["Postive tested on Covid-19 virus", "Negative tested on Covid-19 virus"]
# checkbox = CheckboxGroup(labels=columns, active=[0, 1])
# callback = CustomJS(code="""positiveselect = false; // same xline passed in from args
#                             negativeselect = false;
#                             // cb_obj injected in by the callback
#                             if (cb_obj.active.includes(0)){positiveselect = true;} // 0 index box is Postive tested Covid-19
#                             if (cb_obj.active.includes(1)){negativeselect = true;}""",
#                     args={'positiveselect': positiveselect, 'negativeselect': negativeselect})
# checkbox.js_on_click(callback)

#heading
title = Div(
    text="<b>Visualisation tool of patients tested for Covid-19 of the Hospital Israelita Albert Einstein, at São Paulo, Brazil</b>",
    style={'font-size': '200%', 'color': 'black'},width = 800)

text = [title]



# gridplot
p = gridplot([[p1, p2], [None, p3]], plot_width=400, plot_height=400)

# plot sizes
p1.plot_width = 600
p1.plot_height = 600
p2.plot_width = 600
p2.plot_height = 600
p3.plot_width = 600
p3.plot_height = 600

# GUI Left column
controls = [dropdown, spinner, toggle, resultSelect]

l1 = layout([ p1], sizing_mode='fixed', height=600, width=150)
l2 = layout([p2], sizing_mode='fixed', height=600, width=150)
l3 = layout([ p3], sizing_mode='fixed', height=600, width=150)
# l4 = layout([ p], sizing_mode='fixed', height=600, width=600)

tab4 = Panel(child=l1, title="Division per hospital ward")
tab2 = Panel(child=l2, title="Age covid-19 patients")
tab3 = Panel(child=l3, title="Correlation virusses")
tab1 = Panel(child=p, title="All visualisations")


tabs = Tabs(tabs=[tab1, tab2, tab3, tab4])
# inputs = column(controls, sizing_mode='fixed', height=250, width=350)
layout = layout([[text], [controls, tabs],])
# r = row(children=[inputs, tabs], sizing_mode = 'stretch_both')
# layout = grid([dropdown, [[inputs, tabs]]])
# GridBox(children=[
#     (heading, 0, 0, 1, 2),
#     (inputs, 1, 0, 1, 1),
#     (tabs, 2, 0, 1, 1),
# ])
# layout = column(children = [inputs, tabs])
# Tab setup


show(layout)
