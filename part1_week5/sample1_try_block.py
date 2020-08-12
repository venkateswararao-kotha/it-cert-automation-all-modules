import sys
# below is the sampe code to convert the string to integer in myfile.txt
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
    print(f'i value is {i}')
except IOError as e:  # This will execute if myfile.txt is not existed
    print("I/O error({0}): {1}".format(e.errno, e.strerror))
except ValueError:  # This will execute if the value in file is not a integer
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

# below is example block for raising ValueError ex exception
try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)