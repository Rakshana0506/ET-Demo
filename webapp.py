from flask import Flask, render_template, request, redirect, url_for, session
import pickle
import numpy as np
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for session

# Load ML model
model = pickle.load(open("final_model.pkl", "rb"))

# Store user credentials
USER_FILE = "users.txt"
# Store activity logs
LOG_FILE = "clicks.txt"

# ------------------------
def log_activity(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

# ------------------------
def save_user(username, password):
    with open(USER_FILE, "a") as f:
        f.write(f"{username},{password}\n")

def user_exists(username):
    if not os.path.exists(USER_FILE):
        return False
    with open(USER_FILE, "r") as f:
        for line in f:
            u, _ = line.strip().split(",")
            if u == username:
                return True
    return False

def validate_user(username, password):
    if not os.path.exists(USER_FILE):
        return False
    with open(USER_FILE, "r") as f:
        for line in f:
            u, p = line.strip().split(",")
            if u == username and p == password:
                return True
    return False

# ------------------------
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if user_exists(username):
            return "Username already exists. Please log in."

        save_user(username, password)
        log_activity(f"{username} - Signed Up")
        return redirect(url_for("login"))

    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if validate_user(username, password):
            session["username"] = username
            log_activity(f"{username} - Logged In")
            return redirect(url_for("index"))
        else:
            return "Invalid credentials"

    return render_template("login.html")

@app.route("/", methods=["GET", "POST"])
def index():
    if "username" not in session:
        return redirect(url_for("login"))

    username = session["username"]
    if request.method == "GET" and request.path == "/":
        log_activity(f"{username} - Visited Wellness Prediction Page")
    if request.method == "POST":
        sleep = float(request.form["sleep_hours"])
        screen = float(request.form["screen_time"])
        input_data = np.array([[sleep, screen]])
        prediction = model.predict(input_data)[0]

        log_activity(f"{username} - Submitted prediction: sleep={sleep}, screen={screen}")
        return render_template("result.html", prediction=prediction)

    return render_template("index.html")

@app.route("/logout")
def logout():
    username = session.get("username", "UnknownUser")
    log_activity(f"{username} - Logged Out")
    session.pop("username", None)
    return redirect(url_for("login"))

# ------------------------
if __name__ == "__main__":
    app.run(debug=True)
