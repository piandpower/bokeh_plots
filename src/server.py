from flask import Flask, render_template, url_for

from domains_dashboard import domains_dashboard
from keywords_dashboard import keywords_dashboard

from data import page_data


app = Flask(__name__)


@app.route('/')
def index():
    script, div = domains_dashboard(page_data)
    return render_template("index.html", div=div, script=script)


if __name__ == '__main__':
    app.debug = True
    app.run()
