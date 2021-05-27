from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "pass")
    app.project.create_new_project(Project(name="new project name"))
