import pandas as pd
import re


class DataCleaner:

    expected_columns = [
        "CustomerID", "Name", "Age", "Email", "SignUpDate",
        "LastPurchaseDate", "TotalPurchases", "AveragePurchaseValue",
        "PreferredDevice", "Location"
    ]

    def __init__(self, dataframe):
        self.df = self.validate_dataframe(dataframe)

    @staticmethod
    def validate_dataframe(dataframe):
        if dataframe.empty:
            raise pd.errors.EmptyDataError("The provided DataFrame is empty.")
        return dataframe

    def validate_columns(self):
        """Check if the DataFrame follows the expected format."""
        missing_columns = set(self.expected_columns) - set(self.df.columns)
        if missing_columns:
            raise ValueError(f"Missing columns: {', '.join(missing_columns)}")

    def clean_ids(self):
        """Ensure CustomerIDs are in a standard format (e.g., 001, 002,...)"""
        self.df['CustomerID'] = self.df['CustomerID'].astype(str).str.zfill(3)

    def clean_names(self):
        """Strip trailing spaces and correct obvious typos in names."""
        self.df['Name'] = self.df['Name'].str.strip().str.replace(r'\bx\b', '', regex=True)

    # ... [Keep other cleaning methods as is, but consider the below enhancements]

    def standardize_devices(self):
        """Correct minor typos in device names and standardize to 'Mobile' or 'Desktop'."""
        device_corrections = {'Mobil': 'Mobile', 'Deskop': 'Desktop'}
        self.df['PreferredDevice'] = self.df['PreferredDevice'].replace(device_corrections)

    # ... [Include other methods]

    def run_all(self):
        """Run all cleaning functions."""
        self.validate_columns()  # Ensure columns are validated before cleaning
        self.clean_ids()
        self.clean_names()
        # ... [Include all other cleaning methods]
        return self.df
