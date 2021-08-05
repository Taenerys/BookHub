import os
from flask import Flask, request, render_template
from dotenv import load_dotenv

# from . import db
from werkzeug.security import check_password_hash, generate_password_hash

# from app.db import get_db

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", url=os.getenv("URL"))


@app.route("/new")
def new():
    return render_template("new.html", url=os.getenv("URL"))
