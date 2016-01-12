import operator

from bokeh.embed import components
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Panel, Tabs, Button, DataTable, DateFormatter, TableColumn
from bokeh.charts import Bar
from bokeh.io import vform


data = {u'guns': 96, u'potato salad': 97, u'ar15 ak47': 95}


def queries_table(response):
    response_items = sorted(response.items(), key=operator.itemgetter(1),
            reverse=True)
    xqueries = [x[0] for x in response_items]
    yqueries = [y[1] for y in response_items]
    source = ColumnDataSource(data=dict(x=xqueries, y=yqueries))
    columns = [
            TableColumn(field="x", title="Query"),
            TableColumn(field="y", title="Count"),
        ]
    data_table = DataTable(source=source, columns=columns, width=400,
            height=280)
    return data_table


def keywords_dashboard():
    queries = queries_table(data)
    return components(vform(queries))
