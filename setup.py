from setuptools import find_packages, setup


def find_required():
    with open("requirements.txt") as f:
        return f.read().splitlines()

setup(
    name="fresh-deps",
    version="1.0.0",
    description="Keep your Python dependencies fresh",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Nikita Tsvetkov",
    author_email="pychapter@2gis.ru",
    python_requires=">=3.8",
    url="https://gitlab.2gis.ru/pychapter/fresh-deps",
    packages=find_packages(exclude=("tests",)),
    package_data={"fresh_deps": ["py.typed"]},
    entry_points={
        "console_scripts": [
            "fresh-deps = fresh_deps:update_dependencies",
            "fresh_deps = fresh_deps:update_dependencies",
        ],
    },
    install_requires=find_required(),
)