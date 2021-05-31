from model.project import Project

def test_del_project(app):
    app.session.login("administrator", "pass")
    if len(app.project.get_project_list()) == 0:
        app.project.create_new_project(Project(name="addedBecauseZero"))
    index = 0
    old_list = app.project.get_project_list()
    project = app.project.get_project_list()[index]
    app.project.delete_project(index)
    old_list.remove(project)
    new_list = app.project.get_project_list()
    assert sorted(old_list, key=lambda p: p.name) == sorted(new_list, key=lambda p: p.name)
