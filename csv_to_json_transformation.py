import csv
import json

csv_file_path = 'samplecsvfile.csv'
csv_file_path2 = 'samplecsvfile2.csv'

csv_list = [
            csv_file_path, 
            csv_file_path2
            ]  

# you can add more csv file paths to this list 

for csv_file in csv_list:
    try:
        # reads the csv file
        with open(csv_file, mode='r') as file:
            # creates the csv reader object
            csv_data_object = csv.reader(file)
        
            # creates a list of each row as an array from the csv
            list_data = list(csv_data_object)

        # check if the file has data
        if not list_data:
            print(f"Warning: {csv_file} is empty")
            continue

        # get the header separately
        headers = list_data[0]

        dict_list = []
        # go through each row after the header
        for row in list_data[1:]:
            # create a dictionary for each row with the header as the keys and data information as the values
            row_dict = dict(zip(headers, row))
            dict_list.append(row_dict)

        # create a JSON filename based on the CSV filename
        json_file_path = csv_file.replace('.csv', '.json')
        
        # writes json file with the list of dictionaries
        with open(json_file_path, mode='w') as json_file:
            json.dump(dict_list, json_file, indent=3)
        
        print(f"Successfully converted {csv_file} to {json_file_path}")
            
    except FileNotFoundError:
        print(f"Error: File {csv_file} not found")
    except Exception as e:
        print(f"Error processing {csv_file}: {str(e)}")
