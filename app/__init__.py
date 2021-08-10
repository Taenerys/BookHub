from os import path
from flask import Flask, request, render_template, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    # TODO: will store this key safely later & change it!
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secret_key_for_now_secret_key"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth/")

    from .models import User, Book, Tag

    create_database(app)

    return app


def create_database(app):
    if not path.exists("app" + DB_NAME):
        db.create_all(app=app)
        print("Database Created!")
