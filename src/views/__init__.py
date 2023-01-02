from flask import render_template, request, redirect, url_for, session
from web import app
from model import *
from api_points import get_stats


@app.route('/', methods=["GET"])
def home():
    if "username" in session:
        campaign_data = get_stats()
        username = session["username"]
        return render_template('index.html', data={"campaign":campaign_data, "username":username})
    else:
        return render_template('login.html')


# Register new user
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        registerUser()
    return redirect(url_for("login"))

#Check if email already exists in the registratiion page
@app.route('/checkusername', methods=["POST"])
def check():
    return checkusername()

# Everything Login (Routes to renderpage, check if username exist and also verifypassword through Jquery AJAX request)
@app.route('/login', methods=["GET"])
def login():
    if request.method == "GET":
        if "username" not in session:
            return render_template("login.html")
        else:
            return redirect(url_for("home"))


@app.route('/checkloginusername', methods=["POST"])
def checkUserlogin():
    return checkloginusername()

@app.route('/checkloginpassword', methods=["POST"])
def checkUserpassword():
    return checkloginpassword()

#The admin logout
@app.route('/logout', methods=["GET"])  # URL for logout
def logout():  # logout function
    session.pop('username', None)  # remove user session
    return redirect(url_for("home"))  # redirect to home page with message

#Forgot Password
@app.route('/forgot-password', methods=["GET"])
def forgotpassword():
    return render_template('forgot-password.html')
