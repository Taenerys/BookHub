from app.models import User, Book, Tag
from werkzeug.security import generate_password_hash

def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, passwords if they are defined correctly
    """
    user = User(email='test_email@gmail.com', password=generate_password_hash('holyshitomg', method='sha256'))
    assert user.email == 'test_email@gmail.com'
    assert user.password != 'holyshitomg'

def test_new_book():
    """
    GIVEN a Book model
    WHEN a new Book is created
    THEN check the fields if they are defined correctly
    """
    book = Book(title='A book', author='An author', img='IMG_here', notes='Thoughts here')
    assert book.title == 'A book'
    assert book.author == 'An author'
    assert book.img == 'IMG_here'
    assert book.notes == 'Thoughts here'

def test_new_tag():
    """
    GIVEN a Tag model
    WHEN a new Tag is created
    THEN check the fields if they are defined correctly
    """
    tag = Tag(name="fiction")
    assert tag.name == 'fiction'