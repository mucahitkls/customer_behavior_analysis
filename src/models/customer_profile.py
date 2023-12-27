class CustomerProfile:
    def __init__(self):

        self.expected_columns = [
            "CustomerID", "Name", "Age", "Email", "SignUpDate",
            "LastPurchaseDate", "TotalPurchases", "AveragePurchaseValue",
            "PreferredDevice", "Location"
        ]

    def update_profile(self, **kwargs):
        """Update the customer's profile with the given keyword arguments"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def display_profile(self):
        """Print the customer's profile information."""
        profile_info = vars(self)
        for key, value in profile_info.items():
            print(f"{key}: {value}")
