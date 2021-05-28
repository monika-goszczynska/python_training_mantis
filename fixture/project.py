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
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        # go back to projects list
        self.open_projects_page()

    def fill_new_project_form(self, project):
        # wd = self.app.wd
        self.change_field_value("name", project.name)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_css_selector("input[id='project-name']").clear()
            wd.find_element_by_css_selector("input[id='project-name']").send_keys(text)

    def delete_project(self, index):
        wd = self.app.wd
        self.open_projects_page()
        self.open_edit_page_by_index(index)
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()

    def open_edit_page_by_index(self, index):
        wd = self.app.wd
        table = wd.find_element_by_tag_name("tbody")
        row = table.find_elements_by_tag_name("tr")[index]
        name = row.find_element_by_tag_name("td").text
        row.find_element_by_link_text(name).click()

    def get_project_list(self):
        wd = self.app.wd
        self.open_projects_page()
        project_list = []
        table = wd.find_element_by_tag_name("tbody")
        for element in table.find_elements_by_tag_name("tr"):
            cells = element.find_elements_by_tag_name("td")
            project_name = cells[0].text
            project_list.append(Project(name=project_name))
        return project_list
