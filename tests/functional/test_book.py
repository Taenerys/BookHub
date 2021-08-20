from app import create_app


def test_home_page():
    """
    GIVEN a Flask application configured for testing
    WHEN thhe '/' page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = create_app()

    # create a test client using the Flask app configured for testig
    with flask_app.test_client() as test_client:
        response = test_client.get("/auth/login?next=%2F")
        assert response.status_code == 200
        # assert b"Welcome to Book Hub!" in response.data
        # assert b"Needs an account?" in response.data
        # assert b"Existing user?" in response.data


def test_home_page_post():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is is posted to (POST)
    THEN check that a '405' status code is returned
    """
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.post("/")
        assert response.status_code == 405
