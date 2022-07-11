from setuptools import setup, find_packages
from src import wise as wise

with open('requirements.txt') as f:
        required = f.read().splitlines()

setup(
    name='wise-py-utils',
    version=wise.__version__,
    description='Python utils created by Zac the Wise',
    packages=find_packages(
        where='src',
    ),
    package_dir={"":"src"},
    install_requires=required,

)
