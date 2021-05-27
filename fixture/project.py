
from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def create_new_project(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.fill_new_project_form(project)
        wd.find_element_by_css_selector("input[type='submit']").click()
        # go back to projects list
        wd.find_element_by_link_text("Manage Projects").click()

    def fill_new_project_form(self, project):
        # wd = self.app.wd
        self.change_field_value("name", project.name)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_css_selector("input[id='project-name']").clear()
            wd.find_element_by_css_selector("input[id='project-name']").send_keys(text)

