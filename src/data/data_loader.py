import pandas as pd
from src.utils.helper import *


class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        if self.file_path.endswith('.csv'):
            return self.load_csv()
        elif self.file_path.endswith('.xlsx'):
            return self.load_excel()
        else:
            raise ValueError("File type not supported")

    def load_csv(self):
        """ Load data from a CSV file """
        if is_file_exists(self.file_path):
            return pd.read_csv(self.file_path)
        raise FileExistsError("File does not exists")

    def load_excel(self):
        """ Load data from an Excel file """
        if is_file_exists(self.file_path):
            return pd.read_excel(self.file_path)
        raise FileExistsError("File does not exists")
