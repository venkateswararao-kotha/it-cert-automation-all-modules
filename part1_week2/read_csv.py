import csv

with open('eggs.csv') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        a,b,c,d = row  # unpack list into variables
        #print(a, b, c, d)
        print('|'.join(row))