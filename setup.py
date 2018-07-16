import re
import sys

import setuptools


REQUIREMENTS = [
    "flake8>=3.5.0,<4",
    "flake8-colors>=0.1.6,<1",
    "flake8-import-order>=0.18<1",
    "flake8-quotes>=1.0.0<2",
]

# Regex matching version pattern
# (3 numerical values separated by `.`, semver style, followed by an optional pre-release marker)
version_pattern = re.compile("\d+\.\d+(\.\d+)?([.-][\w-]+)?")


def get_version():
    changelog_file = "CHANGELOG.md"
    with open(changelog_file, "r") as fn:
        for changelog_line in fn:
            version = version_pattern.search(changelog_line)
            if version is not None:
                return "".join(version.group())
        raise RuntimeError("Couldn't find a valid version in {}".format(changelog_file))


if __name__ == "__main__":
    if sys.argv[1] == "requirements":
        for line in REQUIREMENTS:
            print(line)
        sys.exit(0)

    setuptools.setup(
        name="flake8_edited",
        description="Edited linter for Python, based on flake8",
        version=get_version(),
        author="EDITED devs",
        author_email="dev@edited.com",
        packages=setuptools.find_packages(),
        include_package_data=True,
        url="https://github.com/EDITD/flake8_edited",
        install_requires=REQUIREMENTS,
    )
