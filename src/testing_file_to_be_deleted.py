# This file is to to used for misc testing purpose. Delete at the end before submitting.


# def search_database(): 
#     #Import
#     from upload_file import car_database,upload_file

#     car_database=upload_file.car_database

#     for keys,values in car_database:
#         print(keys)
#     print(values)
    
def search_database():
    from upload_file import car_database  # Import the global car_database variable

    for keys, values in car_database.items():
        print(keys)
        print(values)
