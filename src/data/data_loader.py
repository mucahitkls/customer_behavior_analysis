import pandas as pd
from tkinter import filedialog
from src.utils.helper import *


class DataLoader:
    def __init__(self, filepath: str = ""):
        self.file_path = self.get_file_path(filepath)

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

    @staticmethod
    def get_file_path(filepath):
        """
            Returns a file path. If the filepath is not provided, prompts the user to select a file.

            :param filepath: A string representing the initial file path.
            :return: The provided file path, or a path selected by the user.

        """
        if not filepath:
            filepath = filedialog.askopenfilename(filetypes=[('Excel file', '*.xlsx'), ('CSV file', '*.csv')])
            if not filepath:
                raise ValueError("No file was selected.")
            return filepath


loader = DataLoader()
variable = loader.load_data()
