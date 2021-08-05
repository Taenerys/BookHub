import os
from flask import Flask, render_template
from flask import Flask, request, render_template
from . import db
from app.db import get_db

app = Flask(__name__)
app.config["DATABASE"] = os.path.join(os.getcwd(), "flask.sqlite")
db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html", title="Book Hub", url="localhost:5000")


@app.route("/create")
@app.route("/create", methods=("GET", "POST"))
def create_thoughts():
    if request.method == "POST":
        book_title = request.form.get("book_name")
        book_author = request.form.get("book_author")
        date_added = request.form.get("date_added")
        book_image = request.form.get("book_image")
        book_notes = request.form.get("book_notes")

        db = get_db()
        error = None

        if not book_title:
            error = "Book title is required"
        elif not book_author:
            error = "Book author is required"
        elif not date_added:
            error = "Date added is required"
        elif not book_image:
            error = "Book image is required"
        elif not book_notes:
            error = "Book notes is required"

        if error is None:
            db.execute(
                "INSERT INTO books (title, author, date_added, image, notes) VALUES (?, ?, ?, ?, ?)",
                (book_title, book_author, date_added, book_image, book_notes),
            )
            db.commit()
            return f"Book {book_title} added successfully"
        else:
            return error, 418

    return render_template("create-thought.html")
