import csv  # Importing the CSV module to handle CSV file operations

# Global dictionary to store car details
car_database = {}

# Function to upload a car database from a CSV file
def upload_file(file_path):
    global car_database  # Accessing the global car_database variable
    try:
        # Open the CSV file for reading
        with open(file_path, 'r') as file:
            # Create a CSV dictionary reader to parse the file
            reader = csv.DictReader(file)
            # Check if CSV file has the correct headers
            required_headers = {'Make', 'Model', 'Year', 'Price'}
            if not required_headers.issubset(reader.fieldnames):
                print("Error: CSV file is missing one or more required headers.")
                sys.exit(1)  # Exit the program with a non-zero status
            # Initialize a counter for the row number
            row_number = 0
            # Iterate over each row in the CSV file
            for row in reader:
                row_number += 1
                try:
                    # Ensure all required fields are present
                    if 'Make' not in row or 'Model' not in row or 'Year' not in row or 'Price' not in row:
                        raise ValueError(f"Missing required fields in row {row_number}")
                    # Create a key using the Make, Model, and Year from the row
                    key = (row['Make'], row['Model'], int(row['Year']))
                     # Check for duplicate entry
                    if key in car_database:
                        raise ValueError(f"Duplicate entry found for {row['Make']} {row['Model']} {row['Year']} in row {row_number}")
                    # Store the Price in the car database dictionary, converting it to a float
                    car_database[key] = float(row['Price'])
                except ValueError as ve:
                    # Print error if required fields are missing or other ValueError occurs
                    print(f"Error in row {row_number}: {ve}")
                except Exception as e:
                    # Print any other unexpected errors
                    print(f"Unexpected error in row {row_number}: {e}")
        # Print success message after file is uploaded and processed
        print("File uploaded successfully.")
    except FileNotFoundError:
        # Handle file not found error
        print("Error: File not found. Please check the file path.")
    except Exception as e:
        # Handle other exceptions and print the error message
        print(f"An error occurred: {e}")

