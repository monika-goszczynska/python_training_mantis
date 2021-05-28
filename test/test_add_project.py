from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "pass")
    old_list = app.project.get_project_list()
    project = Project(name="y")
    old_list.append(project)
    app.project.create_new_project(project)
    new_list = app.project.get_project_list()
    assert sorted(old_list) == sorted(new_list)

