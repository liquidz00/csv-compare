# Changelog

All notable changes to this project will be documented in this file. 

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Features currently in progress:

- Adding additional column identifier in event columns are not the same across the two CSV files

## [1.0.3] - 2023-09-15

### Fixed

- Issue with project files not properly being indexed in distribution being uploaded to PyPi
- Issue where `CSVComparer` class could not be imported after installing via `pip`

### Deprecated

- Yanked version 1.0.2 from PyPi due to package import issues mentioned above

## [1.0.2] - 2023-09-13

### Changed

- Configuration of pyproject.toml file
- Refactored package name from csv-compare-tool to csvcomparetool for easier import statements
- Bumped to v1.0.2

### Deprecated

- `setup.py` file per [setuptools documentation](https://setuptools.pypa.io/en/latest/userguide/quickstart.html#transitioning-from-setup-py-to-setup-cfg)

## [1.0.1] - 2023-09-12

### Fixed

- Issue with build when installing package via `pip`

### Changed

- Bumped to version 1.0.1
- Metadata in pyproject.toml and setup.py files


