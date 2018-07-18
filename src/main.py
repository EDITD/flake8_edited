import os
import sys

from flake8.main import application


def main(argv=None):
    package_dir = os.path.normpath(os.path.dirname(__file__))
    config_file = os.path.join(package_dir, "config", "edited.ini")
    config_args = ["--prepend-config", config_file]

    cli_args = (argv or sys.argv)[1:]

    args = ["flake8"] + config_args + cli_args

    app = application.Application()
    app.run(args)
    app.exit()
