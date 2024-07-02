# append_database.py
from upload_file import car_database  # Import the shared car_database

def append_database(make, model, year, price):
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
        
        # Print success message
        print(f"{year} {make} {model} was added successfully.")

    except TypeError as te:
        print(f"TypeError: {te}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

