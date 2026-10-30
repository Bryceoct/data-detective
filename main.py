import csv

try:
    with open("customers.csv", "r", newline="") as file:
        reader = csv.reader(file)
        data = list(reader)
        # Checks for an empty dataset before accessing the header row.
        if len(data) > 0:
            print(f"Total Records: {len(data) - 1}")
            print("Total Columns:", len(data[0]))
            print()

            for index, column in enumerate(data[0]):
                print(index + 1, column)

            print("\nFirst 3 Records")
            for record in data[1:4]:
                print(record)
        else:
            print("Error: The CSV file is empty.")

except FileNotFoundError:
    print("Error: CSV file not found.")
