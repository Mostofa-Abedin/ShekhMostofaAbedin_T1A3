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

# <strong style="color:salmon"> Project Management </strong>

## Implementation plan 

### <strong style="color: #f59c42"> Main Program (main.py) </strong>
#### Outline:
#### Logic: 
### <strong style="color: #f59c42"> CSV data (car_database.csv) </strong>
#### Outline:
#### Logic: 
### <strong style="color: #f59c42"> Feature 1: (upload_file.py) </strong>

#### Outline: 

1.	Import CSV Module to handle CSV files.
2.	Create a blank dictionary to store vehicle data. Let’s call it car_database
3.	Create a function called that take the argument of the file path where the csv is located.
4.	Using csv.DictReader open the csv file according to provided file path.
5.	Iterate through each row.
6.	Check if correct car details are present(make,model,year,price)
7.	If they are present add to dictonary car_database such that the key is a tuple of (make,model,year) and the value is the price.
8.	Save the information.
9.	Print a success message saying that the upload has been successful. 

#### Logic:

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

### <strong style="color: #f59c42"> Feature 2: (search_database.py) </strong>
#### Outline:
#### Logic:
### <strong style="color: #f59c42"> Feature 3: (append_database.py) </strong>
#### Outline:
#### Logic:
### <strong style="color: #f59c42"> Feature 4: (estimate_price.py) </strong>
#### Outline:
#### Logic:
### <strong style="color: #f59c42"> Feature 5: (find_cars_by_budget.py) </strong>


## Project Management Software

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

