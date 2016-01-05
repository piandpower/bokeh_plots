from urlparse import urlparse
from collections import Counter

from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Panel, Tabs
from bokeh.charts import Bar

from data import data as sample


PLOT_ELEMENTS = 10


def domains_bar(response):
    urls = [x[0][0] for x in response["pages"]]
    # xdata = [x[1] for x in response["pages"]]
    # ydata = [x[2] for x in response["pages"]]

    parsed_urls = [urlparse(x).hostname for x in urls]
    domains = Counter(parsed_urls).most_common(PLOT_ELEMENTS)
    endings = Counter([x[x.rfind("."):] for x in parsed_urls]).most_common(PLOT_ELEMENTS)

    xdomains = [x[0] for x in domains]
    ydomains = [y[1] for y in domains]

    xendings = [x[0] for x in endings]
    yendings = [y[1] for y in endings]

    source = ColumnDataSource(data=dict(x=xdomains, y=ydomains))

    p = Bar(source.data, values="y", label="x", title="Domains by Number")
    return components(p)


def top_level_domains_bar(response):
    urls = [x[0][0] for x in response["pages"]]

    parsed_urls = [urlparse(x).hostname for x in urls]
    endings = Counter([x[x.rfind("."):] for x in parsed_urls]).most_common(PLOT_ELEMENTS)

    xendings = [x[0] for x in endings]
    yendings = [y[1] for y in endings]

    source = ColumnDataSource(data=dict(x=xendings, y=yendings))

    p = Bar(source.data, values="y", label="x", title="Top Level Domains by Number")
    return components(p)


def dashboard():
    # domains = domains_bar(sample)
    # top_level = top_level_domains_bar(sample)
    # return components(Tabs(tabs=[domains, top_level]))
    # return top_level_domains_bar(sample)
    return domains_bar(sample)
