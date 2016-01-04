from flask import Flask, render_template
from domain_dashboard import dashboard
app = Flask(__name__)

@app.route('/')
def index():
    plot = dashboard()
    return render_template("index.html", div=plot[1], script=plot[0])

if __name__ == '__main__':
    app.debug = True
    app.run()
