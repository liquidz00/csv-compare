from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='csv-comparer',
    version='1.0',
    description='Package to find differences between two CSV files',
    packages=find_packages(),
    requires=requirements
)
