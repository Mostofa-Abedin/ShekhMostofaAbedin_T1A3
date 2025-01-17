# Import the car_database from the upload_file module
from upload_file import car_database

# Function to find cars within a budget.
def find_cars_by_budget(price, make=None):
    try:
        # Check if Make is a string or none. If not raise error.
        if not isinstance(make, (str, type(None))):
            raise TypeError("Make should be a string.")
        # Check if Price is an integer or a float. If not raise error.
        if not isinstance(price, (int, float)):
            raise TypeError("Price should be a number.")

        # Initialize an empty list to store the car that wille be found. 
        car_found = []

        # Initialize make_exists to false.
        make_exists = False

        # Iterate over each car in the car_database. 
        for (find_make, find_model, find_year), find_price in car_database.items():
            # Check if the car's make matches the preferred make (if specified)
            if make is None or make == find_make:
                make_exists = True
                # Check if the car is within the budget.
                if find_price <= price:
                    # If both checks pass, append the car details to the car_found list
                    car_found.append((find_make, find_model, find_year, find_price))

        # Check if any cars were found within the budget.
        if not car_found:
            # If no cars were found, check if the specified make exists in the database
            if not make_exists:
                # Return error message
                return f"No cars found for the make '{make}' in the database."
            else:
                # Return error message
                return f"No cars found within the budget of {price} for the make '{make}'."
        else:
            # Return the list of cars that match the criteria
            return car_found

    except TypeError as te:
        # Return a TypeError message if input types are invalid
        return f"TypeError: {te}"
    except Exception as e:
        # Return a generic error message for any other exceptions
        return f"An unexpected error occurred: {e}"
