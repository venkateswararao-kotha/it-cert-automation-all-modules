my_number = raw_input('Please Enter a Number: \n')
Please Enter a Number: 
1337
print(my_number)
1337



# In Python 2 input(x) is just eval(raw_input(x)). eval() will just evaluate a generic string as if it were a Python expression.

my_raw_input = raw_input('Please Enter a Number: \n')
Please Enter a Number: 
123 + 1  # This is treated like a raw string.
my_input = input('Please Enter a Number: \n')
Please Enter a Number: 
123 + 1 # This is treated like an expression.
print(my_raw_input)
123 + 1
print(my_input)
124 # See that the expression was evaluated!


# In Python 3
# raw_input doesn’t natively exist in Python 3
# Taking an input from a user, input should be used. See the below sample:
my_number = input('Please Enter a Number: \n')
Please Enter a Number:
123 + 1
print(my_number)
123 + 1
type(my_number)
<class 'str'>

'''
Notice that the expression is treated just like a string. It is not evaluated. 
If we want to, we can call eval() and that will actually execute the string as an expression:
'''
Please Enter a Number: 
123 + 1
>>> print(my_number)
123 + 1
>>> eval(my_number)
124


