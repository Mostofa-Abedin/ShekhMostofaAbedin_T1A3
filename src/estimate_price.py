# Import the search_database function, math module and datetime module.
from search_database import search_database
from datetime import datetime  
import math  

# Function to estimate the price of a used car
def estimate_price(make, model, year, mileage):
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
        # Check the type of 'mileage' to ensure it is a number (int or float). If not raise error.
        if not isinstance(mileage, (int, float)):
            raise TypeError("Mileage should be a number.")
        
        # Fetch the base price of the car from the database using search_database function.
        base_price = search_database(make, model, year)
        # If the car is not found, return the message "Car not found in the database".
        if base_price == "Car not found in the database":
            return base_price

        # Ensure base_price is a float
        base_price = float(base_price)

        # Set depreciation rate (5% per year).
        depreciation_rate = 0.05
        # Set mileage adjustment factor (0.01 per mile).
        mileage_adjustment_factor = 0.01
        
        # Get the current date and time.
        today = datetime.now()
        # Extract the current year
        current_year = int(today.year)
        # Calculate the age of the car by subtracting the year from the current year.
        years_old = current_year - int(year)

        # Ensure mileage is an integer.
        mileage = int(mileage)

        # Calculate the depreciation using the math module.
        depreciation = math.prod([depreciation_rate, years_old, base_price])

        # Calculate the mileage adjustment using the math module.
        mileage_adjustment = math.prod([mileage_adjustment_factor, mileage])

        # Calculate the final price.
        price = base_price - depreciation + mileage_adjustment

        # Check if the calculated price is less than or equal to 0
        if price <= 0:
            # If it is let the user know that the car is rubbish!
            return "After depreciation, estimated value is 0. It is only worth scrap value"
        else:
            return price

    except TypeError as te:
        # Return a TypeError message if input types are invalid
        return f"TypeError: {te}"
    except Exception as e:
        # Return a generic error message for any other exceptions
        return f"An unexpected error occurred: {e}"
