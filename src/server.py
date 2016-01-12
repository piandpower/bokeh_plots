from flask import Flask, render_template
from domain_dashboard import domain_dashboard
from keywords_dashboard import keywords_dashboard
app = Flask(__name__)


@app.route('/')
def index():
    script, div = keywords_dashboard()
    return render_template("index.html", div=div, script=script)


if __name__ == '__main__':
    app.debug = True
    app.run()
