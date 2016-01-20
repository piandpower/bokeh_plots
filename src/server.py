from flask import Flask, render_template, url_for

from domains_dashboard import domains_dashboard
from page_times import pages_timeseries

from data import page_data, time_data


app = Flask(__name__)


@app.route('/')
def index():
    script = pages_timeseries(time_data)
    # script, div = domains_dashboard(page_data)
    return render_template("index.html", script=script)


if __name__ == '__main__':
    app.debug = True
    app.run()
