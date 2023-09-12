from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

def read_files(files):
    data = []
    for file in files:
        with open(file, encoding='utf-8') as f1:
            data.append(f1.read())
    return "\n".join(data)

long_description = read_files(["README.md"])

meta = {}
with open('src/csv_compare_tool/version.py', encoding='utf-8') as f:
    exec(f.read(), meta)

setup(
    name='csv_compare_tool_liquidz00',
    description='Package to find differences between two CSV files',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version=meta['__version__'],
    author='Andrew Speciale',
    url="https://github.com/liquidz00/csv-compare",
    packages=find_packages(exclude=['tests']),
    package_dir={'': 'src'},
    python_requires=">=3.8",
    install_requires=requirements,
    license='Apache-2.0',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Mac Administrators',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache-2.0 License',
        'Operating System :: OS Independent'
    ]
)
