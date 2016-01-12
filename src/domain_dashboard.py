from urlparse import urlparse
from collections import Counter

from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Panel, Tabs, Button, DataTable, DateFormatter, TableColumn
from bokeh.charts import Bar
from bokeh.io import vform

from data import page_data as sample


PLOT_ELEMENTS = 10
BAR_WIDTH = 0.4


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


def domains_table(response):
    urls = [x[0][0] for x in response["pages"]]

    parsed_urls = [urlparse(x).hostname for x in urls]
    domains = Counter(parsed_urls).most_common()

    xdomains = [x[0] for x in domains]
    ydomains = [y[1] for y in domains]
    source = ColumnDataSource(data=dict(x=xdomains, y=ydomains))

    columns = [
            TableColumn(field="x", title="Domain"),
            TableColumn(field="y", title="Count"),
        ]
    data_table = DataTable(source=source, columns=columns, width=400,
            height=280)
    return data_table


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


def top_level_domains_table(response):
    urls = [x[0][0] for x in response["pages"]]

    parsed_urls = [urlparse(x).hostname for x in urls]
    endings = Counter([x[x.rfind("."):] for x in parsed_urls]).most_common(PLOT_ELEMENTS)

    xendings = [x[0] for x in endings]
    yendings = [y[1] for y in endings]
    source = ColumnDataSource(data=dict(x=xendings, y=yendings))
    columns = [
            TableColumn(field="x", title="Top Level Domain"),
            TableColumn(field="y", title="Count"),
        ]
    data_table = DataTable(source=source, columns=columns, width=400,
            height=280)
    return data_table


def domain_dashboard():
    domains = domains_bar(sample)
    top_level = top_level_domains_bar(sample)
    table_domains = domains_table(sample)
    top_level_table_domains = top_level_domains_table(sample)
    return components(vform(Tabs(tabs=[domains, top_level]), table_domains,
        top_level_table_domains))
