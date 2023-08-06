#######################################
# Comprehensions
#######################################
# squares.map.py
# If you code like this you are not a Python dev! ;)
from string import ascii_lowercase
from math import sqrt
squares = []
for n in range(10):
    squares.append(n ** 2)

print(f'squares: {squares}')

# This is better, one line, nice and readable
squares = map(lambda n: n**2, range(10))
print(f'list(squares): {list(squares)}')

# squares.comprehension.py
[n ** 2 for n in range(10)]
print(f'[n ** 2 for n in range(10)]: {[n ** 2 for n in range(10)]}')

# even.squares.py
# using map and filter
sq1 = list(map(lambda n: n ** 2, filter(lambda n: not n % 2, range(10))))
# equivalent, but using list comprehensions
sq2 = [n ** 2 for n in range(10) if not n % 2]
print(f'sq1: {sq1},', f'sq1 == sq2: {sq1 == sq2}')

#######################################
# ## Nested comprehensions
#######################################
# pairs.for.loop.py
items = 'ABCD'
pairs = []

for a in range(len(items)):
    for b in range(a, len(items)):
        pairs.append((items[a], items[b]))

print(f'pairs: {pairs}')

# pairs.list.comprehension.py
items = 'ABCD'
pairs = [(items[a], items[b])
         for a in range(len(items)) for b in range(a, len(items))]
print(f'pairs: {pairs}')

#######################################
# ## Filtering a comprehension
#######################################
# pythagorean.triple.py
# this will generate all possible pairs
mx = 10
triples = [(a, b, sqrt(a ** 2 + b ** 2))
           for a in range(1, mx) for b in range(a, mx)]
# this will filter out all non-Pythagorean triples
triples = list(filter(lambda triple: triple[2].is_integer(), triples))
print(f'triples: {triples}')

# pythagorean.triple.int.py
mx = 10
triples = [(a, b, sqrt(a ** 2 + b ** 2))
           for a in range(1, mx) for b in range(a, mx)]
triples = filter(lambda triple: triple[2].is_integer(), triples)
# this will make the third number in the tuples integer
triples = list(map(lambda triple: triple[:2] + (int(triple[2]), ), triples))
print(f'triples: {triples}')  # prints: [(3, 4, 5), (6, 8, 10)]

# pythagorean.triple.comprehension.py
# this step is the same as before
mx = 10
triples = [(a, b, sqrt(a ** 2 + b ** 2))
           for a in range(1, mx) for b in range(a, mx)]
# here we combine filter and map in one CLEAN list comprehension
triples = [(a, b, int(c)) for a, b, c in triples if c.is_integer()]
print(f'triples: {triples}')  # prints: [(3, 4, 5), (6, 8, 10)]

# pythagorean.triple.walrus.py
# this step is the same as before
mx = 10
# we can combine generating and filtering in one comprehension
triples = [(a, b, int(c))
           for a in range(1, mx) for b in range(a, mx)
           if (c := sqrt(a ** 2 + b ** 2)).is_integer()]
print(f'triples: {triples}')  # prints: [(3, 4, 5), (6, 8, 10)]

#######################################
# ## Dictionary comprehensions
#######################################
# dictionary.comprehension.py
lettermap = {c: k for k, c in enumerate(ascii_lowercase, 1)}
# equivalent to the above
lettermap = dict((c, k) for k, c in enumerate(ascii_lowercase, 1))
print(f'lettermap: {lettermap}')

# dictionary.comprehensions.duplicates.py
word = 'Hello'
swaps = {c: c.swapcase() for c in word}
print(f'swaps: {swaps}')  # prints: {'H': 'h', 'e': 'E', 'l': 'L', 'o': 'O'}

# dictionary.comprehensions.positions.py
word = 'Hello'
positions = {c: k for k, c in enumerate(word)}
print(f'positions: {positions}')

#######################################
# ## Set comprehensions
#######################################
# set.comprehensions.py
word = 'Hello'
letters1 = {c for c in word}
letters2 = set(c for c in word)
print(letters1)  # prints: {'H', 'e', 'l', 'o'}
print(letters1 == letters2)  # prints: True
