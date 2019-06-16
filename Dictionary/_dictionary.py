# PYTHON DICTIONARIES

# Creating an empty Dictionary
employee = {}
employee = dict()   # Using Constructor

# Adding elements to an empty dictionary
employee['name'] = 'steve'
employee['salary'] = 60000

print(employee)

employee = {'name': 'steve', 'salary': 60000, 'languages': ['java', 'python']}

print(len(employee))    # Prints the length of the dictionary

# Accessing elements of a dictionary
print(employee['name'])
print(employee['languages'])
print(employee.get('salary'))

# Accessing a key that does not exist
# print(employee['age'])      # Throws exception KeyError: 'age'
print(employee.get('age'))      # get() method Does not throw an exception, but returns 'None'
print(employee.get('age', 'The Key not found in the dictionary'))   # Throws exception KeyError: 'age'

# Adding / Updating the dictionary
employee.update({'age': 35, 'phone': '111-1111'})
employee = {**employee, 'address': '2200, Valley View Lane'}

# Deleting the key and value
employee.popitem()      # Returns and deletes the last key/value pair in the dictionary
print(employee.pop('age'))    # Returns and Deletes the mentioned key from the dictionary
# del employee['age']     # Deletes the Key 'age' and its value

# Looping through Key's and Value's of the Dictionary
employee = {'name': 'steve', 'salary': 60000, 'languages': ['java', 'python']}

print(employee.items())     # Returns a tuple of key,value pairs

for item in employee:      # Prints only key's of the dictionary
    print(item)
    
for item in employee:
    print(employee[item])   # Prints Values of the dictionary

for key, value in employee.items():     # Tuple un-packing
    print(key, value)

for key in employee.keys():
    print(key)

for value in employee.values():
    print(value)

for index, items in enumerate(employee.items()):
    print(index, items)

# Merging Dictionaries
d1 = {'fname': 'steve', 'lname': 'jobs'}
d2 = {'age': 56, 'company': 'apple'}

d3 = {**d1, **d2}

# Creating Dictionary using List's
cities = ['Tokyo',
          'Delhi',
          'Shanghai',
          'Sao Paulo',
          'Mumbai'
          ]

population = ['38,001,000',
              '25,703,168',
              '23,740,778',
              '21,066,245',
              '21,042,538'
              ]

dict_city_pairs = dict(zip(cities, population))

print(dict_city_pairs)    # Prints dictionary of city and population pairs
# {'Tokyo': '38,001,000', 'Delhi': '25,703,168', 'Shanghai': '23,740,778',
# 'Sao Paulo': '21,066,245', 'Mumbai': '21,042,538'}

# Print max and min values in dict_city_pairs
print(max(dict_city_pairs))
print(min(dict_city_pairs))

# Prints {'Bangalore': 26, 'Delhi': 35, 'Chennai': 37, 'Kolkata': 32}
temperatures = [('Bangalore', 26), ('Delhi', 35), ('Chennai', 37), ('Kolkata', 32)]
dict_temp = dict(temperatures)
print(dict_temp)

# Prints default value zero if the key is not found in the dictionary
print(dict_city_pairs.get('Bangalore', 0))

# Print max and min temperatures in dict_temp
print(max(dict_temp))
print(min(dict_temp))

# Count number of words in a sentence
sentence = '''
Python is an interpreted, high-level, general-purpose programming language.
Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability,
notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales.
Van Rossum led the language community until stepping down as leader in July 2018.
'''
words = sentence.split()

words_count = {}

for word in words:
    word_count = words.count(word)
    words_count.update({word: word_count})

print(words_count)


# Finding Commonalities in Two Dictionaries
a = {'x': 1, 'y': 2, 'z': 3}

b = {'w': 10, 'x': 11, 'y': 2}

# Find keys in common
print(a.keys() & b.keys())     # Prints { 'x', 'y' }


# Find keys in a that are not in b
print(a.keys() - b.keys())  # prints { 'z' }

# Find (key,value) pairs in common
print(a.items() & b.items())   # prints { ('y', 2) }


# Make a new dictionary with certain keys removed
c = {key: a[key] for key in a.keys() - {'z', 'w'}} # prints c is {'x': 1, 'y': 2}

# The values() method of a dictionary does not support the set opearations described
# in above example. this is due to the fact that unlike keys, the items
# contained in a values view aren’t guaranteed to be unique


# However, if you must perform such calculations, they
# can be accomplished by simply converting the values to a set first.


print([value for value in set(a.values()) - {1}])   # Prints [2, 3]

