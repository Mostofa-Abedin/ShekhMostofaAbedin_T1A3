# <strong style="color:salmon"> About the Project </strong>
This project serves as part of the fulfillment of T1A2: Portfolio towards a Diploma of Information Technology at Coder Academy.

## Important Links 

Link to git repository: https://github.com/Mostofa-Abedin/-ShekhMostofaAbedin-_T1A2.git

## Built with

Python 3.10.12

## Style Guide

PEP8

## Purpose

The aim of this project is to g. 

# <strong style="color:salmon"> Features of Program </strong>

This section provides a high-level overview of the program's features and their underlying logic. It is designed for non-technical users to understand the capabilities and functionality of the program without delving into technical specifics. For a detailed examination of the internal mechanisms of each feature, please refer to the "Code Implementation Plan" section.

## List of Features and their Logic

### <strong style="color:#bc5090"> Main program </strong>

This is the main program. It displays a main menu that asks the user to choose an option from:
- Option 1: Upload car database.
- Option 2: Search car database.
- Option 3: Append to car database.
- Option 4: Estimate used car price.
- Option 5: Find cars within budget.
- Option 6: Exit the application.

From each option, individual functions are run and the output in returned. 

```mermaid
graph TD
  A(["Main Menu"])
  
  B1["Option 1: Upload car database"]
  B2["Option 2: Search car database"]
  B3["Option 3: Append to car database"]
  B4["Option 4: Estimate used car price"]
  B5["Option 5: Find cars within budget"]
  B6["Option 6: Exit the application"]

  C6["Exit"]
  C1["Run Upload car database function"]
  C2["Run Search car database function"]
  C3["Run Append to car database function"]
  C4["Run Estimate used car price function"]
  C5["Run Find cars within budget function"]

  O1["Output"]
  O2["Output"]
  O3["Output"]
  O4["Output"]
  O5["Output"]

  D1["Return"]
  D2["Return"]
  D3["Return"]
  D4["Return"]
  D5["Return"]
  
  A --> B6
  A --> B1
  A --> B2
  A --> B3
  A --> B4
  A --> B5

  B6 --> C6
  B1 --> C1
  B2 --> C2
  B3 --> C3
  B4 --> C4
  B5 --> C5

  C1 --> O1
  C2 --> O2
  C3 --> O3
  C4 --> O4
  C5 --> O5

  O1 --> D1
  O2 --> D2
  O3 --> D3
  O4 --> D4
  O5 --> D5

  D1 --> A
  D2 --> A
  D3 --> A
  D4 --> A
  D5 --> A

```
### <strong style="color:#bc5090"> Feature 1: Upload CSV file and store to local Dictionary. </strong>

From the Main menu, Option 1: Upload to car database. <br><Br>
This feature allows the user to upload a CSV format file to the local database. It asks the user to input the file path of where the file is located. 
- If it the inputs are are <strong style="color:green"> valid</strong> it reads the CSV and upload to local database and prints a success message. It then exits and returns to the main menu.
- If the the inputs are <strong style="color:red"> invalid </strong>. It prints an error message and return to the main menu. 

```mermaid
graph TD
  A(["Main Menu"])
  B(["Option 1: Upload to car database"])
  C(["Ask user for file path"])
  D{"Are inputs valid"}
  E["Read CSV and upload to local database"]
  F["Print success message"]
  G["Print error message"]
  H(["Return"])

  A --> B
  B --> C
  C --> D
  D -->|Yes| E
  D -->|No| G
  E --> F
  F --> H
  G --> H
  H --> A

```
### <strong style="color:#bc5090"> Feature 2: Search through car database to find price of car when it was new. </strong>

From the Main menu, Option 2: Search car database. <br><br>
This feature allows the user to search through the car database to find the price of a specific car when it was new. It asks the user to specify the Make,Model and Year of the vehicle.
- If the inputs are <strong style="color:green"> valid</strong> it loops through the database to find the car and returns the price. It then exits back to the main menu.
- If the inputs are <strong style="color:red"> invalid </strong>, it prints an error message and returns back to the main menu.

```mermaid
graph TD
  A(["Main Menu"])
  B(["Option 2: Search car database"])
  C(["Ask user for Make, Model, and Year"])
  D{"Are inputs valid?"}
  E["Loop through database to find the car"]
  F["Return price of the car"]
  G["Print error message"]
  H(["Return"])

  A --> B
  B --> C
  C --> D
  D -->|Yes| E
  D -->|No| G
  E --> F
  F --> H
  G --> H
  H --> A

```
### <strong style="color:#bc5090"> Feature 3: Append Car Database. </strong>

From the Main menu, Option 3: Append to car database. <br><br>

This feature allows the user to add a new vehicle to the car database. It asks the user to input Make,Model and Year one by one.
- If the inputs are <strong style="color:green"> valid</strong>. The car is appended to the car database and exit back to main menu.
- If the inputs are <strong style="color:red"> invalid </strong>. Print error message and return back to main menu. 

 ```mermaid
graph TD
  A(["Main Menu"])
  B(["Option 3: Append to car database"])
  C(["Ask user for Make, Model, and Year"])
  D{"Are inputs valid?"}
  E["Append car to database"]
  F["Print success message"]
  G["Print error message"]
  H(["Return"])

  A --> B
  B --> C
  C --> D
  D -->|Yes| E
  D -->|No| G
  E --> F
  F --> H
  G --> H
  H --> A
```

### <strong style="color:#bc5090"> Feature 4: Estimate car price today based on depreciation and mileage. </strong>

From the Main menu, Option 4: Estimate used car price. <br><br>

This feature allows the user to find the estimated current market price for a vehicle. It asks the user to input Make,Model and Year one by one. 
- If <strong style="color:green"> valid</strong> inputs provided, return estimated vehicle price and go back to main menu.
- If <strong style="color:red"> invalid </strong>  inputs provided, return error message and go back to main menu.

```mermaid
graph TD
  A(["Main Menu"])
  B(["Option 3: Estimate used car price"])
  C(["Ask user for Make, Model, and Year"])
  D{"Are inputs valid?"}
  E["Return estimated vehicle price"]
  F["Print error message"]
  G(["Return"])

  A --> B
  B --> C
  C --> D
  D -->|Yes| E
  D -->|No| F
  E --> G
  F --> G
  G --> A
```
### <strong style="color: #bc5090"> Feature 5: Find all cars in database that meet budget and Make requirements. </strong>

From the Main menu, Option 5: Find cars by budget. <br><br>

This feature allows the user to search through the car datbase to find all cars that are within the specified budget and Make. It asks the user to input a price and optionally also a Make.
- If <strong style="color:green"> valid</strong> inputs are provided, return a list of vehciles that match criteria
- If <strong style="color:red"> invalid </strong>  inputs provided, return error message and go back to main menu.

```mermaid
graph TD
  A(["Main Menu"])
  B(["Option 5: Find cars by budget"])
  C(["Ask user for Price and optionally Make"])
  D{"Are inputs valid?"}
  E["Return list of vehicles that match criteria"]
  F["Print error message"]
  G(["Return"])

  A --> B
  B --> C
  C --> D
  D -->|Yes| E
  D -->|No| F
  E --> G
  F --> G
  G --> A

```

# <strong style="color:salmon"> Project Management </strong>

## Code Implementation plan 

<strong>Disclaimer -This section was initially written during the planning stage, before any code for the program was written. It has been actively updated as the project progressed. Therefore, there may be some differences between the initial plan and the final product. </strong>

### <strong style="color: #f59c42"> Main Program </strong>

#### File: (main.py) 

#### Pseudocode Outline:

1. Import and load all features from their respective modules.  
2. Create a main function that runs on a while loop.
3. Within the while loop, Display Main Menu Options
4. Prompt the user to choose an option.
   - Option 1: Upload car database.
   - Option 2: Search car database.
   - Option 3: Append to car database.
   - Option 4: Estimate used car price.
   - Option 5: Find cars within budget.
   - Option 6: Exit the application.
5. Based on choice, do the following.
   - Option 1: Upload File: Ask for file path 
     - If correct inputs provided, upload to local database and go back to main menu.
     - If incorrect inputs provided, display error message and go to main menu.
   - Option 2: Search Database: Ask for car details and search the database.
     - If correct inputs provided, return price of vehicle and go back to main menu.
     - If incorrect inputs provided, return error message and go back to main menu.
   - Option 3: Append Database: Ask for new car details 
     - If correct inputs provided, append car to database and go back to main menu.
     - If incorrect inputs provided, return error message and go back to main menu.
   - Option 4: Estimate Price: Ask for car details 
     - If correct inputs provided, return estimated vehicle price and go back to main menu.
     - If incorrect inputs provided, return error message and go back to main menu.
   - Option 5: Find Cars by Budget: Ask for budget and make (optional)
     - If correct inputs provided, find cars within that budget, return list of cars and go back to main menu.
     - If incorrect inputs provided, display error message and go back to main menu.
   - Option 6: Exit: Exit the application.
6. Handle Invalid Choices: Print an error message for invalid choices.


#### Pseudocode Logic:

```mermaid
graph TD
  A(["Start"])
  B(["Import and load all features from modules"])
  C(["Main function"])
  D(["Display Main Menu Options"])
  E(["Prompt user to choose an option"])
  F{"Option chosen"}
  G1["Option 1: Upload File"]
  G2["Option 2: Search Database"]
  G3["Option 3: Append Database"]
  G4["Option 4: Estimate Price"]
  G5["Option 5: Find Cars by Budget"]
  G6["Option 6: Exit"]
  H1["Ask for file path"]
  H2["Ask for car details"]
  H3["Ask for new car details"]
  H4["Ask for car details"]
  H5["Ask for budget and make (optional)"]
  I1{"Correct inputs?"}
  I2{"Correct inputs?"}
  I3{"Correct inputs?"}
  I4{"Correct inputs?"}
  I5{"Correct inputs?"}
  J1["Upload to local database"]
  J2["Return price of vehicle"]
  J3["Append car to database"]
  J4["Return estimated vehicle price"]
  J5["Find cars within budget"]
  J6["Exit the application"]
  K1["Display error message"]
  K2["Return error message"]
  K3["Return error message"]
  K4["Return error message"]
  K5["Display error message"]
  L(["Return to main menu"])
  M["Handle invalid choices"]
  N["Print error message for invalid choices"]
  O(["End"])

  A --> B
  B --> C
  C --> D
  D --> E
  E --> F
  F -->|1| G1
  F -->|2| G2
  F -->|3| G3
  F -->|4| G4
  F -->|5| G5
  F -->|6| G6
  F -->|Invalid| M

  G1 --> H1
  H1 --> I1
  I1 -->|Yes| J1
  I1 -->|No| K1
  J1 --> L
  K1 --> L

  G2 --> H2
  H2 --> I2
  I2 -->|Yes| J2
  I2 -->|No| K2
  J2 --> L
  K2 --> L

  G3 --> H3
  H3 --> I3
  I3 -->|Yes| J3
  I3 -->|No| K3
  J3 --> L
  K3 --> L

  G4 --> H4
  H4 --> I4
  I4 -->|Yes| J4
  I4 -->|No| K4
  J4 --> L
  K4 --> L

  G5 --> H5
  H5 --> I5
  I5 -->|Yes| J5
  I5 -->|No| K5
  J5 --> L
  K5 --> L

  G6 --> J6
  J6 --> O

  L -.-> D
  M --> N
  N --> L

```



### <strong style="color: #f59c42"> CSV data </strong>

#### File: (car_database.csv) 

#### Pseudocode Outline:

1. Create a simple CSV called car_database.
2. Add 4 headers to called "Make" "Model" "Year" "Price".
3. Populate the CSV with with random cars taken from the internet.
4. Place the CSV in a folder called data within the local repository and note the file path.


### <strong style="color: #f59c42"> Feature 1: Upload CSV file and store to local Dictionary  </strong>

#### File: (upload_file.py)

#### Pseudocode Outline: 

1.	Import CSV Module to handle CSV files.
2.	Create a blank dictionary to store vehicle data. Let’s call it car_database.
3.	Create a function called upload_file that take the argument of the file path where the csv is located.
4.	Using csv.DictReader open the csv file according to provided file path.
5.	Iterate through each row.
6.	Check if correct car details are present(make,model,year,price)
7.	If they are present add to dictonary car_database such that the key is a tuple of (make,model,year) and the value is the price.
8.	Save the information.
9.	Print a success message saying that the upload has been successful. 

#### Pseudocode Logic:

```mermaid
graph TD
  A([Start])
  B[Import CSV Module]
  C[Create blank dictionary: car_database]
  D[Define function with file path argument]
  E{Open CSV file}
  F[File opened successfully]
  G[File not found]
  H{Iterate through each row}
  I[Check if details are present]
  J{Details present?}
  K[Log error: fields missing]
  L[Add to car_database]
  M[Save the information]
  N[Print success message]
  O([End])

  A --> B
  B --> C
  C --> D
  D --> E
  E -->|Success| F
  E -->|Not Found| G
  F --> H
  H --> I
  I --> J
  J -->|No| K
  J -->|Yes| L
  L --> M
  M --> N
  G --> O
  K --> H
  N --> O

```

### <strong style="color: #f59c42"> Feature 2: Search through car database to find price of car when it was new  </strong>

#### File: (search_database.py)

#### Pseudocode Outline:

1.	Import the car_database dictionary base created in function 1.
2.	Create a function called search_database that takes the arguments of (Make,Model,Year). 
3.	Check that the inputs provided are valid.
4.	If valid, iterate throw each row in car_database
5.	Iterate until exact car is found.
6.	Return the price of the car.

#### Pseudocode Logic:

```mermaid
graph TD
  A([Start])
  B[Import car_database dictionary]
  C[Define function search_database with inputs Make, Model, Year]
  D[Check if inputs are valid]
  E{Inputs valid?}
  F[Iterate through car_database]
  G{Car found?}
  H[Return price of the car]
  I[Log error: Invalid inputs]
  J([End])

  A --> B
  B --> C
  C --> D
  D --> E
  E -->|Yes| F
  E -->|No| I
  F --> G
  G -->|Yes| H
  G -->|No| F
  H --> J
  I --> J
 ```
### <strong style="color: #f59c42"> Feature 3: Append Car Database </strong>

#### File: (append_database.py)

#### Pseudocode Outline:

1.	Import the car_database dictionary base created in function 1.
2.	Create a function called append_database that takes the arguments of (Make,Model,Year,Price). 
3.	Check that the inputs provided are valid.
4.	Add the car to the database where the key is a tuple of Make,Model,Year and the value is Price.
5.	Print success message

#### Pseudocode Logic:

```mermaid
graph TD
  A([Start])
  B[Import car_database dictionary]
  C[Define function append_database takes inputs Make, Model, Year, Price]
  D[Check if inputs are valid]
  E{Inputs valid?}
  F[Add car to database key: Make, Model, Year, value: Price]
  G[Print success message]
  H[Log error: Invalid inputs]
  I([End])

  A --> B
  B --> C
  C --> D
  D --> E
  E -->|Yes| F
  E -->|No| H
  F --> G
  G --> I
  H --> I
```
### <strong style="color: #f59c42"> Feature 4: Estimate car price today based on depreciation and mileage. </strong>

#### File: (estimate_price.py)

#### Pseudocode Outline:


1.	Import the search_database fuction created in feature 2
2.	Import datetime module.
3.	Import math module.
4.	Create a function called estimate_price that takes the arguments of (Make,Model,Year,Mileage). 
5.	Check that the inputs provided are valid.
6.	Use search_database to find car from inputs provided and store to variable called base price
7.	If car not found using search_database return “car not found”
8.	Calculate depreciation and milage adujustment
      a.	Set depreciation rate to 5% per year.
      b.	Set mileage adjustment factor to 0.01 per mile.
9.	Calculate age of car using datetime module
10.	Calculate current price of car based on formula price = base_price - (depreciation_rate * years_old * base_price) + (mileage_adjustment_factor * mileage)
11.	Return calculated price.

#### Pseudocode Logic:

```mermaid
graph TD
  A(["Start"])
  B(["Import search_database function"])
  C(["Import datetime module"])
  D(["Import math module"])
  E(["Define function estimate_price(Make, Model, Year, Mileage)"])
  F(["Check if inputs are valid"])
  G{"Inputs valid?"}
  H(["Use search_database to find car"])
  I{"Car found?"}
  J(["Return 'car not found'"])
  K(["Calculate depreciation and mileage adjustment"])
  L(["Set depreciation rate to 5% per year"])
  M(["Set mileage adjustment factor to 0.01 per mile"])
  N(["Calculate age of car using datetime module"])
  O(["Calculate current price"])
  P(["Return calculated price"])
  Q(["End"])

  A --> B
  B --> C
  C --> D
  D --> E
  E --> F
  F --> G
  G -->|Yes| H
  G -->|No| Q
  H --> I
  I -->|No| J
  I -->|Yes| K
  K --> L
  K --> M
  L --> N
  M --> N
  N --> O
  O --> P
  P --> Q
  J --> Q
```
### <strong style="color: #f59c42"> Feature 5: Find all cars in database that meet budget and Make requirements  </strong>

#### File: (find_cars_by_budget.py)

#### Pseudocode Outline:

1.	Import the car_database dictionary base created in feature 1.
2.	Create a function called find_cars_by_budget that takes the arguments of (Price,Make). Or Make = none
3.	Check that the inputs provided are valid. 
4.	Create empty list to store cars found.
5.	Iterate through car_database to find cars that satisfy:
    - 	Price < budget
    - Make matches Make (Optional)
6.	Car found within those criteria returned to list.


#### Pseudocode Logic:

```mermaid
graph TD
  A(["Start"])
  B(["Import car_database dictionary"])
  C(["Define function find_cars_by_budget(Price, Make=None)"])
  D(["Check if inputs are valid"])
  E{"Inputs valid?"}
  F(["Create empty list to store cars found"])
  G(["Iterate through car_database"])
  H{"Price < budget?"}
  I{"Make matches?"}
  J(["Add car to list"])
  K(["Continue to next car"])
  L(["Return list of cars found"])
  M(["End"])

  A --> B
  B --> C
  C --> D
  D --> E
  E -->|Yes| F
  E -->|No| M
  F --> G
  G --> H
  H -->|Yes| I
  H -->|No| K
  I -->|Yes| J
  I -->|No| K
  J --> K
  K --> G
  G -->|End of database| L
  L --> M
```
## Testing and Patching

### <strong style="color: #f59c42"> Feature 1: Upload CSV file and store to local Dictionary  </strong>


**Test 1: Invalid File Path**
  - **Action:** Provide an incorrect file path.
  - **Expected Result:** Error message indicating the file was not found.
  - **Actual Result:** Error message returned.
  - **Status:** OK

**Test 2: CSV with Missing Header**
  - **Action:** Provide a CSV file missing one or more required headers (Make, Model, Year, Price).
  - **Expected Result:** Error message indicating missing header but uploads.
  - **Actual Result:** Error message returned but still uploaded. Message and detection not satisfactory.
  - **Status:** Patched. Code added to detect mandatory headers. See commit aa8a2b32. -m "Testing and Patching of Feature 1:Done"

**Test 3: CSV with Missing Value**
  - **Action:** Provide a CSV file where some rows have missing values for Make, Model, Year, or Price.
  - **Expected Result:** Error message indicating missing value.
  - **Actual Result:** Error message returned.
  - **Status:** OK

**Test 4: CSV with Incorrect Value for Specific Car**
  - **Action:** Provide a CSV file with an incorrect value format for a specific car (e.g., non-numeric price).
  - **Expected Result:** File should still upload, but user notified of the specific row error.
  - **Actual Result:** File uploaded, user notified of the error.

**Test 5: CSV with Duplicate Entries**
  - **Action:** Provide a CSV file with duplicate car entries.
  - **Expected Result:** File should still upload, but user notified of the specific row error.
  - **Actual Result:** Did not pick up on duplicates.
  - **Status:** Patched with new code inserted. See commit aa8a2b32. -m "Testing and Patching of Feature 1:Done"

### <strong style="color: #f59c42"> Feature 2: Search through car database to find price of car when it was new  </strong>

**Test 1: Invalid Make Type**
   - **Action:** Provide Make such that not all characters are alphabet letters.
   - **Expected Result:** Returns "Make should be string" error message.
   - **Actual Result:** Incorrect result. Need modification to main function.
   - **Status:** Patched. Main function needed some changes. See commit:

**Test 2: Invalid Year Type**
   - **Action:** Provide a non-integer value for Year.
   - **Expected Result:** Returns "TypeError: Year should be an integer."
   - **Actual Result:** Error message thrown. However, it is different from the expected message.
   - **Status:** Keep it as it is for now.

**Test 3: Empty Car Database**
   - **Action:** Search for a car when the car_database is empty.
   - **Expected Result:** Returns "Car not found in the database."
   - **Actual Result:** Returns as expected.
   - **Status:** OK

**Test 4: Case Sensitivity in Make and Model**
   - **Action:** Search for a car with different case (e.g., make instead of Make).
   - **Expected Result:** Case sensitivity may cause "Car not found in the database."
   - **Actual Result:** Returns as expected.
   - **Status:** OK

### <strong style="color: #f59c42"> Feature 3: Append Car Database </strong>

**Test 1: Valid Inputs Without File Path**
- **Action:** Append a valid car entry without running Option 1 first.
- **Expected Result:** Error message asking the user to run option 1 first.
- **Actual Result:** Error message as expected.
- **Status:** OK

**Test 2: Invalid Make Type**
- **Action:** Provide Make such that not all characters are alphabet letters.
- **Expected Result:** Returns "Make should be string" error message.
- **Actual Result:** Incorrect result. Need modification to main function.
- **Status:** Patched. Main function needed some changes. See commit: 69a4dd6 -m "Testing and Patching of Feature 3:Done for now"

**Test 3: Invalid Year Type**
- **Action:** Provide a non-integer value for Year.
- **Expected Result:** Returns "Error: Year must be an integer and Price must be a number."
- **Actual Result:** Error message as expected.
- **Status:** OK

**Test 4: Invalid Year Type**
- **Action:** Provide a non-integer value for Price.
- **Expected Result:** Returns "Error: Year must be an integer and Price must be a number."
- **Actual Result:** Error message as expected.
- **Status:** OK

### <strong style="color: #f59c42"> Feature 4: Estimate car price today based on depreciation and mileage. </strong>

**Test 1: Invalid Make Type**
- **Action:** Provide Make such that not all characters are alphabet letters.
- **Expected Result:** Returns "Make should be string" error message.
- **Actual Result:** Incorrect result. Need modification to main function.
- **Status:** Patched. Main function needed some changes. See commit: 56220b5 m- "Testing and Patching of Feature 4:Done for now"

**Test 2: Enter Very High Mileage**
- **Action:** Provide so high mileage such that car value becomes negative.
- **Expected Result:** Message showing that car has no value.
- **Actual Result:** Incorrect result. Need modification to estimate_price function to add new message letting user know car has no value.
- **Status:** Patched. Estimate_price function needed some changes. See commit: 56220b5 m- "Testing and Patching of Feature 4:Done for now"

**Test 3: Invalid Year Type**
- **Action:** Provide a non-integer value for Year.
- **Expected Result:** Returns "Error: Year must be an integer and Price must be a number."
- **Actual Result:** Error message as expected.
- **Status:** OK

**Test 4: Invalid Mileage Type**
- **Action:** Provide a non-numeric value for mileage.
- **Expected Result:** Raises TypeError with the message "Mileage should be a number."
- **Actual Result:** Error message as expected.
- **Status:** OK

### <strong style="color: #f59c42"> Feature 5: Find all cars in database that meet budget and Make requirements  </strong>

**Test 1: Invalid Make Type**
- **Action:** Provide Make such that not all characters are alphabet letters.
- **Expected Result:** Returns "Make should be string" error message.
- **Actual Result:** Incorrect result. Need modification to main function.
- **Status:** Patched. Main function needed some changes. See commit:

**Test 2: Enter Very Low Budget**
- **Action:** Enter so low budget that there are no cars available.
- **Expected Result:** Message showing no cars found.
- **Actual Result:** Incorrect result. Need modification to find_cars_by_budget function to add new message letting user know that there are no cars that match their criteria.
- **Status:** Patched. find_cars_by_budget function needed some changes. See commit:

**Test 3: Enter Make Not in Database**
- **Action:** Enter a make that isn’t in the database.
- **Expected Result:** Message showing Make not found in database.
- **Actual Result:** Incorrect result. Need modification to find_cars_by_budget function to add new message letting user know that make not found.
- **Status:** Patched. find_cars_by_budget function needed some changes. See commit:

## Project Tracking

### Platform

For my project, I decided to use the agile based project mangement software JIRA. It is a popular project management tool that is widely used in software development due to its robust data tracking and agile project management capabilities. 

### Methodology

Sprint Duration: 7 days


### Tickets

Epics:
2 Epics: 
- Application Coding
- Documentation & Research 


| Story name                                   | Story points | Subtask name                                | Epic                       | Original Estimate (days) | Priority    |
|----------------------------------------------|--------------|---------------------------------------------|----------------------------|--------------------------|-------------|
| Set Up Basic Infrastructure (CAP-33)         | 3            | Initialize Project Repository (TAP-21)      | Application Coding         | 0.5                      | Medium      |
|                                              |              | Create Folders and Structure (TAP-22)       | Application Coding         | 0.5                      | Medium      |
|                                              |              | Create Car Dictionary Structure (TAP-26)    | Application Coding         | 0.5                      | Medium      |
|                                              |              | Create Main.py file (TAP-27)                | Application Coding         | 0.5                      | Medium      |
|                                              |              | Create empty files for each feature (TAP-28)| Application Coding         | 0.5                      | Medium      |
| Set Up Documentation Structure (CAP-32)      | 2            | Create Readme file and add headers and sections (TAP-31)| Documentation & Research   | 0.5                      | Low         |
|                                              |              | Create Requirements.txt (TAP-32)            | Documentation & Research   | 0.5                      | Low         |
| Feature 1: Implement File Upload Functionality (CAP-34)| 5 | Implement Function to Read CSV File (TAP-12)| Application Coding         | 1                        | Highest     |
|                                              |              | Populate Car Dictionary (TAP-13)            | Application Coding         | 0.5                      | Highest     |
|                                              |              | Handle File Reading Errors 1 (TAP-14)       | Application Coding         | 0.5                      | Highest     |
| Feature 1: Documentation (CAP-35)            | 2            | Write Pseudocode 1 (TAP-39)                 | Documentation & Research   | 0.5                      | Medium      |
|                                              |              | Update Documents 1 (TAP-40)                 | Documentation & Research   | 0.5                      | Medium      |
| Feature 2: Implement Search and Append Functionality (CAP-36)| 5 | Implement Search Function (TAP-24)          | Application Coding         | 1                        | Highest     |
|                                              |              | Implement Append Function (TAP-25)          | Application Coding         | 0.5                      | Highest     |
| Feature 2: Documentation (CAP-37)            | 2            | Write Pseudocode 2 (TAP-41)                 | Documentation & Research   | 0.5                      | Medium      |
|                                              |              | Update Documents 2 (TAP-42)                 | Documentation & Research   | 0.5                      | Medium      |
| Feature 3: Implement Used Car Price Estimation (CAP-38)| 5 | Collect User Input for Car Details (TAP-10) | Application Coding         | 0.5                      | Highest     |
|                                              |              | Implement Price Estimation Formula (TAP-11) | Application Coding         | 1                        | Highest     |
| Feature 3: Documentation (CAP-39)            | 2            | Write Pseudocode 3 (TAP-37)                 | Documentation & Research   | 0.5                      | Medium      |
|                                              |              | Update Documents 3 (TAP-43)                 | Documentation & Research   | 0.5                      | Medium      |
| Feature 4: Implement Car Finder Based on Budget (CAP-40) | 5 | Collect User Input for Budget (TAP-15)      | Application Coding         | 0.5                      | Highest     |
|                                              |              | Implement Budget-Based Car Finder Function (TAP-16) | Application Coding         | 1                        | Highest     |
| Feature 4: Documentation (CAP-41)            | 2            |                                             | Documentation & Research   | 0.5                      | Medium      |
| Integration and Testing 1 (CAP-42)           | 8            |                                             | Application Coding         | 2                        | Medium      |
| Additional Changes and Features (CAP-43)     | 8            |                                             | Application Coding         | 2                        | Medium      |
| Integration and Testing 2 (CAP-44)           | 8            |                                             | Application Coding         | 2                        | Medium      |
| Finalize Documentation (CAP-45)              | 3            |                                             | Documentation & Research   | 1                        | Low         |
| Final Review and Deployment (CAP-46)         | 8            |                                             | Application Coding         | 2                        | Medium      |
| Placeholder 1 (CAP-47)                       | 1            |                                             | Application Coding         | 0.5                      | Low         |
| Placeholder 2 (CAP-48)                       | 1            |                                             | Application Coding         | 0.5                      | Low         |
| Placeholder 3 (CAP-49)                       | 1            |                                             | Application Coding         | 0.5                      | Low         |


### Sprint progression
#### <strong style="color:#bc5090"> Day 1 </strong>

##### Day Brief:
##### Sprint Board at End of Day:
##### Burnup chart:

#### <strong style="color:#bc5090"> Day 2 </strong>

##### Day Brief:
##### Sprint Board at End of Day:
##### Burnup chart:

#### <strong style="color:#bc5090"> Day 3 </strong>

##### Day Brief:
##### Sprint Board at End of Day:
##### Burnup chart:

#### <strong style="color:#bc5090"> Day 4 </strong>

##### Day Brief:
##### Sprint Board at End of Day:
##### Burnup chart:

#### <strong style="color:#bc5090"> Day 5 </strong>

##### Day Brief:
##### Sprint Board at End of Day:
##### Burnup chart:

#### <strong style="color:#bc5090"> Day 6 </strong>

##### Day Brief:
##### Sprint Board at End of Day:
##### Burnup chart:

#### <strong style="color:#bc5090"> Day 7 </strong>

##### Day Brief:
##### Sprint Board at End of Day:
##### Burnup chart: