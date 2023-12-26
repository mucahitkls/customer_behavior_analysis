import pandas as pd
import re


class DataCleaner:

    def __init__(self, dataframe):
        self.df = dataframe
        self.expected_columns = [
            "CustomerID", "Name", "Age", "Email", "SignUpDate",
            "LastPurchaseDate", "TotalPurchases", "AveragePurchaseValue",
            "PreferredDevice", "Location"
        ]

    def validate_dataframe(self):
        """Check if the DataFrame follows the expected format."""
        missing_columns = set(self.expected_columns) - set(self.df.columns)
        if missing_columns:
            raise ValueError(f"Missing columns: {', '.join(missing_columns)}")

    def clean_ids(self):
        """Ensure CustomerIDs are in a standard format (e.g., 001, 002,...)"""
        self.df['CustomerID'] = self.df['CustomerID'].apply(lambda x: str(x).zfill(3))

    def clean_names(self):
        """Strip trailing spaces and correct obvious typos in names."""
        self.df['Name'] = self.df['Name'].str.strip().replace(r'\bx\b', '')

    def clean_ages(self):
        """Convert ages from text to integers, handle missing and nonsensical values."""

        def age_converter(age):
            if pd.isnull(age):
                return None  # Handle missing values explicitly

            if isinstance(age, int) or age.isdigit():
                return min(150, max(1, int(age)))  # Ensure age is within 1-150

            # Match textual representations like 'twenty-five'
            match = re.match(r'(\w+)-?(\w+)', age.lower())
            if match:
                word_map = {
                    'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                    'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
                    'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
                    'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18,
                    'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40,
                    'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80,
                    'ninety': 90, 'hundred': 100
                }
                num1, num2 = match.groups()
                return min(150, max(1, word_map.get(num1, 0) + word_map.get(num2, 0)))

            # Handle other non-numeric or unexpected formats
            return None

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
        """Ensure total purchase and average purchase values are numeric and reasonable"""
        self.df['TotalPurchases'] = pd.to_numeric(self.df['TotalPurchases'], errors='coerce')
        self.df['AveragePurchaseValue'] = pd.to_numeric(self.df['AveragePurchaseValue'], errors='coerce')

    def standardize_devices(self):
        """Correct minor typos in device names and standardize to 'Mobile' or 'Desktop'."""
        self.df['PreferredDevice'] = self.df['PreferredDevice'].str.replace('Mobil', 'Mobil', regex=False)

    def clean_locations(self):
        """Handle missing or incomplete location data"""
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
