import os
from flask import Flask, request, render_template, send_file
from . import db
from app.db import get_db
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config["DATABASE"] = os.path.join(os.getcwd(), "flask.sqlite")
db.init_app(app)


@app.route("/")
def home():
    return render_template("home.html", title="Book Hub", url="localhost:5000")


@app.route("/create")
def create_thoughts():
    return render_template("create-thought.html")


@app.route("/upload", methods=("GET", "POST"))
def upload():
    if request.method == "POST":
        # get the user input from Create form
        book_title = request.form.get("book_name")
        book_author = request.form.get("book_author")
        date_added = request.form.get("date_added")
        book_image = request.files.get("book_image")
        book_notes = request.form.get("book_notes")

        # manipulate book image data
        # file name of the image
        book_image_name = secure_filename(book_image.filename)
        # type of the image (e.g: jpeg, png)
        book_image_mimetype = book_image.mimetype

        db = get_db()
        error = None

        # error checking
        if not book_title:
            error = "Book title is required"
        elif not book_author:
            error = "Book author is required"
        elif not date_added:
            error = "Date added is required"
        elif not book_image:
            error = "Book image is required"
        elif not book_image_name:
            error = "Bad upload - filename"
        elif not book_image_mimetype:
            error = "Bad upload - mimetype"
        elif not book_notes:
            error = "Book notes is required"

        # if there is no error, add to database and return successful code
        if error is None:
            db.execute(
                "INSERT INTO books (title, author, image, date_added, image_name, image_mimetype, notes) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (
                    book_title,
                    book_author,
                    date_added,
                    book_image.read(),
                    book_image_name,
                    book_image_mimetype,
                    book_notes,
                ),
            )
            db.commit()
            return f"Book {book_title} added successfully"
        else:
            return error, 418
    return "Submit action done!", 200
