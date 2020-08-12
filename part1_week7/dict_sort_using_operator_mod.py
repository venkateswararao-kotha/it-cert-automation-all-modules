import operator

fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
# Call the sorted function to sort the items in the dictionary
print("Call the sorted function to sort the items in the dictionary")
print(sorted(fruit.items()))
print()
# We'll now sort the dictionary using the item's key. For this use the operator module.
print("Sorting fruits dictionary using Keys, operator module")
print(sorted(fruit.items(), key=operator.itemgetter(0)))

# To sort a dictionary based on its values, pass the argument 1 to the itemgetter function of the operator module.
print()
print("Sorting fruits dictionary using values, operator module")
print(sorted(fruit.items(), key=operator.itemgetter(1)))
