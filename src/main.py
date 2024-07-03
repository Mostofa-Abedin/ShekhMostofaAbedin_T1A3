# Importing necessary functions from their respective modules in the src package
from upload_file import upload_file
from search_database import search_database
from append_database import append_database
from estimate_price import estimate_price
# from find_cars_by_budget import find_cars_by_budget

# Delete this later
# from testing_file_to_be_deleted import estimate_price



# Create a function to run the Car Dealership Management System
def main():
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
            # Option 2: Search car database
            
            make = input("Enter Make: ")
            model = input("Enter Model: ")
            year = int(input("Enter Year: "))
            price = search_database(make, model, year)
            try:
                # Attempt to convert price to float
                price_float = float(price)
                # If successful, print the formatted price message
                print(f"The price of {year} {make} {model} is {price_float}")
            except ValueError:
                # If conversion fails, price is a string (error message), so print it directly
                print(price)

        elif choice == '3':
            # Option 3: Append to car database
            make = input("Enter Make: ")
            model = input("Enter Model: ")
            year = input("Enter Year: ")
            price = input("Enter Price: ")
            
            try:
                year = int(year)  # Convert year to an integer
                price = float(price)  # Convert price to a float
            except ValueError:
                print("Year must be an integer and Price must be a number.")
                continue

            # Call the append_database function with the provided inputs
            append_database(make, model, year, price)
            
        elif choice == '4':
            # Option 4: Estimate used car price
            make = input("Enter Make: ")
            model = input("Enter Model: ")
            year = input("Enter Year: ")
            mileage = input("Enter Mileage: ")
            
            try:
                year = int(year)  # Convert year to an integer
                mileage = float(mileage)  # Convert mileage to a float
            except ValueError:
                print("Year must be an integer and Mileage must be a number.")
                continue
            price = estimate_price(make,model,year,mileage)
            print(f"The value of a {year} {make} {model} is {price}")
            
            
        # elif choice == '5':
            
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