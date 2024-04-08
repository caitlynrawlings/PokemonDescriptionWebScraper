import csv

csv_file = 'pokemon_info.csv'

# List to store the name values which are in column 30
name_values = []

with open(csv_file, 'r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    
    for row in csv_reader:
        # Check if the row has at least 31 columns (0-indexed)
        if len(row) >= 31:
            # Append the value from column 30 (index 29, since indexing starts from 0)
            name_values.append(row[30])
