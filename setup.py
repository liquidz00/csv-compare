from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='csv-comparer',
    author='liquidz00 // github.com/liquidz00',
    version='1.0',
    description='Package to find differences between two CSV files',
    packages=find_packages(),
    install_requires=requirements
)
