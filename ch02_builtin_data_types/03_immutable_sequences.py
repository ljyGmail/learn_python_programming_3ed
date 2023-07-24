#####################
# Immutable sequences
#####################

#####################
## Strings and bytes
#####################
# 4 ways to make a string
str1 = 'This is a string. We built it with single quotes.'
print(f'str1: {str1}')
str2 = "This is also a string, but built with double quotes."
print(f'str2: {str2}')
str3 = '''This is built using triple quotes,
so it can span multiple lines.'''
print(f'str3: {str3}')
str4 = """This too
is a multiline one
built with triple double-quotes."""
print(f'str4: {str4}')

print(f'len(str1): {len(str1)}')

s = 'Hello There'
print(f"s.removeprefix('Hell'): {s.removeprefix('Hell')}")
print(f"s.removesuffix('here'): {s.removesuffix('here')}")
print(f"s.removeprefix('Ooops'): {s.removeprefix('Ooops')}")

#################################
### Encoding and decoding strings
#################################
s = "This is üŋíc0de" # unicode string: code points
print(f'type(s): {type(s)}')
encoded_s = s.encode('utf-8') # utf-8 encoded version of s
print(f'encoded_s: {encoded_s}') # result: bytes object
print(f'type(encoded_s): {type(encoded_s)}') # another way to verify it
print(f"encoded_s.decode('utf-8'): {encoded_s.decode('utf-8')}") # let's revert to the original
bytes_obj = b"A bytes object" # a bytes object
print(f'type(bytes_obj): {type(bytes_obj)}')

#################################
### Indexing and slicing strings
#################################
s = "The trouble is you think you have time."
print(f's[0]: {s[0]}') # indexing at position 0, which is the first char
print(f's[5]: {s[5]}') # indexing at position 5, which is the sixth char
print(f's[:4]: {s[:4]}') # slicing, we specify only the stop position
print(f's[4:]: {s[4:]}') # slicing, we specify only the start position
print(f's[2:14]: {s[2:14]}') # slicing, both start and stop positions
print(f's[2:14:3]: {s[2:14:3]}') # slicing, both start and stop positions
print(f's[:]: {s[:]}') # quick way of making a copy

#################################
### String formatting
#################################
greet_old = 'Hello %s!'
print(f"greet_old % 'Fabrizio': {greet_old % 'Fabrizio'}")
greet_positional = 'Hello {}!'
print(f"greet_positional.format('Fabrizio'): {greet_positional.format('Fabrizio')}")
greet_positional = 'Hello {} {}!'
print(f"greet_positional.format('Fabrizio', 'Romano): {greet_positional.format('Fabrizio', 'Romano')}")
greet_positional_idx = 'This is {0}! {1} loves {0}!'
print(f"greet_positional_idx.format('Python', 'Heinrich'): {greet_positional_idx.format('Python', 'Heinrich')}")
print(f"greet_positional_idx.format('Coffee', 'Fab'): {greet_positional_idx.format('Coffee', 'Fab')}")
keyword = 'Hello, my name is {name} {last_name}'
print(f"keyword.format(name='Fabrizio', last_name='Romano'): {keyword.format(name='Fabrizio', last_name='Romano')}")

name = 'Fab'
age = 42
print(f"Hello! My name is {name} and I'm {age}")

from math import pi
print(f"No arguing with {pi}, it's irrational...")

user = 'heinrich'
password = 'super-secret'
print(f"Log in with: {user} and {password}")
print(f"Log in with: {user=} and {password=}")

#####################
## Tuples
#####################
t = () # empty tuple
print(f'type(t): {type(t)}')
one_element_tuple = (42, ) # comma is required!
three_elements_tuple = (1, 3, 5) # braces are optional here
a, b, c = 1, 2, 3 # tuple for multiple assignment
print((a, b, c)) # implicit tuple to print with one instruction
print(f'3 in three_elements_tuple: {3 in three_elements_tuple}')

# one-line swaps
a, b = 1, 2
c = a # we need three lines and a temporary var c
a = b
b = c
print(f'a, b: {a, b}')
# Now let's see how we would do it in Python:
a, b = 0, 1
a, b = b, a
print(f'a, b: {a, b}')