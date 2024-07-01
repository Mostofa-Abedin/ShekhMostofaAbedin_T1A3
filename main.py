# Importing necessary functions from their respective modules in the src package
from src.upload_file import upload_file
from src.search_database import search_database
from src.append_database import append_database
from src.estimate_price import estimate_price
from src.find_cars_by_budget import find_cars_by_budget



# Create a function to run the Car Dealership Management System
def main():
	# Use a while loop to continiously show options
    while True:
        # Display the menu options to the user
        print("\nCar Welcome to the car Dealership Management System")
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
            
        elif choice == '2':
            # Option 2: Search car database
            
        elif choice == '3':
            # Option 3: Append to car database
            
        elif choice == '4':
            # Option 4: Estimate used car price
            
        elif choice == '5':
            
        elif choice == '6':
            # Option 6: Exit the application
           
        else:
            # Handle invalid menu choice
            print("Invalid choice. Please try again.")

# Entry point of the application
if __name__ == "__main__":
    # Call the main function to start the application
    main()