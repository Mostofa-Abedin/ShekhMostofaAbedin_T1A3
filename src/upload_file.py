import csv  # Importing the CSV module to handle CSV file operations

# Global dictionary to store car details
car_database = {}

# Function to upload a car database from a CSV file
def upload_file(file_path):
    global car_database  # Accessing the global car_database variable
    with open(file_path, 'r') as file:
            # Create a CSV dictionary reader to parse the file
            reader = csv.DictReader(file)
            # Iterate over each row in the CSV file
            for row in reader:
                    key = (row['Make'], row['Model'], row['Year'])
                    # Store the Price in the car database dictionary, converting it to a float
                    car_database[key] = float(row['Price'])
                
                
        # Print success message after file is uploaded and processed
    print("File uploaded successfully.")

