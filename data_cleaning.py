import pandas as pd  # Add this import statement

try:
    from faker import Faker
except ModuleNotFoundError:
    print("The 'faker' module is not installed. Please install it using 'pip install faker'.")
    exit(1)

def clean_data(file_path):
    # Load the CSV file
    df = pd.read_csv(file_path)
    
    # Detect and clean errors column-wise
    for column in df.columns:
        if df[column].dtype == 'object':
            # Remove leading/trailing whitespace
            df[column] = df[column].str.strip()
            # Replace empty strings with NaN
            df[column].replace('', pd.NA, inplace=True)
        elif df[column].dtype in ['int64', 'float64']:
            # Replace negative values with NaN
            df[column] = df[column].apply(lambda x: pd.NA if x < 0 else x)
    
    # Drop rows with any NaN values
    df.dropna(inplace=True)
    
    # Save the cleaned data to a new CSV file
    cleaned_file_path = file_path.replace('.csv', '_cleaned.csv')
    df.to_csv(cleaned_file_path, index=False)
    
    return cleaned_file_path

# Example usage
if __name__ == "__main__":
    file_path = 'C:/Users/perumalm/Desktop/GIT/githubemc02/sample_data_with_errors.csv'  # Update this line
    cleaned_file_path = clean_data(file_path)
    print(f"Cleaned data saved to {cleaned_file_path}")
