from setuptools import setup, find_packages


setup(
    name='wise-py-utils',
    version='0.0.1',
    description='Python utils created by Zac the Wise',
    packages=find_packages(
        where='src',
    ),
    package_dir={"": "src"}
    #package_dir={'get_day': 'src/datetime-utils',},
    # packages=find_packages(where="src")
    #py_modules=('datetimeutils'),
    #packages=['datetime-utils']
)
