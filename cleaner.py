import pandas as pd
import os
import re

def clean_csv(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Detect and remove numerical indices that might mistakenly appear as headers
    if df.columns[0].isdigit():
        df.columns = df.iloc[0]  # Set the first row as the header
        df = df[1:].reset_index(drop=True)  # Drop the first row

    df = df[1:].reset_index(drop=True)  # Drop the duplicated header row

    # Function to clean and format each header
    def format_header(header):
        header = re.sub(r'\s+', ' ', header.strip())  # Normalize spaces
        header = re.sub(r'(\w+) Departure', r'\1 (Departure)', header)  # Format "Departure"
        header = re.sub(r'Arrival at (\w+)', r'\1 (Arrival)', header)  # Correct "Arrival at"
        return header

    df.columns = [format_header(col) for col in df.columns]

    # Save the cleaned CSV file
    df.to_csv(file_path, index=False)
    print(f"Cleaned {file_path}")

# Example usage
# clean_csv('path_to_your_file.csv')

def clean_directory_csvs(directory_path):
    # Walk through all directories and files in the given path
    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            # Check if the file is a CSV file
            if filename.endswith('.csv'):
                file_path = os.path.join(root, filename)
                clean_csv(file_path)

# Example directory cleaning
clean_directory_csvs('.')
