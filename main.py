import csv

# Function to print a specific column from a CSV file
def print_column(csv_file, column_index):
    with open(csv_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Skip the header row
        column_data = [row[column_index] for row in reader]

    # Print the column data
    print(f"Column {column_index + 1} ({header[column_index]}):")
    for item in column_data:
        print(item)

# Example usage: print the first column from a CSV file
csv_file = 'games.csv'
column_index = 2  # Adjust the index based on the column you want (0 for the first column, 1 for the second, etc.)
print_column(csv_file, column_index)