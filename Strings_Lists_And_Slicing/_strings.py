# Working with Strings or Textaul Data

# All Variables should in Lower Case. If there are more than one word in the Variable,
# then we separate with under scores. And this is PYTHON CONVENTION
# =================================================================
my_message = 'Hello World'
print(my_message)

# We can use both single and Double Quotes for the Strings.
# If you hava single Quotes in the actual String, we can represent the original String in Double Quotes.
# If the String actual String contains Double Quotes, we can use single Quotes to represent the String.

message = "Welcome to Python's world"
print(message)

message = 'Welcome to Pythons"s world'
print(message)

# We can use Escape Charater as well
message = 'Welcome to Python\'s world'
print(message)

message = "Welcome to Python\"s world"
print(message)

# We can use either double backslash or prefix 'r' which stands for raw string or regular expression
print("C:\\testing\\newfolder")
print(r"C:\testing\newfolder")

# use Triple Quotes to represent a Multi-Line String
multi_line_string = '''Hello There..
Welcome to Python tutorials'''
print(multi_line_string)

multi_line_string = """Hello There..
Welcome to Python tutorials"""
print(multi_line_string)

# =========================================================
my_message = 'Hello World'

# String Functions
print(len(my_message))      # Prints the Length of the String. Index starts from Zero
print(my_message.upper())   # Prints the String in Upper Case
print(my_message.lower())   # Prints the String in Lower Case
print(my_message.count('l'))    # Prints number of occurances of the letter 'l'
print(my_message.count('Hello'))    # Prints number of occurances of the word 'Hello'
print(my_message.find('l'))     # Prints the index of first occurance of the letter 'l'
print(my_message.find('World'))     # Prints the index of first occurance of the word 'World'
print(my_message.find('Universe'))      # Prints -1.
print(my_message.replace('World', 'Universe'))  # Prints 'Hello Universe'

# String Concatination
greeting = 'Hello'
name = 'Steve'
print(greeting, name)

print('Python '+str(2019))      # 2019 should be convered to String if using + operator
print('Python' + ' 2019')
print('Python', 2019)       # Comma is used for concatinating two string of different datatypes

# '+' is used for concatinating two objects of same datatype
print(greeting+', '+name)

# Repeats the string 5 times
print('Hello ' * 5)
