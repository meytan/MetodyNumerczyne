import matplotlib.pyplot as plot
from numpy import arange


def draw_plot(method):

    points = [(x, method(x)) for x in arange(-2, 8, 0.01)]
    plot.grid(True)
    plot.axhline(y=0, color='k')
    plot.axvline(x=0, color='k')
    plot.plot([x[0] for x in points], [y[1] for y in points])
    plot.show()
