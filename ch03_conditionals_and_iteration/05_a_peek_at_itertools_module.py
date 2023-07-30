######################################
# A quick peek at the itertools module
######################################

##########################
# ## Infinite iterators
##########################
from itertools import permutations
from itertools import compress
from itertools import count

for n in count(5, 3):
    if n > 20:
        break
    print(n, end=', ')  # instead of newline, comma and space
print()

#############################################################
# ## Iterators terminating on the shortest input sequence
#############################################################
data = range(10)
even_selector = [1, 0] * 10
odd_selector = [0, 1] * 10

even_numbers = list(compress(data, even_selector))
odd_numbers = list(compress(data, odd_selector))

print(f'odd_selector: {odd_selector}')
print(f'even_selector: {even_selector}')
print(f'list(data): {list(data)}')
print(f'even_numbers: {even_numbers}')
print(f'odd_numbers: {odd_numbers}')

###############################
# ## Combinatoric generators
###############################
print(f"list(permutations('ABC')): {list(permutations('ABC'))}")
