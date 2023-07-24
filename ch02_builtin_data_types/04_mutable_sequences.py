#####################
# Mutable sequences
#####################

#####################
# Lists
#####################
print(f'[]: {[]}') # empty list
print(f'list(): {list()}') # empty list
print(f'[1, 2, 3]: {[1, 2, 3]}') # as with tuples, items are comma separated
print(f'[x + 5 for x in [2, 3, 4]]: {[x + 5 for x in [2, 3, 4]]}') # Python is magic
print(f'list((1, 3, 5, 7, 9)): {list((1, 3, 5, 7, 9))}') # list from a tuple
print(f"list('hello'): {list('hello')}") # list from a string

# use lists
a = [1, 2, 3]
a.append(13) # we can append anything at the end
print(f'a: {a}')
print(f'a.count(1): {a.count(1)}') # how many `1s` are there in the list?
a.extend([5, 7]) # extend the list by another (or sequence)
print(f'a: {a}')
print(f'a.index(13): {a.index(13)}') # position of `13` in the list (0-based indexing)
a.insert(0, 17)
print(f'a: {a}')
print(f'a.pop(): {a.pop()}') # pop (remove and return) last element
print(f'a.pop(3): {a.pop(3)}') # pop element at position 3
print(f'a: {a}')
a.remove(17) # remove `17` from the list
print(f'a: {a}')
a.reverse() # reverse the order of the elements in the list
print(f'a: {a}')
a.sort() # sort the list
print(f'a: {a}')
a.clear() # remove all elements from the list
print(f'a: {a}')

# extend() method
a = list('hello') # makes a list from a string
print(f'a: {a}')
a.append(100) #append 100, heterogeneous type
print(f'a: {a}')
a.extend((1, 2, 3)) # extend using tuple
print(f'a: {a}')
a.extend('...') # extend using string
print(f'a: {a}')

# the most operations
a = [1, 3, 5, 7]
print(f'min(a): {min(a)}')
print(f'max(a): {max(a)}')
print(f'sum(a): {sum(a)}')

from math import prod
print(f'prod(a): {prod(a)}')
print(f'len(a): {len(a)}')

b = [6, 7, 8]
print(f'a + b: {a + b}') # `+` with list means concatenation
print(f'a * 2: {a * 2}') # `*` has also a special meaning

# sorted method
from operator import itemgetter
a = [(5, 3), (1, 3), (1, 2), (2, -1), (4, 9)]
print(f'sorted(a): {sorted(a)}')
print(f'sorted(a, key=itemgetter(0)): {sorted(a, key=itemgetter(0))}')
print(f'sorted(a, key=itemgetter(0, 1)): {sorted(a, key=itemgetter(0, 1))}')
print(f'sorted(a, key=itemgetter(1)): {sorted(a, key=itemgetter(1))}')
print(f'sorted(a, key=itemgetter(1), reverse=True): {sorted(a, key=itemgetter(1), reverse=True)}')

#####################
# Bytearrays
#####################
print(f'bytearray(): {bytearray()}') # empty bytearray object
print(f'bytearray(10): {bytearray(10)}') # zero-filled instance with given length
print(f'bytearray(range(5)): {bytearray(range(5))}') # zero-filled instance with given length
name = bytearray(b'Lina') # bytearray from bytes
print(f"name.replace(b'L', b'l'): {name.replace(b'L', b'l')}")
print(f"name.endswith(b'na'): {name.endswith(b'na')}")
print(f'name.upper(): {name.upper()}')
print(f"name.count(b'L'): {name.count(b'L')}")