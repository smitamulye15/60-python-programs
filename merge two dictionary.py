# Python Program to Concatenate Two Dictionaries

first_Dict = {'a': 'apple', 'b': 'Banana' , 'o': 'Orange'}
second_Dict = { 'k': 'Kiwi', 'm': 'Mango'}
print("First Dictionary: ", first_Dict)
print("Second Dictionary: ", second_Dict)

# Concatenate Two Dictionaries in Python
print("\nAfter Concatenating two Dictionaries : ")
print(dict(first_Dict, **second_Dict) )