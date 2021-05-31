from model.project import Project
import random


def test_add_project(app):
    app.session.login("administrator", "pass")
    old_list = app.project.get_project_list()
    project = Project(name="project" + str(random.randint(0, 1000)))
    old_list.append(project)
    app.project.create_new_project(project)
    new_list = app.project.get_project_list()
    assert sorted(old_list, key=lambda p: p.name) == sorted(new_list, key=lambda p: p.name)

