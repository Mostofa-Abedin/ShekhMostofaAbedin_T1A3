# Import the car_database from the upload_file module
from upload_file import car_database

# Start Search database function
def search_database(make, model, year):
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
        
        # Iterate through each item in the car_database dictionary.
        for (car_make, car_model, car_year), price in car_database.items():
            # Check if the current car's make, model, and year match the search parameters.
            if car_make == make and car_model == model and car_year == year:
                return price  # Return the price if a matching car is found
        
        # Return a message if no matching car is found in the database
        return "Car not found in the database"
    
    except TypeError as te:
        # Return an error message if a TypeError occurs
        return f"TypeError: {te}"
    except Exception as e:
        # Return a general error message for any other exceptions
        return f"An unexpected error occurred: {e}"
