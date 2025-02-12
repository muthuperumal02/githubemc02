import mysql.connector  # Add this import statement
import csv
import os

# MySQL database connection details
db_config = {
    'user': 'your_username',  # Replace with your actual username
    'password': 'your_password',  # Replace with your actual password
    'host': 'localhost',
    'database': 'your_database'  # Replace with your actual database name
}

# Connect to the MySQL database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Function to load CSV data into a MySQL table
def load_csv_to_mysql(file_path, table_name):
    with open(file_path, mode='r') as file:
        csv_data = csv.reader(file)
        headers = next(csv_data)
        columns = ', '.join(headers)
        placeholders = ', '.join(['%s'] * len(headers))
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        
        for row in csv_data:
            cursor.execute(insert_query, row)
        conn.commit()

# Define the file paths and table names
files_and_tables = [
    (r"C:\Users\perumalm\Desktop\GIT\MySQL server\Product.csv", "Product"),
    (r"C:\Users\perumalm\Desktop\GIT\MySQL server\Customer.csv", "Customer"),
    (r"C:\Users\perumalm\Desktop\GIT\MySQL server\sales_data.csv", "Sales")
]

# Load each CSV file into the corresponding MySQL table
for file_path, table_name in files_and_tables:
    load_csv_to_mysql(file_path, table_name)
    print(f"Data from {file_path} has been loaded into the {table_name} table.")

# Close the database connection
cursor.close()
conn.close()
