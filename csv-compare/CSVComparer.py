# Author: liquidz00
# GitHub: https://github.com/liquidz00
#
#
# Written: Sep 08 23

import pandas as pd
import logging
import os
from typing import Optional, Union

# Logger
logger = logging.getLogger(__name__)

# StrPath
StrPath = Union[str, 'os.PathLike[str]']

class CSVComparer:
    def __init__(self, path_one: Optional[StrPath], path_two: Optional[StrPath], identifier: Optional[str]) -> None:
        self.path_one: Optional[StrPath] = path_one
        self.path_two: Optional[StrPath] = path_two
        self.identifier: Optional[str] = identifier

    def validate_paths(self):
        if not os.path.exists(self.path_one):
            logging.error(f"CSV file not found: {self.path_one}")
            return False
        if not os.path.exists(self.path_two):
            logging.error(f"CSV file not found: {self.path_two}")
            return False
        return True

    def find_differences(self):
        if not self.validate_paths():
            return []

        db_1 = pd.read_csv(self.path_one)
        db_2 = pd.read_csv(self.path_two)

        users_1 = db_1[self.identifier].to_list()
        users_2 = db_2[self.identifier].to_list()

        differences = []

        for user in users_2:
            if user not in users_1:
                differences.append(user)

        return differences
