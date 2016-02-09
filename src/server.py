from flask import Flask, render_template, url_for

from domains_dashboard import domains_dashboard
from page_times import pages_timeseries, line_scratch

from data import page_data, time_data


app = Flask(__name__)


@app.route('/')
def index():
    script = line_scratch()
    # script, div = line_scratch()
    # script, div = domains_dashboard(page_data)
    return render_template("index.html", script=script)
    # return render_template("alt.html", script=script, div=div)


if __name__ == '__main__':
    app.debug = True
    app.run()
