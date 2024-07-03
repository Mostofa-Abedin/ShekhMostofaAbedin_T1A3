
# Import the search_database function from the search_database module
from upload_file import car_database


# Function to estimate the price of a used car
def find_cars_by_budget(make, price):
    try:
         # Validate the types of the inputs
        if not isinstance(make, str):
            raise TypeError("Make should be a string.")
        if not isinstance(price, (int, float)):
            raise TypeError("Price should be a number.")
        
        found_car = []
        
        for car_type,car_price in car_database.items():
            if car_price <= price: 
                found_car.append ((car_type,car_price))
                return found_car
        
        return "No Car found"
    
    except TypeError as te:
        return f"TypeError: {te}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
