import pandas as pd
import numpy as np
from bokeh.plotting import figure, curdoc

bokeh_document = curdoc()

plot1 = figure(plot_height=600, plot_width=600, name = 'random_points')
plot1.circle(
    x=np.random.randint(low=0, high=50, size=(10,)),
    y=np.random.randint(low=0, high=50, size=(10,)),
    )

curdoc().add_root(plot1)
curdoc().title = "app2"
