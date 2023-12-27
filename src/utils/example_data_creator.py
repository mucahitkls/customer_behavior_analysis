from faker import Faker
import random
import pandas as pd
from datetime import datetime

# Initialize Faker
fake = Faker()

# Define number of customers
num_customers = 1000

# Create empty list to hold customer data
customers = []

# Define a function to randomly create some data inconsistencies
def add_noise(data, noise_chance=0.1):
    if random.random() < noise_chance:
        if data.isdigit():  # For age, create some non-digit entries
            return ''.join(random.choice(['twenty', 'thirty', 'forty']) + '-five')
        elif '@' in data:  # For email, create some missing or incomplete entries
            return random.choice(['', 'missing', data.split('@')[0]])
        elif '-' in data:  # For dates, mess up the format or leave it empty
            return random.choice(['', '2023/12/01', 'wrong_date'])
        else:  # For other text fields, add typos or leave them empty
            return random.choice(['', data[:-1], data + 'x'])
    return data

# Generate customer data
for _ in range(num_customers):
    customer_id = str(_ + 1).zfill(3)
    name = fake.name()
    age = str(random.randint(13, 70))
    email = fake.email()
    sign_up_date = fake.date_between(start_date='-3y', end_date='today')
    # Ensure last_purchase_date is after the sign_up_date
    last_purchase_date = fake.date_between(start_date=sign_up_date, end_date='today')
    total_purchases = str(random.randint(1, 100))
    avg_purchase_value = str(round(random.uniform(20.0, 100.0), 2))
    preferred_device = random.choice(['Mobile', 'Desktop'])
    location = fake.city()

    # Add noise to the data to simulate real-world inconsistencies
    customer = [
        add_noise(customer_id),
        add_noise(name),
        add_noise(age),
        add_noise(email),
        add_noise(str(sign_up_date)),
        add_noise(str(last_purchase_date)),
        add_noise(total_purchases),
        add_noise(avg_purchase_value),
        add_noise(preferred_device),
        add_noise(location)
    ]

    customers.append(customer)

# Create a DataFrame
customer_df = pd.DataFrame(customers, columns=[
    "CustomerID", "Name", "Age", "Email", "SignUpDate", "LastPurchaseDate",
    "TotalPurchases", "AveragePurchaseValue", "PreferredDevice", "Location"
])

# Display the first few rows of the dataset
customer_df.to_csv("example_data.csv")
