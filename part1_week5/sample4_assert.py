'''
my_word_list = ['east', 'after', 'up', 'over', 'inside']

def OrganizeList(myList):
    myList.sort()
    return myList

print(OrganizeList(my_word_list))

We used the OrganizeList() function to sort a given list alphabetically. The function seems to be working fine.
However, there is a problem when we try to call the function on a list containing number values.
Run the following cell to see what happens.

my_new_list = [6, 3, 8, '12', 42]
print(OrganizeList(my_new_list))

From the above output we see that our function now raises a TypeError. This is because
the OrganizeList() function makes sense for lists that are filled with only strings.
Take control of the error messaging here and pre-empt this error by filling in the blanks
below to add an assert type argument that verifies whether the input list is filled with only strings.
You can have the error message say something like "Word list must be a list of strings".

'''
def OrganizeList(myList):
    for item in myList:
        assert isinstance(item, str), "Word list must be a list of strings*"

    myList.sort()
    return myList

my_new_list = [6, 3, 8, '12', 42]
print(OrganizeList(my_new_list))