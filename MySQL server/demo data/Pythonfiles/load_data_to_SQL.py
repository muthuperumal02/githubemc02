import pandas as pd
import os

import mysql.connector

# MySQL database connection details
db_config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'your_database'
}

# Path to the directory containing CSV files
csv_directory = r'C:\Users\perumalm\Desktop\GIT\MySQL server'

# Establish a database connection
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Function to load a CSV file into a MySQL table
def load_csv_to_mysql(file_path, table_name):
    df = pd.read_csv(file_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)

# Iterate over all CSV files in the directory
for file_name in os.listdir(csv_directory):
    if file_name.endswith('.csv'):
        file_path = os.path.join(csv_directory, file_name)
        table_name = os.path.splitext(file_name)[0]
        load_csv_to_mysql(file_path, table_name)

# Close the database connection
cursor.close()
conn.close()