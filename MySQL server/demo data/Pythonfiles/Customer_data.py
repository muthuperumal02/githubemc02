import csv
import random
import os

# Define the file path for the customer data
customer_file_path = r"C:\Users\perumalm\Desktop\GIT\MySQL server\Customer.csv"

# Generate customer data
customer_data = []
for customer_id in range(1, 101):
    customer_name = f"Customer_{customer_id}"
    customer_email = f"customer{customer_id}@example.com"
    customer_phone = f"+1-555-010{customer_id:03d}"
    customer_data.append([customer_id, customer_name, customer_email, customer_phone])

# Write customer data to CSV file
with open(customer_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["CustomerID", "CustomerName", "CustomerEmail", "CustomerPhone"])
    writer.writerows(customer_data)

print(f"Customer data has been generated and saved to {customer_file_path}")
