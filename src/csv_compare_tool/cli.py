# Author: liquidz00
# GitHub: https://github.com/liquidz00
#
#
# Written: Sep 08 23

import argparse
from src.csv_compare_tool.csv_compare_tool import CSVComparer

help_desc = """

CSV Compare Tool // github.com/liquidz00 // AUG 2023

Compare two different CSV files by specifying a column identifier. 

Usage (after navigating to project directory in Terminal): 
python3 cli.py path/to/first.csv path/to/second.csv column

Where 'column' is the column title containing data to compare

"""

def main():
    parser = argparse.ArgumentParser(description=help_desc, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('csv1', '-c1', type=str, help='Path to the first CSV file')
    parser.add_argument('csv2', '-c2', type=str, help='Path to the second CSV file')
    parser.add_argument('column', '-column', type=str, help='Column identifier for both CSVs')

    args = parser.parse_args()

    comparer = CSVComparer(args.csv1, args.csv2, args.column)

    if not comparer.validate_paths():
        print("CSV file paths are invalid. Please check the file paths and try again.")
        return

    if not comparer.validate_columns():
        print("Invalid column. Please check column identifier and try again.")

    differences = comparer.find_differences()

    if differences:
        print("Differences found:")
        for difference in differences:
            print(f"Record '{difference}' is present in CSV2 but not in CSV1.")
    else:
        print("No differences found.")

if __name__ == "__main__":
    main()
