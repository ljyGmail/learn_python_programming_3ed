#############################
# Mapping types: dictionaries
#############################
# create a dictionary in five different ways
a = dict(A=1, Z=-1)
b = {'A': 1, 'Z': -1}
c = dict(zip(['A', 'Z'], [1, -1]))
d = dict([('A', 1), ('Z', -1)])
e = dict({'Z': -1, 'A': 1})
print(f'a == b == c == d == e: {a == b == c == d == e}') # They are all the same indeed

# zip() is named after the real-life zip, which glues together two parts, taking one element from each part at a time.
print(f"list(zip(['h', 'e', 'l', 'l', 'o'], [1, 2, 3, 4, 5])): {list(zip(['h', 'e', 'l', 'l', 'o'], [1, 2, 3, 4, 5]))}")
print(f"list(zip('hello', range(1, 6))): {list(zip('hello', range(1, 6)))}") # equivalent, more pythonic

# basic operations
d = {}
d['a'] = 1 # let's set a couple of (key, value) pairs
d['b'] = 2
print(f'len(d): {len(d)}')
print(f"d['a']: {d['a']}") # what is the value of 'a'?
print(f'd: {d}') # how does `d` look now?
del d['a'] # let's remove `a`
print(f'd: {d}') # how does `d` look now?
d['c'] = 3 # let's add 'c': 3
print(f"'c' in d: {'c' in d}") # membership is checked against the keys
print(f'3 in d: {3 in d}') # not the values
print(f"'e' in d: {'e' in d}")
d.clear() # let's clean everything from this dictionary
print(f'd: {d}')

# dictionary views
d = dict(zip('hello', range(5)))
print(f'd: {d}')
print(f'd.keys(): {d.keys()}')
print(f'd.values(): {d.values()}')
print(f'd.items(): {d.items()}')
print(f'3 in d.values(): {3 in d.values()}')
print(f"('o', 4) in d.items(): {('o', 4) in d.items()}")

# some other methods of dictionaries
print(f'd: {d}')
print(f'd.popitem(): {d.popitem()}') # removes a random item (useful in algorithms)
print(f'd: {d}')
print(f"d.pop('l'): {d.pop('l')}") # remove item with key `l`
# d.pop('not-a-key') # remove a key not in dictionary: KeyError
print(f"d.pop('not-a-key', 'default-value'): {d.pop('not-a-key', 'default-value')}") # with a default value?
d.update({'another': 'value'}) # we can update dict this way
d.update(a=13) # or this way (like a function call)
print(f'd: {d}')
print(f"d.get('a'): {d.get('a')}") # same as d['a] but if key is missing no KeyError
print(f"d.get('a', 177): {d.get('a', 177)}") # default value used if key is missing
print(f"d.get('b', 177): {d.get('b', 177)}") # like in this case
print(f"d.get('b'): {d.get('b')}") # key is not there, so None is returned

# setdefault()
d = {}
print(f"d.setdefault('a', 1): {d.setdefault('a', 1)}") # 'a' is missing, we get default value
print(f'd: {d}') # also, the key/value pair ('a', 1) has now been added
print(f"d.setdefault('a', 5): {d.setdefault('a', 5)}") # let's try to override the value
print(f'd: {d}') # no override, as expected

# test knowledge about dictionary methods
d = {}
d.setdefault('a', {}).setdefault('b', []).append(1)
print(f'd: {d}')

# union operator for dict objects
d = {'a': 'A', 'b': 'B'}
e = {'b': 8, 'c': 'C'}
print(f'd | e: {d | e}')
print(f'e | d: {e | d}')
print({**d, **e})
print("{**d, **e}:", {**d, **e})
print("{**e, **d}:", {**e, **d})
d |= e
print(f'd: {d}')