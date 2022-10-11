import json
from flask import Flask, render_template, jsonify
from jinja2 import TemplateNotFound
from gophish.models import *

app = Flask(__name__)


@app.route("/")
def dashboard():
    from api_points import API
    campaigns = API.campaigns.get()
    for summary in campaigns:
        print(summary)
    return render_template('dashboard.html', campaigns=campaigns)


if __name__ == '__main__':
    app.run()