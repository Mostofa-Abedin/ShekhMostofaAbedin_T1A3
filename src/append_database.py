# Import csv and upload_file modules. 
import csv  
from upload_file import car_database

# Start append database function.
def append_database(make, model, year, price, file_path=None):
    try:
        # Check the type of 'make' to ensure it is a string. If not raise error. 
        if not isinstance(make, str):
            raise TypeError("Make should be a string.")
        # Check the type of 'model' to ensure it is a string. If not raise error. 
        if not isinstance(model, str):
            raise TypeError("Model should be a string.")
        # Check the type of 'year' to ensure it is an integer. If not raise error. 
        if not isinstance(year, int):
            raise TypeError("Year should be an integer.")
        # Check the type of 'price' to ensure it is a number (int or float)
        if not isinstance(price, (int, float)):
            raise TypeError("Price should be a number.")

        # Add the new car entry to the car_database dictionary. Make,model and year is a tuple key. Price is the value. 
        car_database[(make, model, year)] = price
        
        # Check if the user wants to append the entry to a CSV file.
        if file_path:
            # file path taken from feature 1. Opens CSV in write mode. Appends to end of CSV.
            with open(file_path, 'a', newline='') as file:
                writer = csv.writer(file)  # Create a CSV writer object
                writer.writerow([make, model, year, price])  # Write the new entry to the CSV file
            # Print success message.
            print(f"{year} {make} {model} was added to the CSV file successfully.")

        # Print a success message for adding the entry to the dictionary
        print(f"{year} {make} {model} was added successfully to the database.")

    except TypeError as te:
        # Print an error message if a TypeError occurs.
        print(f"TypeError: {te}")
    except Exception as e:
        # Print a general error message for any other exceptions.
        print(f"An unexpected error occurred: {e}")
