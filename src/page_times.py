from urlparse import urlparse
from collections import Counter
import datetime
from operator import itemgetter

import numpy as np
import pandas as pd

from bokeh.plotting import figure, curdoc, vplot
from bokeh.embed import autoload_server
from bokeh.client import push_session
from bokeh.models import Button


def pages_timeseries(response):
    parse_datetime = lambda x: datetime.datetime.strptime(x, "%Y-%m-%dT%H:%M:%S.%f")
    parsed_dates = [parse_datetime(x[1]) for x in response]
    dates = sorted(parsed_dates)
    plot = figure(plot_width=584, x_axis_type="datetime", x_axis_label="Dates",
            y_axis_label="Number Fetched")
    plot.line(x=dates, y=range(len(dates)))

    button = Button(label="Press Me")

    session = push_session(curdoc())
    script = autoload_server(vplot(plot, button), session_id=session.id)
    return script
