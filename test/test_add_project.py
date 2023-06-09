from model.project import Project


def test_add_project(app, json_projects):
    project = json_projects
    old_projects = app.project.get_project_list()
    app.project.create_project(project)
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert len(old_projects) == len(new_projects)
    assert sorted(old_projects, key=Project.key_name) == sorted(new_projects, key=Project.key_name)


def test_add_new_project_2(app, json_projects):
    project = json_projects
    old_projects = app.soap.get_project_list()
    app.project.create_project(project)
    new_projects = app.soap.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.key_name) == sorted(new_projects, key=Project.key_name)
