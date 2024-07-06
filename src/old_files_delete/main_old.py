# Importing necessary functions from their respective modules in the src package
from upload_file import upload_file
from search_database import search_database
from append_database import append_database
from estimate_price import estimate_price
from find_cars_by_budget import find_cars_by_budget

# Delete this later
#from testing_file_to_be_deleted import find_cars_by_budget



# Create a function to run the Car Dealership Management System
def main():
    global file_path
    file_path = None  # Initialize file_path to None
	# Use a while loop to continiously show options
    while True:
        # Display the menu options to the user
        print("\nWelcome to the car Dealership Management System")
        print("1. Upload to car database")
        print("2. Search car database")
        print("3. Append to car database")
        print("4. Estimate used car price")
        print("5. Find cars by budget")
        print("6. Exit")

        # Get the user's choice from the menu
        choice = input("Choose an option: ")

        if choice == '1':
            # Option 1: Upload car database
            file_path = input("Enter file path: ")
            upload_file(file_path)
            
        elif choice == '2':
            if not file_path:
                print("Please upload a file first using option 1.")
                continue
            # Option 2: Search car database
            make = input("Enter Make: ")
            model = input("Enter Model: ")
            year = input("Enter Year: ")
            
            try:
                year = int(year)  # Convert year to an integer

                # Validate that Make contains only alphabetic characters
                if not make.isalpha():
                    raise ValueError("Make should contain only alphabetic characters.")
               
                
                price = search_database(make, model, year)
                
                try:
                    # Attempt to convert price to float
                    price_float = float(price)
                    # If successful, print the formatted price message
                    print(f"The price of {year} {make} {model} is {price_float}")
                except ValueError:
                    # If conversion fails, price is a string (error message), so print it directly
                    print(price)
            
            except ValueError as ve:
                # Handle invalid year or invalid make/model input
                print(ve)


        elif choice == '3':
            if not file_path:
                print("Please upload a file first using option 1.")
                continue
            # Option3: Append database
            make = input("Enter Make: ")
            model = input("Enter Model: ")
            year = input("Enter Year: ")
            price = input("Enter Price: ")
            try:
                year = int(year)
                price = float(price)
                if not make.isalpha():
                    raise ValueError("Make should contain only alphabetic characters.")
            
                append_to_csv = input("Would you like to append this to the CSV file? (yes/no): ").strip().lower()
                if append_to_csv == 'yes' and file_path:
                    append_database(make, model, year, price, file_path)
                else:
                    append_database(make, model, year, price)
            except ValueError:
                print("Year must be an integer and Price must be a number.")
            except TypeError as te:
                print(te)
                
        elif choice == '4':
            if not file_path:
                print("Please upload a file first using option 1.")
                continue
            # Option 4: Estimated used car value
            make = input("Enter Make: ")
            model = input("Enter Model: ")
            year = input("Enter Year: ")
            mileage = input("Enter Mileage: ")
            try:
                year = int(year)
                mileage = float(mileage)
                if not make.isalpha():
                    raise ValueError("Make should contain only alphabetic characters.")
                if not model.isalpha():
                    raise ValueError("Model should contain only alphabetic characters.")
                price = estimate_price(make, model, year, mileage)
                if isinstance(price, (int, float)):
                    print(f"The value of a {year} {make} {model} is {price}")
                else:
                    print(price)
            except ValueError:
                print("Year must be an integer and Mileage must be a number.")
            except TypeError as te:
                print(te)

            
            
        elif choice == '5':
            if not file_path:
                print("Please upload a file first using option 1.")
                continue
            # Option 5: Find cars within Budget
            price = input("Enter Maximum Budget: ")
            make = input("Enter Make (optional): ")
            try:
                price = float(price)
                if make and not make.isalpha():
                    raise ValueError("Make should contain only alphabetic characters.")
                if make == "":
                    make = None
                cars = find_cars_by_budget(price, make)
                if isinstance(cars, list):
                    for car in cars:
                        print(f"Make: {car[0]}, Model: {car[1]}, Year: {car[2]}, Price: {car[3]}")
                else:
                    print(cars)
            except ValueError as ve:
                print(f"Invalid input: {ve}")
            
        
            
        elif choice == '6':
            # Option 6: Exit the application
            print("Exiting the application. Goodbye!")
            break
           
        # else:
            # Handle invalid menu choice
            print("Invalid choice. Please try again.")

# Entry point of the application
if __name__ == "__main__":
    # Call the main function to start the application
    main()