from setuptools import setup, find_packages
from src import wise as wise

with open('README.md') as f:
    long_description = f.read()


with open('requirements.txt') as f:
        required = f.read().splitlines()

setup(
    name='wise-py-utils',
    author=wise.__author__,
    version=wise.__version__,
    description='Python utils created by Zac the Wise',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/techWiz-3/python-utils",
    keywords="python-utils python-utilities",
    packages=find_packages(
        where='src',
    ),
    package_dir={"":"src"},
    install_requires=required,

)
