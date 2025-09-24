import csv
import json

csv_file_path = 'samplecsvfile.csv'
json_file_path = 'samplejsonfile.json'

# reads the csv file
with open(csv_file_path, mode='r') as csv_file:

    #creates the csv into a object
    csv_data_object = csv.reader(csv_file)
    
    # creates a list of each row as an array from the csv
    list_data = list(csv_data_object)

    # get the header seperately
    headers = list_data[0]

    dict_list = []

    # go through each row after the header
    for row in list_data[1:]:
        #create a dictionary for each row with the header as the keys and data information as the values
        row_dict = dict(zip(headers, row))
        dict_list.append(row_dict)


with open(json_file_path, mode='w') as json_file:
    json.dump(dict_list, json_file, indent=3)
