from setuptools import find_packages, setup
setup(
    name='Mission1',
    version='0.0.0',
    packages=find_packages(exclude=['tests']),  # Include all the python modules except `tests`.
    description='My custom package tested with tox',
    long_description='A long description of my custom package tested with tox',
    install_requires=[],
)
