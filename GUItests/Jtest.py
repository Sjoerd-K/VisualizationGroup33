import numpy as np
from bokeh.plotting import figure, curdoc
from bokeh.models.widgets import Button
from bokeh.layouts import column, widgetbox

def button_callback():
    """Add `num_points` circles to figure `fig`."""
    sample_plot.circle(x=np.random.normal(size=(10,)),
                       y=np.random.normal(size=(10,)))

def renderer_added(attr, old, new):
    print(f"attribute '{attr}' changed")

bokeh_doc = curdoc()

sample_plot = figure(plot_height=400, plot_width=400)

# Creating button to generate new points on the plot
button = Button(label="Generate", button_type="success")
button.on_click(button_callback)

sample_plot.on_change("renderers", renderer_added)

bokeh_doc.add_root(column([sample_plot, widgetbox(button, align="center")]))

bokeh_doc.title = "Bokeh App with a button and attribute callbacks."