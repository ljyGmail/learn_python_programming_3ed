################################
# A few useful tips
################################
"""
* Functions should do one thing.
* Functions should be small.
* The fewer input parameters, the better.
* Functions should be consistent in their return value
* Functions shouldn't have side effects.
"""
numbers = [4, 1, 7, 5]
# won't sort the original 'numbers' list
print(f'sorted(numbers): {sorted(numbers)}')
print(f'numbers: {numbers}')  # let's verify, good, untouched
numbers.sort()  # this will act on the list
print(f'numbers: {numbers}')
