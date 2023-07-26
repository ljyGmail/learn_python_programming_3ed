#####################
# Set types
#####################
small_primes = set() # empty set
small_primes.add(2) # adding one element at a time
small_primes.add(3)
small_primes.add(5)
print(f'small_primes: {small_primes}')
small_primes.add(1) # Look what I've done, 1 is not a prime!
print(f'small_primes: {small_primes}')
small_primes.remove(1) # so let's remove it
print(f'3 in small_primes: {3 in small_primes}') # membership test
print(f'4 in small_primes: {4 in small_primes}')
print(f'4 not in small_primes: {4 not in small_primes}') # negated membership test
small_primes.add(3) # trying to add 3 again
print(f'small_primes: {small_primes}') # no change, duplication is not allowed
bigger_primes = set([5, 7, 11, 13]) # faster creation
print(f'small_primes | bigger_primes: {small_primes | bigger_primes}') # union operator `|`
print(f'small_primes & bigger_primes: {small_primes & bigger_primes}') # intersection operator `&`
print(f'small_primes - bigger_primes: {small_primes - bigger_primes}') # difference operator `-`

# another way to creating a set is by simply using the curly braces notation
small_primes = {2, 3, 5, 5, 3}
print(f'small_primes: {small_primes}')

# immutable counterpart of the set type: fronzenset
small_primes = frozenset([2, 3, 5, 7])
bigger_primes = frozenset([5, 7, 11])
# small_primes.add(11) # we cannot add to a frozenset # # we cannot add to a frozenset # # we cannot add to a frozenset # # we cannot add to a frozenset # # we cannot add to a frozenset
# small_primes.remove(2) # nor can we remove
print(f'small_primes & bigger_primes: {small_primes & bigger_primes}') # intersect, union, etc. allowed