from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint("views", __name__)


@views.route("/")
@login_required
def home():
    # books = get_books()
    # TODO: Pass actual image to get it displayed - perhaps needs to do research
    # for book in books:
    #     book['img'] = send_file(book['img'], book['img_mimetype'])
    #     print(book['img'])
    return render_template(
        # "home.html", title="Book Hub", url="localhost:5000", books=books
        "home.html",
        title="Book Hub",
        url="localhost:5000",
        user=current_user,
    )


@views.route("/create")
def create_thoughts():
    return render_template("create-thought.html", user=current_user)


@views.route("/success")
def success():
    return render_template("success.html", user=current_user)


@views.route("/upload")
def upload():
    return render_template("upload.html", user=current_user)
