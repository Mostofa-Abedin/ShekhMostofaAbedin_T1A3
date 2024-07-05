# Import the car_database from the upload_file module
from upload_file import car_database

# Function to find cars within a budget
def find_cars_by_budget(price, make=None):
    try:
        # Validate the types of the inputs
        if not isinstance(make, (str, type(None))):
            raise TypeError("Make should be a string.")
        if not isinstance(price, (int, float)):
            raise TypeError("Price should be a number.")

        # Initialize an empty list to store the results
        car_found = []

        # Flag to check if the specified make exists in the database
        make_exists = False

        # Iterate over each car in the car database
        for (find_make, find_model, find_year), find_price in car_database.items():
            # Check if the car's make matches the preferred make (if specified)
            if make is None or make == find_make:
                make_exists = True
                # Check if the car is within the budget
                if find_price <= price:
                    # Add the car details to the results list
                    car_found.append((find_make, find_model, find_year, find_price))

        # Check if any cars were found within the budget
        if not car_found:
            if not make_exists:
                return f"No cars found for the make '{make}' in the database."
            else:
                return f"No cars found within the budget of {price} for the make '{make}'."
        else:
            return car_found

    except TypeError as te:
        return f"TypeError: {te}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
