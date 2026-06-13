import argparse

parser = argparse.ArgumentParser(
    description = "Project Management CLI"
)

subparsers = parser.add_subparsers(dest = "command")

add_user = subparsers.add_parser("add-user")
add_user.add_argument("username")

