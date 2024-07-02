# This file is to to used for misc testing purpose. Delete at the end before submitting.


def search_database(): 
    #Import
    from upload_file import upload_file

    car_database=upload_file.car_database

    for keys,values in car_database:
        print(keys)
    print(values)