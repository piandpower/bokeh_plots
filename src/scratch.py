from urlparse import urlparse
from collections import Counter, OrderedDict

from bokeh.models import ColumnDataSource

from data import time_data
from datetime import datetime, timedelta

import pandas as pd
import numpy as np


datetimes = np.array([np.datetime64(x[1]) for x in time_data])
base = datetimes[0]
deltas = np.array([base - np.datetime64(x[1]) for x in time_data])

# datetimes = np.array([np.datetime64(x[1]) for x in time_data])
# parsed_dates = pd.to_timedelta(datetimes)
# print(parsed_dates)
# parsed_dates.values.sort()

# df = pd.DataFrame(parsed_dates, columns=["datetimes"])
# gb = df.groupby("datetimes")
