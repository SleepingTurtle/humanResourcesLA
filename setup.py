from setuptools import setup,find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    # Package Info
    name = "hr",
    version = "0.1",
    description = "Manages users on a server based an inventory.json file",
    long_description = readme,

    # Package requirements
    packages = find_packages('src'),
    package_dir = {'':'src'},
    install_requires = [],

    # Metadata
    author = "SleepingTurtle",
    auther_email = "joshua@acadaca.com"
)
