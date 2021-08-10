from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    # books = get_books()
    # TODO: Pass actual image to get it displayed - perhaps needs to do research
    # for book in books:
    #     book['img'] = send_file(book['img'], book['img_mimetype'])
    #     print(book['img'])
    return render_template(
        # "home.html", title="Book Hub", url="localhost:5000", books=books
        "home.html", title="Book Hub", url="localhost:5000"
    )

@views.route('/create')
def create_thoughts():
    return render_template("create-thought.html")