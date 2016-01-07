from math import pi
from urlparse import urlparse
from collections import Counter

from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Panel, Tabs, Button
from bokeh.charts import Bar
from bokeh.io import vform

from data import data as sample


PLOT_ELEMENTS = 10
BAR_WIDTH = 0.4


def sample_tabs():
    from bokeh.models.widgets import Panel, Tabs
    from bokeh.io import output_file, show
    from bokeh.plotting import figure

    output_file("slider.html")

    p1 = figure(plot_width=300, plot_height=300)
    p1.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)
    tab1 = Panel(child=p1, title="circle")

    p2 = figure(plot_width=300, plot_height=300)
    p2.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=3, color="navy", alpha=0.5)
    tab2 = Panel(child=p2, title="line")

    tabs = Tabs(tabs=[ tab1, tab2 ])

    return tabs


def domains_bar(response):
    urls = [x[0][0] for x in response["pages"]]

    parsed_urls = [urlparse(x).hostname for x in urls]
    domains = Counter(parsed_urls).most_common(PLOT_ELEMENTS)

    xdomains = [x[0] for x in domains]
    ydomains = [y[1] for y in domains]

    source = ColumnDataSource(data=dict(x=xdomains, y=ydomains))

    p = Bar(source.data, values="y", label="x", title="Domains by Number",
            bar_width=BAR_WIDTH)
    bar_panel = Panel(child=p, title="Domains")

    return bar_panel


def top_level_domains_bar(response):
    urls = [x[0][0] for x in response["pages"]]

    parsed_urls = [urlparse(x).hostname for x in urls]
    endings = Counter([x[x.rfind("."):] for x in parsed_urls]).most_common(PLOT_ELEMENTS)

    xendings = [x[0] for x in endings]
    yendings = [y[1] for y in endings]

    source = ColumnDataSource(data=dict(x=xendings, y=yendings))

    p = Bar(source.data, values="y", label="x",
            title="Top Level Domains by Number", bar_width=BAR_WIDTH)
    bar_panel = Panel(child=p, title="Top Level")
    return bar_panel


def dashboard():
    button = Button(label="Foo", type="success")
    domains = domains_bar(sample)
    top_level = top_level_domains_bar(sample)
    return components(vform(Tabs(tabs=[domains, top_level]), button))
    #return components(sample())
