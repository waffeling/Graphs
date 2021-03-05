from bokeh.plotting import Figure, show, output_file
from bokeh.models import Div, CustomJS, Slider, ColumnDataSource
from bokeh.io import show, curdoc
from bokeh.layouts import layout, column
from math import pi
import numpy as np


x = np.linspace(0, 2*np.pi, 200)
y = np.sin(x)


data = dict(x=x, y=y)
source = ColumnDataSource(data=data)

plot = Figure(title="Sine Graph")
plot.line('x', 'y', source=source, legend_label="y=sin(x)", line_width=2,)

freq = Slider(start=0.1, end=2, value=1, step=0.1, title="Frequency")

def update(attrname, old, new):
    b = freq.value

    x = np.linspace(0, 2*np.pi, 200)

    y = np.sin(b*x)

    source.data = dict(x=x, y=y)

freq.on_change('value', update)


column = column(freq, plot)
curdoc().add_root(column)
curdoc().title = "Change the frequency!"





