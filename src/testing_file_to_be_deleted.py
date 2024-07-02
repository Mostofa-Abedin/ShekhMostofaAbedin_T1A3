# This file is to to used for misc testing purpose. Delete at the end before submitting.
from datetime import datetime
from upload_file import car_database

def estimate_price(Make, Model, Year, Mileage):
    try:
         # Validate the types of the inputs
        if not isinstance(Make, str):
            raise TypeError("Make should be a string.")
        if not isinstance(Model, str):
            raise TypeError("Model should be a string.")
        if not isinstance(Year, int):
            raise TypeError("Year should be an integer.")
        if not isinstance(Mileage, (int, float)):
            raise TypeError("Price should be a number.")
        # Estimate car price
        # Get the current date and time
        today = datetime.now()
        # Extract the year
        current_year = today.year
        Depreciation_rate = 0.05
        Mileage_adjustment_factor = 0.01
        base_price = car_database.get((Make, Model, Year))
        
        price = base_price-(Depreciation_rate*(Year-current_year)*base_price)+(Mileage_adjustment_factor*Mileage)
        
        return price
             
    except TypeError as te:
        return f"TypeError: {te}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"







