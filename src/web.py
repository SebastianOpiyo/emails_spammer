from flask import Flask
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "somesecret_keyyouknow"
app.permanent_session_lifetime = timedelta(minutes=5)

from views import *

if __name__ == "__main__":
    app.run(debug="true")
