from setuptools import setup, find_packages

setup(
    name="Chicken-Disease-Classification",
    version="0.0.0",
    author="sambitpani",
    author_email="sambitpani2@gmail.com",
    description="A small python package for CNN app",
    url=f"https://github.com/sambitpani-ds/Chicken-Disease-Classification",
    project_urls={
        "Bug Tracker": f"https://github.com/sambitpani-ds/Chicken-Disease-Classification/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src")
)