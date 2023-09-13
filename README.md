# :mag_right: CSV-Compare
[![PyPI version](https://badge.fury.io/py/csv-compare-tool.svg)](https://badge.fury.io/py/csv-compare-tool)
#### A python package for Jamf MacAdmins in mind

The csvcomparetool allows you to find differences between two CSV files based on a specified column identifier. It provides a simple way to compare the contents of two CSV files and identify which records are present in one file but not in the other. 

> **Best Practice** <br>
> When comparing CSV files for differences, be sure to provide the CSV with more entries second. For example, if CSV-1 has a list of 34 names, and CSV-2 has a list of 40, CSV-2 should be set as the second passed CSV path in order for differences to show as expected.

- [Installation](#installation)
- [Usage](#usage)
  - [Import class](#import-the-csvcomparer-class-from-the-package)
  - [Create object](#create-a-csvcomparer-object)
  - [Validate paths](#validate-the-paths-to-ensure-the-specified-csv-files-exist)
  - [Validate column](#validate-the-column-exists-in-the-provided-csv-files)
  - [Find differences](#find-the-differences-between-the-two-csv-files)
  - [Handle differences as needed](#print-or-process-the-differences-as-needed)
- [Examples](#examples)
  - [Python project](#python-project)
  - [CLI](#command-line-tool)

## Installation

You can install CSV-Compare using `pip`:
```bash
pip install csv-compare-tool
```

## Usage
To use CSV-Compare in your Python project, follow these steps.
> **Important** <br>
> When importing as a package in a Python project, be sure to **remove** the hyphens so the package reads `csvcomparetool` (See [PEP 8](https://peps.python.org/pep-0008/#package-and-module-names) for more information)

### Import the package
```python
import csvcomparetool
```
Optionally, you can import the `CSVComparer` class alone
```python
from csvcomparetool import CSVComparer
```

### Create a `CSVComparer` object
> **Note** <br>
> The `CSVComparer` object requires two paths and a column identifier. The column identifier is the title of the column you are pulling from. <br> For example, 'Full Name' would be the column identifier for full names.
```python
csv1_path = "path/to/first.csv"
csv2_path = "path/to/second.csv"
column = "identifier_column"
comparer = CSVComparer(csv1_path, csv2_path, column)
```

### Validate the paths to ensure the specified CSV files exist
```python
if not comparer.validate_paths():
    print("CSV file paths are invalid. Please check the file paths and try again.")
    return
```

### Validate the column exists in the provided CSV files
```python
if not comparer.validate_columns():
    print("Provided column not found in CSV. Check the columns and try again.")
    return
```

### Find the differences between the two CSV files
```python
differences = comparer.find_differences()
```

### Print or process the differences as needed
```python
for difference in differences:
    print(f"Record '{difference}' is present in CSV2 but not in CSV1.")
```

## Examples
### Python Project

```python
from csvcomparetool import CSVComparer

csv1_path = "path/to/first.csv"
csv2_path = "path/to/second.csv"
column = "identifier_column"

comparer = CSVComparer(csv1_path, csv2_path, column)

if not comparer.validate_paths() or not comparer.validate_columns():
    print("CSV file paths are invalid, or the column identifier does not exist. Check the file paths and columns and try again.")
else:
    differences = comparer.find_differences()
    for difference in differences:
        print(f"Record '{difference}' is present in CSV2 but not in CSV1.")
```

### Command Line tool
First, clone this repository to a local directory on your machine
```bash
git clone https://github.com/liquidz00/csv-compare.git
```
Navigate to the cloned repo location (local directory where you chose to save the repository)
```bash
cd /path/to/repo/src/csvcomparetool/
```
Lastly, run the following command
```bash 
python cli.py /csv/path/one /csv/path/two columnidentifier
```
