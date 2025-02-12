import csv
import random
import os

# Define the file path for the product data
product_file_path = r"C:\Users\perumalm\Desktop\GIT\MySQL server\Product.csv"

# Generate product data
product_data = []
for product_id in range(1, 51):
    product_name = f"Product_{product_id}"
    product_price = round(random.uniform(5.0, 500.0), 2)
    product_data.append([product_id, product_name, product_price])

# Write product data to CSV file
with open(product_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["ProductID", "ProductName", "ProductPrice"])
    writer.writerows(product_data)

print(f"Product data has been generated and saved to {product_file_path}")
