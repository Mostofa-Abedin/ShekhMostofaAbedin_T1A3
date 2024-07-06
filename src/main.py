# Importing necessary functions from their respective modules in the src package
from upload_file import upload_file
from search_database import search_database
from append_database import append_database
from estimate_price import estimate_price
from find_cars_by_budget import find_cars_by_budget

# This is the start of the main function that displays the main menu.
def main():
    # This variable file_path is necessary for Feature 3 down the line. To make the Append to CSV unctionality work we have to initialize the file_path as none.
    global file_path
    file_path = None  

    while True:
        # These are the main menu options that the user can select.
        print("\nWelcome to the Car Dealership Management System")
        print("1. Upload to car database")
        print("2. Search car database")
        print("3. Append to car database")
        print("4. Estimate used car price")
        print("5. Find cars by budget")
        print("6. Exit")

        # The users input is stored in a variable called choice.
        choice = input("Choose an option: ")
        
        # Option 1: Upload car database.
        
        if choice == '1':
            # The file path must be specified by the user.
            file_path = input("Enter file path: ")
            # The function upload_file is run with the file paht provided.
            upload_file(file_path)

        # Option 2: Search car database
        
        elif choice == '2':
            # Ensure a file is uploaded using option 1 before searching.
            if not file_path:
                print("Please upload a file first using option 1.")
                continue
            # The user is asked to specify Make,Model and Year
            make = input("Enter Make: ")
            model = input("Enter Model: ")
            year = input("Enter Year: ")
            # Start a try block.
            try:
                year = int(year)  # Convert year to an integer
                # Check that Make contains only alphabetic characters in it. If not raise an error.
                if not make.isalpha():
                    raise ValueError("Make should contain only alphabetic characters.")
                # If valid. It can now run the function search_database with user inputs.
                price = search_database(make, model, year)
                # Another try block within for Error handling returned errors within the search_database function
                try:
                    # Attempt to convert price to float
                    price_float = float(price)
                    print(f"The price of {year} {make} {model} is {price_float}")
                except ValueError:
                    print(price)  # If conversion fails, an error has been thrown from within the function. We print the error message directly.
            except ValueError as ve:
                print(ve)  # Handle invalid year or invalid make/model input

        # Option 3: Append to car database
        
        elif choice == '3':
            # Ensure a file is uploaded using option 1 before appending to database. 
            if not file_path:
                print("Please upload a file first using option 1.")
                continue
             # The user is asked to specify Make,Model,Year and Price.
            make = input("Enter Make: ")
            model = input("Enter Model: ")
            year = input("Enter Year: ")
            price = input("Enter Price: ")
            # Start a try block.
            try:
                year = int(year) # Convert Year to integer.
                price = float(price) # Convert price to float.
                # Check that Make contains only alphabetic characters in it. If not raise an error.
                if not make.isalpha():
                    raise ValueError("Make should contain only alphabetic characters.")
                 # If valid. The user is asked if they would also like to append to CSV.
                append_to_csv = input("Would you like to also append this to the CSV file? (yes/no): ").strip().lower()
                # If Yes, and file path exists then the inputs are passed into the function such that CSV is also appended.
                if append_to_csv == 'yes' and file_path:
                    append_database(make, model, year, price, file_path)
                else:
                    # If No, file path is not passed onto function and onlylocal database is updated. 
                    append_database(make, model, year, price)
            # Errors thrown if conversion of Year and Price fails.        
            except ValueError:
                print("Year must be an integer and Price must be a number.")
            except TypeError as te:
                print(te)
                
        # Option 4: Estimate used car price
        
        elif choice == '4':
            # Ensure a file is uploaded using Option 1 before estimating price
            if not file_path:
                print("Please upload a file first using option 1.")
                continue
            # The user is asked to specify Make,Model,Year and Mileage.
            make = input("Enter Make: ")
            model = input("Enter Model: ")
            year = input("Enter Year: ")
            mileage = input("Enter Mileage: ")
            #Start a try block. 
            try:
                year = int(year) # Convert Year to integer.
                mileage = float(mileage) # Convert Mileage to float.
                # Check that Make contains only alphabetic characters in it. If not raise an error.
                if not make.isalpha():
                    raise ValueError("Make should contain only alphabetic characters.")
                # If valid, the users's inputs are passed along to the function estimate_price.
                price = estimate_price(make, model, year, mileage)
                # If the returned price is an integer or float we can display the price straightaway.
                if isinstance(price, (int, float)):
                    print(f"The value of a {year} {make} {model} is {price}")
                # If not a float or integer, it is a message from within the function eg: "After deprication, estimated value is 0. It is only worth scrap value"
                else:
                    print(price)
            # Errors thrown if conversion of Year and Price fails. 
            except ValueError:
                print("Year must be an integer and Mileage must be a number.")
            except TypeError as te:
                print(te)
                
        # Option 5: Find cars within budget
        
        elif choice == '5':
            # Ensure a file is uploaded using Option 1before finding cars within budget
            if not file_path:
                print("Please upload a file first using option 1.")
                continue
            # The user is asked to specify Make and Price
            price = input("Enter Maximum Budget: ")
            make = input("Enter Make (optional): ")
            # Start Try block
            try:
                price = float(price) # Convert price to float.
                # Check that Make contains only alphabetic characters in it. If not raise an error.
                if make and not make.isalpha():
                    raise ValueError("Make should contain only alphabetic characters.")
                # Make is optional. User can choose to specify it or not. If left blank initialize make as none.
                if make == "":
                    make = None
                # If valid, the users input's can be passed along to function find_cars_by_budget.
                cars = find_cars_by_budget(price, make)
                # If the returned variable is a list, then the function has found a list of cars that meet the criteria and a message can be printed.
                if isinstance(cars, list):
                    for car in cars:
                        print(f"Make: {car[0]}, Model: {car[1]}, Year: {car[2]}, Price: {car[3]}")
                # If it is not a list, it is a message from within the function eg: N ocars found with in Budget.
                else:
                    print(cars)
            # Errors throw if conversion of price fails.
            except ValueError as ve:
                print(f"Invalid input: {ve}")
                
        # Option 6: Exit the application
        elif choice == '6':
            # The while loop breaks and exits the program
            print("Exiting the application. Goodbye!")
            break
        # Error message for invalid choice
        else:
            print("Invalid choice. Please try again.")


# Application starting point.
if __name__ == "__main__":
    main()
