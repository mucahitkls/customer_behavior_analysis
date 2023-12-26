import pandas as pd
import re

class DataCleaner:
    def __init__(self, dataframe):
        self.df = dataframe

    def clean_ids(self):
        """Ensure CustomerIDs are in a standard format (e.g., 001, 002,...)."""
        self.df['CustomerID'] = self.df['CustomerID'].apply(lambda x: str(x).zfill(3))

    def clean_names(self):
        """Strip trailing spaces and correct obvious typos in names."""
        self.df['Name'] = self.df['Name'].str.strip().replace(r'\bx\b', '')

    def clean_ages(self):
        """Convert ages from text to integers, handle missing and nonsensical values."""
        def age_converter(age):
            if re.match(r'^\d+$', age):
                return int(age)
            if 'twenty' in age:
                return 25
            if 'thirty' in age:
                return 35
            if 'forty' in age:
                return 45
            return None  # or some default/mean/median age

        self.df['Age'] = self.df['Age'].apply(age_converter)

    def clean_emails(self):
        """Remove rows with invalid or missing email addresses."""
        valid_email = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        self.df = self.df[self.df['Email'].str.match(valid_email)]

    def standardize_dates(self):
        """Convert dates to a standard YYYY-MM-DD format, handle wrong formats."""
        self.df['SignUpDate'] = pd.to_datetime(self.df['SignUpDate'], errors='coerce')
        self.df['LastPurchaseDate'] = pd.to_datetime(self.df['LastPurchaseDate'], errors='coerce')

    def clean_purchases(self):
        """Ensure total purchases and average purchase values are numeric and reasonable."""
        self.df['TotalPurchases'] = pd.to_numeric(self.df['TotalPurchases'], errors='coerce')
        self.df['AveragePurchaseValue'] = pd.to_numeric(self.df['AveragePurchaseValue'], errors='coerce')

    def standardize_devices(self):
        """Correct minor typos in device names and standardize to 'Mobile' or 'Desktop'."""
        self.df['PreferredDevice'] = self.df['PreferredDevice'].str.replace('Mobil', 'Mobile', regex=False)

    def clean_locations(self):
        """Handle missing or incomplete location data."""
        self.df['Location'] = self.df['Location'].replace('', 'Unknown')

    def run_all(self):
        """Run all cleaning functions."""
        self.clean_ids()
        self.clean_names()
        self.clean_ages()
        self.clean_emails()
        self.standardize_dates()
        self.clean_purchases()
        self.standardize_devices()
        self.clean_locations()

        return self.df

# Usage example:
# cleaner = DataCleaner(customer_df)
# clean_customer_df = cleaner.run_all()
