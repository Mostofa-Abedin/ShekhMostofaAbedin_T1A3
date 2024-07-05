import csv  # Importing the CSV module to handle CSV file operations
from upload_file import car_database  # Import the shared car_database

def append_database(make, model, year, price, file_path=None):
    try:
        # Validate the types of the inputs
        if not isinstance(make, str):
            raise TypeError("Make should be a string.")
        if not isinstance(model, str):
            raise TypeError("Model should be a string.")
        if not isinstance(year, int):
            raise TypeError("Year should be an integer.")
        if not isinstance(price, (int, float)):
            raise TypeError("Price should be a number.")

        # Add the new car entry to the database
        car_database[(make, model, year)] = price
        
        # Check if the user wants to append to the CSV file
        if file_path:
            with open(file_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([make, model, year, price])
            print(f"{year} {make} {model} was added to the CSV file successfully.")

        # Print success message for adding to the dictionary
        print(f"{year} {make} {model} was added successfully to the database.")

    except TypeError as te:
        print(f"TypeError: {te}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
