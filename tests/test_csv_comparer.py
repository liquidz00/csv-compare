import pytest
import os

from csv_compare.CSVComparer import CSVComparer

BASE_DIR = os.path.dirname(__file__)

@pytest.fixture
def fruit_csvs():
    fruits1 = os.path.join(BASE_DIR, "fruits1.csv")
    fruits2 = os.path.join(BASE_DIR, "fruits2.csv")

    yield fruits1, fruits2

@pytest.fixture
def title_csvs():
    titles1 = os.path.join(BASE_DIR, "anyorg_old_titles.csv")
    titles2 = os.path.join(BASE_DIR, "anyorg_new_titles.csv")

    yield titles1, titles2

def test_fruits(fruit_csvs):
    csv1, csv2 = fruit_csvs
    col = "Fruit"

    comparer = CSVComparer(csv1, csv2, col).find_differences()

    expected_result = ["Banana"]

    assert comparer == expected_result

def test_titles(title_csvs):
    csv1, csv2 = title_csvs
    col = "Job Title"

    comparer = CSVComparer(csv1, csv2, col).find_differences()

    expected_result = ['Product Designer', 'Data Analyst', 'Software Developer', 'HR Administrator', 'Market Researcher', 'Quality Assurance Specialist', 'Support Specialist', 'Recruitment Manager', 'Public Relations Specialist', 'IT Support Specialist', 'Market Analyst', 'Customer Relations Specialist']

    assert comparer == expected_result

def test_invalid_column(title_csvs):
    with pytest.raises(ValueError):
        csv1, csv2 = title_csvs
        CSVComparer(csv1, csv2, identifier="invalid column").find_differences()




