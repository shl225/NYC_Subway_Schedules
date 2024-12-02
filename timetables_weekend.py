import os
import pandas as pd
from bs4 import BeautifulSoup

def extract_timetables(html_file_path):
    # Load the HTML file
    with open(html_file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')

    # Find all accordion containers and their preceding titles
    containers = soup.find_all(class_='AccordionList-container')
    for container in containers:
        # Attempt to find the preceding sibling with a date
        title_tag = container.find_previous_sibling(class_='Title AccordionList-title')
        if title_tag:
            date_text = title_tag.text.strip()
            print(f"Processing schedules for date: {date_text}")
            # Normalize the date text for use in filenames and directory names
            safe_date = date_text.replace(', ', '_').replace(' ', '_')
            # Ensure directory for this date exists
            if not os.path.exists(safe_date):
                os.makedirs(safe_date)
        else:
            safe_date = 'Unknown_Date'
            print("No date found for one of the schedule sections.")
        
        # Process each accordion within the container
        accordions = container.find_all('div', class_='aem-container Accordion')
        for accordion in accordions:
            # Extract the train name
            train_name = accordion.find('button', class_='Accordion-button').text.strip().replace(' - ', ' -').replace(' ', '_').replace('+', '').replace('-', '').strip()
            # Find the table within the accordion
            table = accordion.find('table')
            if table:
                # Parse the table using pandas
                df = pd.read_html(str(table))[0]
                # Ensure column names are string type
                df.columns = [str(col).replace('\n', ' ').strip() for col in df.columns]
                # Create CSV file within the date directory
                filename = os.path.join(safe_date, f"{train_name}.csv")
                df.to_csv(filename, index=False)
                print(f"Exported {filename}")
            else:
                print(f"No table found for {train_name}")

# Example usage
html_file_path = 'weekend.html'
extract_timetables(html_file_path)
