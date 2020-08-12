import os
import csv

'''
Using the CSV file of flowers again, fill in the gaps of the contents_of_file function to 
process the data without turning it into a dictionary. How do you skip over the header 
record with the field names?
'''
# Create a file with data in it
def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
    return_string = ""
    line_count = 0
    # Call the function to create the file
    create_file(filename)

    # Open the file
    with open(filename) as file_nm:
        # Read the rows of the file
        records = csv.reader(file_nm)
        header = next(records)
        # Process each row
        for row in records:
            # if line_count == 0:
            #    return_string += "a {0} {1} is {2}\n".format(row[0],row[1],row[2])
            # if line_count > 0:
            # Format the return string for data rows only
            return_string += "a {b} {a} is {c}\n".format(a=row[0], b=row[1], c=row[2])
            # line_count += line_count
    return return_string


# Call the function
# contents_of_file("flowers123.csv")
print(contents_of_file("flowers123.csv"))
