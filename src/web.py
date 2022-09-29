from flask import Flask, render_template
from jinja2 import TemplateNotFound


app = Flask(__name__)


@app.route("/")
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run()