import pandas as pd


class AnalysisEngine:
    def __init__(self, data):
        self.data = pd.DataFrame(data)  # Assuming data is a list of dictionaries or a dataframe
        self.expected_columns = [
            "CustomerID", "Name", "Age", "Email", "SignUpDate",
            "LastPurchaseDate", "TotalPurchases", "AveragePurchaseValue",
            "PreferredDevice", "Location"
        ]

    def perform_purchase_segmentation(self):
        """Segment customers based on total purchases criteria.
            :returns
            - High - if total_purchases > 50
            - Low - else
        """
        # Implement segmentation logic
        if self.check_if_all_numeric(key='TotalPurchases'):
            self.data['Purchase_Segment'] = self.data['TotalPurchases'].apply(
                lambda x: 'High' if int(x) > 50 else 'Low')
        pass

    def perform_age_segmentation(self):
        """
            Segment customers based on age criteria.
            :returns:
            Young - If age < 18
            Middle - If  18 <= age < 40
            Old - if 40 <= age
        """
        key = 'Age'
        if self.check_if_all_numeric(key=key):
            self.data['Age_Segment'] = self.data['Age'].apply(
                lambda x: 'Young' if int(x) < 18 else ('Middle' if 18 <= int(x) < 40 else 'Old'))

        pass

    def calculate_lifetime_value(self):
        """ Calculates and add a lifetime value metric for each customer.
            Life_Time_Value = AveragePurchaseValue * TotalPurchases
        """

        if self.check_if_all_numeric(key='AveragePurchaseValue') and self.check_if_all_numeric(key='TotalPurchases'):
            self.data['Life_Time_Value'] = self.data['AveragePurchaseValue'] * self.data['TotalPurchases']

    def check_if_all_numeric(self, key):
        """Check if all non-null values in the column are numeric (int or float)."""
        # Attempt to convert the column to a numeric type.
        # 'coerce' will set values that cannot be converted to numeric as NaN.
        numeric_col = pd.to_numeric(self.data[key], errors='coerce')

        # Check if there are any NaNs left (originally non-numeric values).
        # If not, all original non-null values were numeric.
        return not numeric_col.isnull().any()

    def check_if_all_integer(self, key):
        """Check if all non-null values in the column are of integer type."""
        # Convert column to numeric first (to handle strings and other types).
        numeric_col = pd.to_numeric(self.data[key], errors='coerce')

        # Drop NaNs (which represent original non-numeric values or missing values)
        # and then check if all values are integers.
        return (numeric_col.dropna() % 1 == 0).all()
