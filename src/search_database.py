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
            # print(Make,Model,Year) #Debug print
            # print(f"Database entry: {(car_make, car_model, car_year)} -> {price}")  # Debug print
            # print(car_make)
            # print(Make)
            # if car_make == Make:
            #     print(True)
            # else:
            #     print(False)
            
            # print(car_model)
            # print(Model)
            # if car_model == Model:
            #     print(True)
            # else:
            #     print(False)
                
            # print(car_year)
            # print(Year)
            # if car_year == Year:
            #     print(True)
            # else:
            #     print(False)
            
            # Compare each attribute and print debug information
            if car_make == Make:
                print(f"Make matches: {car_make} == {Make}")
            else:
                print(f"Make does not match: {car_make} != {Make}")
            
            if car_model == Model:
                print(f"Model matches: {car_model} == {Model}")
            else:
                print(f"Model does not match: {car_model} != {Model}")
            
            if car_year == Year:
                print(f"Year matches: {car_year} == {Year}")
            else:
                print(f"Year does not match: {car_year} != {Year}")

            if car_make == Make and car_model == Model and car_year == Year:
                return price
        
        # If no matching car is found, return a message
        return "Car not found in the database"
           
    
    except TypeError as te:
        return f"TypeError: {te}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"



