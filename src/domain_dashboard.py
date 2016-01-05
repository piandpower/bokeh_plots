from urlparse import urlparse
from collections import Counter

from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.models import ColumnDataSource
from bokeh.charts import Bar

from data import data


def dashboard(response=None):
    urls = [x[0][0] for x in data["pages"]]
    xdata = [x[1] for x in data["pages"]]
    ydata = [x[2] for x in data["pages"]]

    parsed_urls = [urlparse(x).hostname for x in urls]
    domains = Counter(parsed_urls).most_common()
    endings = Counter([x[x.rfind("."):] for x in parsed_urls]).most_common()

    xdomains = [x[0] for x in domains]
    ydomains = [y[1] for y in domains]

    xendings = [x[0] for x in endings]
    yendings = [y[1] for y in endings]

    source = ColumnDataSource(data=dict(x=xdomains, y=ydomains))

    p = Bar(source.data, values="y", label="x", title="Domains by Number")
    return components(p)
