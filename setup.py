from setuptools import setup,find_packages

setup(
    # Package Info
    name = "hr",
    version = "0.1",
    description = "Manages users on a server based an inventory.json file",

    # Package requirements
    packages = find_packages('src'),
    package_dir = {'':'src'},
    install_requires = [],

    # Metadata
    author = "SleepingTurtle",
    auther_email = "joshua@acadaca.com"
)
