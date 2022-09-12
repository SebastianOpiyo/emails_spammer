from flask import Flask
from gophish import Gophish



app = Flask(__name__)


@app.route("/")
def home():
    return "<p>Hello Gophish Clone</p>"

