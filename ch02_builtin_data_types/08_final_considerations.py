#############################
# Final consideration
#############################

#############################
# ## Small value caching
#############################
a = 1000000
b = 1000000
print(f'id(a) == id(b): {id(a) == id(b)}')

a = 5
b = 5
print(f'id(a) == id(b): {id(a) == id(b)}')

##################################
# ## How to choose data structures
##################################
# example customer objects
customer1 = {'id': 'abc123', 'full_name': 'Master Yoda'}
customer2 = {'id': 'def456', 'full_name': 'Obi-Wan Kenobi'}
customer3 = {'id': 'ghi789', 'full_name': 'Anakin Skywalker'}

# collect them in a tuple
customers = (customer1, customer2, customer3)

# or collect them in a list
customers = [customer1, customer2, customer3]

# or maybe within a dictionary, they have a unique id after all
customers = {
    'abc123': customer1,
    'def456': customer2,
    'ghi789': customer3,
}

###############################
# ## About indexing and slicing
###############################
a = list(range(10))  # `a` has 10 elements. Last one is 9.
print(f'a: {a}')
print(f'len(a): {len(a)}')  # its length is 10 elements
print(f'a[len(a) - 1]: {a[len(a) - 1]}')  # position of last one is len(a) - 1
print(f'a[-1]: {a[-1]}')  # but we don't need len(a)! Python rocks!
print(f'a[-2]: {a[-2]}')  # equivalent to len(a) - 2
print(f'a[-3]: {a[-3]}')  # equivalent to len(a) - 1

###############################
# ## About names
###############################
