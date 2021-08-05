import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", title="Book Hub", url="localhost:5000")


@app.route("/create")
def create_thoughts():
    return render_template("create-thought.html")
