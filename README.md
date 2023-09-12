# :mag_right: CSV-Compare
#### A python package for Jamf MacAdmins in mind

The csv-compare-tool allows you to find differences between two CSV files based on a specified column identifier. It provides a simple way to compare the contents of two CSV files and identify which records are present in one file but not in the other. 

> :white_check_mark: **Best Practice** <br>
> When comparing CSV files for differences, be sure to provide the CSV with more entries second. For example, if CSV-1 has a list of 34 names, and CSV-2 has a list of 40, CSV-2 should be set as the second passed CSV path in order for differences to show as expected.

## :wrench: Installation

You can install CSV-Compare using `pip`:
```bash
pip install csv-compare-tool
```

## :bulb: Usage
To use CSV-Compare in your Python project, follow these steps.

### Import the `CSVComparer` class from the package
```python
from csv-compare-tool import CSVComparer
```

### Create a `CSVComparer` object
> :memo: **Note** <br>
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

## :clipboard: Examples
### Python Project

```python
from csv-compare import CSVComparer

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
cd /path/to/repo/src/csv_compare_tool/
```
Lastly, run the following command
```bash
python cli.py /csv/path/one /csv/path/two columnidentifier
```
