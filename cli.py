import argparse

parser = argparse.ArgumentParser(
    description = "Project Management CLI"
)

subparsers = parser.add_subparsers(dest = "command")
#add-user
add_user = subparsers.add_parser("add-user")
add_user.add_argument("username")

#list-users
list_users = subparsers.add_parser("list-users")

#add-project
add_project = subparsers.add_parser("add-project")

add_project.add_argument("username")
add_project.add_argument("project_name")
