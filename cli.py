import argparse

parser = argparse.ArgumentParser(
    description = "Project Management CLI"
)

subparsers = parser.add_subparsers(dest = "command")