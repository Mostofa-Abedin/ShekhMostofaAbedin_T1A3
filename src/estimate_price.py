# Import the search_database function from the search_database module
from search_database import search_database
from datetime import datetime
import math


# Function to estimate the price of a used car
def estimate_price(make, model, year, mileage):
    try:
         # Validate the types of the inputs
        if not isinstance(make, str):
            raise TypeError("Make should be a string.")
        if not isinstance(model, str):
            raise TypeError("Model should be a string.")
        if not isinstance(year, int):
            raise TypeError("Year should be an integer.")
        if not isinstance(mileage, (int, float)):
            raise TypeError("Mileage should be a number.")
        
        # Get the base price of the car from the database using search_database function
        base_price = search_database(make, model, year)
        # If the car is not found, return the message "Car not found"
        if base_price == "Car not found in the database":
            return base_price

        # Ensure base_price is a float
        base_price = float(base_price)

        # Example depreciation rate (5% per year)
        depreciation_rate = 0.05
        # Example mileage adjustment factor (0.01 per mile)
        mileage_adjustment_factor = 0.01
        
        #Get the current date and time
        today = datetime.now()
        # Extract the year
        current_year = int(today.year)
        # Calculate the age of the car by subtracting the year from the current year 
        years_old = current_year - int(year)

        # Ensure mileage is an integer
        mileage = int(mileage)

        # Calculate the estimated price using the formula:
        # price = base_price - (depreciation_rate * years_old * base_price) + (mileage_adjustment_factor * mileage)
        # price = base_price - (depreciation_rate * years_old * base_price) + (mileage_adjustment_factor * mileage)
        
        # Calculate the depreciation using math module
        depreciation = math.prod([depreciation_rate, years_old, base_price])

        # Calculate the mileage adjustment using math module
        mileage_adjustment = math.prod([mileage_adjustment_factor, mileage])

        # Calculate the final price
        price = base_price - depreciation + mileage_adjustment
        # Return the calculated price
        return price
    
    except TypeError as te:
        return f"TypeError: {te}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"