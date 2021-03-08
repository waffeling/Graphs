from bokeh.plotting import Figure, show, output_file
from bokeh.models import Div, CustomJS, Slider, ColumnDataSource
from bokeh.io import show, curdoc
from bokeh.layouts import layout, column
from math import pi
import numpy as np

t = 0
x = np.linspace(0, 16*np.pi, 200)
deltak = 0
deltaomega = 0

y1 = np.cos(x-t) + np.cos(((1+deltak)*x-(1+deltaomega)*t))
y2 = 3.5 + np.cos(x-t)
y3 = 3.5 + np.cos(((1+deltak)*x-(1+deltaomega)*t))
youtline1 = 2 * np.cos(((deltak)*x-(1+deltaomega)*t)/2)
youtline2 = -2 * np.cos(((deltak)*x-(1+deltaomega)*t)/2)
ys = list(np.array([y1, y2, y3, youtline1, youtline2]))

#print(ys)
x = np.repeat([x], 5, axis=0)
xs = list(x)
line_color = ["blue", "red", "orange", "gray", "gray"]
data = dict(xs=xs, ys=ys, linecolor=line_color)

source = ColumnDataSource(data=data)

plot = Figure(title="Group and Phase Speeds")
plot.multi_line('xs', 'ys', source=source, line_color='linecolor')

freq = Slider(start=0, end=2, value=0, step=0.01, title="Difference in Spatial Frequency")
deltao = Slider(start=-2, end=2, value=0, step=0.1, title="Difference in Temporal Frequency")
time = Slider(start=0, end=50, value=0, step=0.1, title="Time")

def update(attrname, old, new):
    deltak = freq.value
    deltaomega = deltao.value
    t = time.value
    x = np.linspace(0, 16 * np.pi, 200)


    y1 = np.cos(x - t) + np.cos(((1 + deltak) * x - (1 + deltaomega) * t))
    y2 = 3.5 + np.cos(x - t)
    y3 = 3.5 + np.cos(((1 + deltak) * x - (1 + deltaomega) * t))
    youtline1 = 2 * np.cos(((deltak) * x - (deltaomega) * t) / 2)
    youtline2 = -2 * np.cos(((deltak) * x - (deltaomega) * t) / 2)
    ys = list(np.array([y1, y2, y3, youtline1, youtline2]))

    # print(ys)
    x = np.repeat([x], 5, axis=0)
    xs = list(x)
    line_color = ["blue", "red", "orange", "gray", "gray"]
    data = dict(xs=xs, ys=ys, linecolor=line_color)

    source.data = data

freq.on_change('value', update)
deltao.on_change('value', update)
time.on_change('value', update)

column = column(freq, deltao, time, plot)
curdoc().add_root(column)

