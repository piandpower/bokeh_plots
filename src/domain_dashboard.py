from urlparse import urlparse

from bokeh.sampledata.iris import flowers
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components

from data import data


def dashboard():
    urls = [x[0][0] for x in data["pages"]]
    xdata = [x[1] for x in data["pages"]]
    ydata = [x[2] for x in data["pages"]]

    domains = [urlparse(x).hostname for x in urls]
    endings = [x[x.rfind("."):] for x in domains]

dashboard()
