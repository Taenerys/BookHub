from . import db
from flask_login import UserMixin
from datetime import datetime

tag_book = db.Table(
    "tag_book",
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True),
    db.Column("book_id", db.Integer, db.ForeignKey("book.id"), primary_key=True),
)
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(10000), nullable=False)
    author = db.Column(db.String(10000), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    img = db.Column(db.String, nullable=False)
    notes = db.Column(db.String(10000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    tags = db.relationship(
        "Tag",
        secondary=tag_book,
        backref=db.backref("books_associated", lazy="dynamic"),
    )
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    books = db.relationship("Book")