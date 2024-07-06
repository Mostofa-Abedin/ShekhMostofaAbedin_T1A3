# Import CSV module and sys module.
import csv  
import sys  

# Create a Global dictionary to store car details.
car_database = {}

# Start function to upload a car database from a CSV file
def upload_file(file_path):
    global car_database  # Access the global car_database variable that is outside the function.
    try:
        # Open the CSV file in read mode. 
        with open(file_path, 'r') as file:
            # Parse the csv and store it into variable called reader.
            reader = csv.DictReader(file)
            # Specify the required headers for the CSV file. These are must have. 
            required_headers = {'Make', 'Model', 'Year', 'Price'}
            # Check if the CSV file contains the required headers.This checks if all elements in required_headers are present in reader.fieldnames.
            if not required_headers.issubset(reader.fieldnames):
                # If headers missing, print error message.
                print("Error: CSV file is missing one or more required headers.")
                sys.exit(1)  # After which, the program exits if headers missing. 
            # Headers are valid, move onto creating the dictionary.    
            # Initialize a counter for the row number.
            row_number = 0
            # Iterate over each row in the CSV file.
            for row in reader:
                row_number += 1
                try:
                    # Ensure all required fields are present in the row. If not raise error.
                    if 'Make' not in row or 'Model' not in row or 'Year' not in row or 'Price' not in row:
                        raise ValueError(f"Missing required fields in row {row_number}")
                    # Create a key thats is a tuple using the Make, Model, and Year from the row.
                    key = (row['Make'], row['Model'], int(row['Year']))
                    # Check for duplicate entry in the dictionary. Raise error if duplicated found. 
                    if key in car_database:
                        raise ValueError(f"Duplicate entry found for {row['Make']} {row['Model']} {row['Year']} in row {row_number}")
                    # Store the Price as the value of the key in the car database dictionary, converting it to a float.
                    car_database[key] = float(row['Price'])
                # Throw error messages 
                except ValueError as ve:
                    # Print error if required fields are missing or other ValueError occurs
                    print(f"Error in row {row_number}: {ve}")
                except Exception as e:
                    # Print any other unexpected errors
                    print(f"Unexpected error in row {row_number}: {e}")
        # Print a success message after file is uploaded and parsed.
        print("File uploaded successfully.")
    except FileNotFoundError:
        # If file not found return error. 
        print("Error: File not found. Please check the file path.")
    except Exception as e:
        # Handle other exceptions and print the error message.
        print(f"An error occurred: {e}")
