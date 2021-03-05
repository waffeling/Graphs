from bokeh.plotting import Figure, show, output_file
from bokeh.models import Div, CustomJS, Slider, ColumnDataSource
from bokeh.io import show
from bokeh.layouts import layout, column
from math import pi, sin

output_file("GraphCore.html")

Ticks = list(range(0, 720))
x = []
y = []
for i in Ticks:
    x.append(i * pi / 180)
    holdon = i * pi / 180
    y.append(sin(holdon))




data = ColumnDataSource(data=dict(x=x, y=y))

plot = Figure(title="Sine Graph")
plot.line('x', 'y', source=data, legend_label="y=sin(x)", line_width=2, )

callback = CustomJS(args=dict(source=data), code="""
    var data = source.data;
    var f = cb_obj.value
    var x = data['x']
    var y = data['y']
    for (var i = 0; i < x.length; i++) {
        x[i] = 2*3.14*f*x[i]
    }
    source.change.emit();
""")

slider = Slider(start=0.1, end=2, value=1, step=0.1, title="Frequency")
slider.js_on_change('value', callback)

# div = Div(text="""
#         <p>Use the slider to adjust the frequency:</p>
#         """,
#           width=200,
#           height=30)

layout = column(slider, plot)

show(layout)
