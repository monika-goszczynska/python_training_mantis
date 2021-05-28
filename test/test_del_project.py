from model.project import Project

def test_del_project(app):
    app.session.login("administrator", "pass")
    if len(app.project.get_project_list()) == 0:
        app.project.create_new_project(Project(name="addedBecauseZero"))
    app.project.delete_project(0)