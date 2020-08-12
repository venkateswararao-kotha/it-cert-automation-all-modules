import csv

with open('sample_write_output.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

# below John Smith will be quoted with " because quotechar is defined above as "
    employee_writer.writerow(['John, Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])