
# Import the search_database function from the search_database module
from upload_file import car_database


# Function to find cars in Budget
def find_cars_by_budget(make, price):
    try:
        #  # Validate the types of the inputs
        # if not isinstance(make, str):
        #     raise TypeError("Make should be a string.")
        # if not isinstance(price, (int, float)):
        #     raise TypeError("Price should be a number.")
        
        # found_car = []
        
        # for car_type,car_price in car_database.items():
        #     if car_price <= price: 
        #         found_car.append ((car_type,car_price))
        #         return found_car
        
        # return "No Car found"
        
        # Initialize an empty list to store the results
        car_found = []
        
        # Iterate over each car in the car database
        for (find_make, find_model, find_year), find_price in car_database.items():
            # Check if the car is within the budget
            # If preferred_make is specified, also check if the car's make matches the preferred make
            if find_price <= price and (make is None or make == find_make):
                # Add the car details to the results list
                car_found.append((find_make, find_model, find_year, find_price))
        # Return the list of cars that match the criteria
        return car_found
    
    except TypeError as te:
        return f"TypeError: {te}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
