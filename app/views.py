import os
from os import path
import app
from app import db
from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .models import Book, Tag
from werkzeug.utils import secure_filename

views = Blueprint("views", __name__)

@views.route("/")
@login_required
def home():
    books = get_books()
    path = 'app/static/images/'
    for book in books:
        with open(path + book.img_name, "wb") as binary_file:
            # save files to images folder 
            # TODO: is there a way to make images saved to server?
            binary_file.write(book.img)
    return render_template(
        "home.html",
        title="Book Hub",
        url="localhost:5000",
        books=books,
        user=current_user
    )

@views.route("/create")
def create_thoughts():
    return render_template("create-thought.html", user=current_user)

@views.route("/upload", methods=['GET', 'POST'])
def upload_book():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        img = request.files['img']
        notes = request.form.get('notes')
        tag_string = request.form.get('tags')

        tags = process_form_data(tag_string)

        img_name = secure_filename(img.filename)

        if not img:
            return 'No picture is uploaded', 400

        new_book = Book(title=title, author=author, img=img.read(), img_name=img_name, img_mimetype=img.mimetype, notes=notes, user_id=current_user.id, tags=tags)

        # add to database here
        db.session.add(new_book)
        db.session.commit()

    return render_template('success.html',user=current_user)

def get_tags_from_string(tag_string):
    raw_tags = tag_string.split(',')

    # filter out any empty tag names
    tag_names = [name.strip() for name in raw_tags if name.strip()]
    
    # query the database and retrieve any tags we have already saved
    existing_tags = Tag.query.filter(Tag.name.in_(tag_names))

    # determine which tag names are new
    new_names = set(tag_names) - set([tag.name for tag in existing_tags])

    # create a list of unsaved Tag instances for the new tags
    new_tags = [Tag(name=name) for name in new_names]

    # return all existing tags + all the new, unsaved tags
    return list(existing_tags) + new_tags

def process_form_data(value_form):
    if value_form:
        return get_tags_from_string(value_form)
    else:
        return []

def get_books():
    return Book.query.order_by(Book.date_added).all()

# TODO: Fucntion to get an individual book to display the detail for each

# TODO: Function to delete book

# TODO: Function to edit book