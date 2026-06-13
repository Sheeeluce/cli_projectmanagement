class User:
    def __init__(self, username):
        self.username = username
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)