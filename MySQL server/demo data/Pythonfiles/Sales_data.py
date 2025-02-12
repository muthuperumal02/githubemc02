import csv
import random
import os

# Define the file path
file_path = r"C:\Users\perumalm\Desktop\GIT\MySQL server\sales_data.csv"

# Generate sales data
sales_data = []
for i in range(100):
    sale_id = i + 1
    product_id = random.randint(1, 50)
    quantity_sold = random.randint(1, 20)
    sale_amount = round(random.uniform(10.0, 1000.0), 2)
    sales_data.append([sale_id, product_id, quantity_sold, sale_amount])

# Write sales data to CSV file
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SaleID", "ProductID", "QuantitySold", "SaleAmount"])
    writer.writerows(sales_data)

print(f"Sales data has been generated and saved to {file_path}")