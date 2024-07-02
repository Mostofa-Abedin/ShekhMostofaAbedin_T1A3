# # This file is to to used for misc testing purpose. Delete at the end before submitting.
# from datetime import datetime
# from upload_file import car_database
# from search_database import search_database

# Make = "Toyota"
# Model = "Corolla"
# Year = int(2019)
# Mileage = float(5000)

# def estimate_price(Make, Model, Year, Mileage):
#     try:
#          # Validate the types of the inputs
#         if not isinstance(Make, str):
#             raise TypeError("Make should be a string.")
#         if not isinstance(Model, str):
#             raise TypeError("Model should be a string.")
#         if not isinstance(Year, int):
#             raise TypeError("Year should be an integer.")
#         if not isinstance(Mileage, (int, float)):
#             raise TypeError("Price should be a number.")
#         # Estimate car price
#         # Get the current date and time
#         today = datetime.now()
#         # Extract the year
#         current_year = today.year
#         Depreciation_rate = 0.05
#         Mileage_adjustment_factor = 0.01
        
#         # Debug print to check car_database contents
#         print(f"car_database contents: {car_database}")
        
#         # base_price = car_database.get((Make, Model, Year))
        
#         base_price = search_database(Make, Model, Year)
        
#         # Debug print to check base_price
#         print(f"Base price retrieved: {base_price}")
        
#         price = base_price-(Depreciation_rate*(Year-current_year)*base_price)+(Mileage_adjustment_factor*Mileage)
        
       
#         return price
             
#     except TypeError as te:
#         return f"TypeError: {te}"
#     except Exception as e:
#         return f"An unexpected error occurred: {e}"

# result = estimate_price(Make, Model, Year, Mileage)
# print(result)


#--------------------------------------------------x----------------------------------------------------------------------------------------


# Import the search_database function from the search_database module
from search_database import search_database
from datetime import datetime

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
            raise TypeError("Price should be a number.")
        
        # Get the base price of the car from the database using search_database function
        base_price = search_database(make, model, year)
        # If the car is not found, return the message "Car not found"
        if base_price == "Car not found in the database2":
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
        price = base_price - (depreciation_rate * years_old * base_price) + (mileage_adjustment_factor * mileage)
        # Return the calculated price
        return price
    
    except TypeError as te:
        return f"TypeError: {te}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
