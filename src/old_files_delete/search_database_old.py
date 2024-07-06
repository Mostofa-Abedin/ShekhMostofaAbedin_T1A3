# Import the car_database from the upload_file module
from upload_file import car_database

def search_database(Make, Model, Year):
    try:
        # Validate the types of the inputs
        if not isinstance(Make, str):
            raise TypeError("Make should be a string.")
        if not isinstance(Model, str):
            raise TypeError("Model should be a string.")
        if not isinstance(Year, int):
            raise TypeError("Year should be an integer.")
        
        # Iterate through the car_database to find the matching car
        for (car_make, car_model, car_year), price in car_database.items():
            if car_make == Make and car_model == Model and car_year == Year:
                return price
        
        # If no matching car is found, return a message
        return "Car not found in the database"
           
    
    except TypeError as te:
        return f"TypeError: {te}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"



