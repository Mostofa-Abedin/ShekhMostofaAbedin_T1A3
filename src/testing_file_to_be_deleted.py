# This file is to to used for misc testing purpose. Delete at the end before submitting.

from upload_file import car_database

def append_database(Make, Model, Year, Price):
    try:
        # Check if inputs are of the expected types
        if not isinstance(Make, str) or not isinstance(Model, str) or not isinstance(Year, int) or not isinstance(Price, (int, float)):
            raise TypeError("Make and Model should be strings, Year should be an integer, and Price should be a number.")
        
        # Create a new entry for the car
        new_car = {(Make, Model, Year): Price}
        
        # Update the car database with the new entry
        car_database.update(new_car)
        
        # Return the updated car database
        print(f"{Year} {Make} {Model} was added sucessfully")
        return car_database
        
    
    except TypeError as te:
        return f"TypeError: {te}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"







