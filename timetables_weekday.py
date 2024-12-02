import os
import pandas as pd
from bs4 import BeautifulSoup

def extract_timetables(html_file_path):
    # Load the HTML file
    with open(html_file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')

    # Find the parent container of the accordions
    accordion_container = soup.find(class_='AccordionList-container')

    # If the container isn't found, return to avoid errors
    if accordion_container is None:
        print("Accordion list container not found.")
        return

    # Find all accordion divs
    accordions = accordion_container.find_all('div', class_='aem-container Accordion')

    for accordion in accordions:
        # Extract the train name
        train_name = accordion.find('button', class_='Accordion-button').text.strip()
        print(f"Processing schedule for: {train_name}")

        # Find the table within the accordion
        table = accordion.find('table')
        if table:
            # Parse the table using pandas
            df = pd.read_html(str(table))[0]
            # Ensure column names are string type and standardize column names by removing newlines and extra spaces
            df.columns = [str(col).replace('\n', ' ').strip() for col in df.columns]
            # Create CSV file
            filename = f"{train_name.replace(' - ', ' -').replace(' ', '_').replace('+', '').replace('-', '').strip()}.csv"
            df.to_csv(filename, index=False)
            print(f"Exported {filename}")

        else:
            print(f"No table found for {train_name}")

# Example usage
html_file_path = 'weekend.html'
extract_timetables(html_file_path)
