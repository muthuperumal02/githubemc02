import pandas as pd
import random  # Add this import statement
import numpy as np  # Add this import statement
import os

try:
    from faker import Faker
except ModuleNotFoundError:
    print("The 'faker' module is not installed. Please install it using 'pip install faker'.")
    exit(1)

# Initialize Faker instance for random data generation
fake = Faker()

# Create a list to hold rows of the data
data = []

# Define categories for 'Product' and 'SalesRegion'
products = ['Widget', 'Gadget', 'Widgets', 'Widge', 'Wdgt', 'Gadgets']
regions = ['NorthEast', 'SouthWest', 'NorthWest', 'SouthEast', 'East', 'West', 'Unknown']

# Generate 1000 rows with errors
for i in range(1000):
    row = {}
    
    # ID: Random ID, some duplicates will be included
    row['ID'] = random.choice([i, i - 1])  # Some duplicated IDs
    
    # Date: Random date, with some errors
    date = fake.date_this_year()
    if random.random() < 0.05:  # 5% chance of incorrect date format
        date = '2025-01-XX'
    row['Date'] = date
    
    # Product: Random product, some misspelled values
    product = random.choice(products)
    row['Product'] = product
    
    # Amount: Random amounts with errors (outliers, missing, non-numeric)
    if random.random() < 0.05:  # 5% chance of non-numeric amount
        row['Amount'] = 'abc'
    else:
        amount = random.uniform(1, 5000)
        if random.random() < 0.05:  # 5% chance of an outlier
            amount = random.uniform(5000, 100000)
        row['Amount'] = round(amount, 2)
    
    # CustomerAge: Random age, sometimes negative or missing
    if random.random() < 0.1:  # 10% chance of missing age
        row['CustomerAge'] = np.nan
    else:
        age = random.randint(-5, 100)
        row['CustomerAge'] = age
    
    # SalesRegion: Random region, with some invalid values
    region = random.choice(regions)
    row['SalesRegion'] = region
    
    data.append(row)

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Define output path
output_dir = "C:/Users/perumalm/Desktop/GIT/githubemc02"
file_name = "sample_data_with_errors.csv"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

file_path = os.path.join(output_dir, file_name)

# Save the DataFrame to a CSV file
print(f"Saving dataset to {output_dir}...")
df.to_csv(file_path, index=False)
print("Dataset saved successfully.")
