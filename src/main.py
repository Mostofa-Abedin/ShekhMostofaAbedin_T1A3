# Importing necessary functions from their respective modules in the src package
from upload_file import upload_file
# from ssearch_database import search_database
# from append_database import append_database
# from estimate_price import estimate_price
# from find_cars_by_budget import find_cars_by_budget
# Delete this later
from testing_file_to_be_deleted import search_database



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
            # Option 2: Search car database
            make = input("Enter Make: ")
            model = input("Enter Model: ")
            year = input("Enter Year: ")
            print(search_database(make, model, year))
        # elif choice == '3':
        #     # Option 3: Append to car database
            
        # elif choice == '4':
        #     # Option 4: Estimate used car price
            
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