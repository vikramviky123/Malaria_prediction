from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(filePath: str) -> List[str]:
    requirements = []
    with open(filePath, 'r') as f:
        lines = f.readlines()
        requirements = [line.replace("\n", "") for line in lines]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


SRC_REPO = "malaria"
__version__ = "0.0.0"

AUTHOR_USER_NAME = "vikramviky123"
AUTHOR_EMAIL = "vikram_viky2001@yahoo.com"

REPO_NAME = "Malaria_prediction"


setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for Chicken disease classification app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements('requirements.txt')
)
