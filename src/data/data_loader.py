import pandas as pd
from tkinter import filedialog
from src.utils.helper import *


class DataLoader:
    def __init__(self, filepath: str = ""):
        self.file_path = self.get_and_check_filepath(filepath)

    def load_data(self):
        if self.file_path.endswith('.csv'):
            return self.load_csv()
        elif self.file_path.endswith('.xlsx'):
            return self.load_excel()
        else:
            raise ValueError("File type not supported")

    def load_csv(self):
        """ Load data from a CSV file """
        try:
            return pd.read_csv(self.file_path)
        except Exception as e:
            print(f"Error when loading csv file. Filepath: {self.file_path}")
            raise e

    def load_excel(self):
        """ Load data from an Excel file """
        try:
            return pd.read_excel(self.file_path)
        except Exception as e:
            print(f"Error when loading excel file. Filepath: {self.file_path}")
            raise e

    @staticmethod
    def get_and_check_filepath(filepath):
        """
            Returns a file path. If the filepath is not provided, prompts the user to select a file.

            :param filepath: A string representing the initial file path.
            :return: The provided file path, or a path selected by the user.

        """
        if not filepath:
            filepath = filedialog.askopenfilename(filetypes=[('Excel - CSV files', '*.xlsx *.csv')])
            if not filepath:
                raise ValueError("No file was selected.")

            if is_file_exists(file_path=filepath):
                return filepath
            raise FileExistsError(f"File does not exist: {filepath}")
