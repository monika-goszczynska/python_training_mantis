
def test_login(app):
    app.session.login("administrator", "pass")
    assert app.session.is_logged_in_as("administrator")
