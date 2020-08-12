import csv
# this code reading the records into dictionary.. key names are first row in the file
''' We're working with a list of flowers and some information about each one. 
The create_file function writes this information to a CSV file. 
The contents_of_file function reads this file into records and returns the information in a nicely formatted block. 
Fill in the gaps of the contents_of_file function to turn the data in the CSV file into a dictionary using DictReader.
'''
with open('employee_birthday1.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    print(f'type of csv_reader is {type(csv_reader)}')
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
            print(row.items())

        print(row.items())
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')