from datetime import date, timedelta
#########################
# Looping
#########################

#########################
# ## The for loop
#########################
for number in [0, 1, 2, 3, 4]:
    print(f'number: {number}')

############################
# ### Iterating over a range
############################
for number in range(5):
    print(f'number: {number}')

# one value: from 0 to value (excluded)
print(f'list(range(10)): {list(range(10))}')
# two values: from start to stop (excluded)
print(f'list(range(3, 8)): {list(range(3, 8))}')
# three values: step is added
print(f'list(range(-10, 10, 4)): {list(range(-10, 10, 4))}')

###############################
# ### Iterating over a sequence
###############################
surnames = ['Rivest', 'Shamir', 'Adleman']
print(list(range(len(surnames))))
for position in range(len(surnames)):
    # print(position, surnames[position])
    print(surnames[position][0], end='')
print()

# more Pythonic form
surnames = ['Rivest', 'Shamir', 'Adleman']
for surname in surnames:
    print(surname)

# using enumerate() built-in function
surnames = ['Rivest', 'Shamir', 'Adleman']
for position, surname in enumerate(surnames):
    print(position, surname)

############################
# ## Iterators and iterables
###########################

######################################
# ## Iterating over multiple sequences
######################################
people = ['Nick', 'Rick', 'Roger', 'Syd']
ages = [23, 24, 23, 21]
for position in range(len(people)):
    person = people[position]
    age = ages[position]
    print(person, age)

# improve it by using enumerate():
for position, person in enumerate(people):
    age = ages[position]
    print(person, age)

# zip() function
for person, age in zip(people, ages):
    print(person, age)

# expand the previous example using explicit assignment:
people = ['Nick', 'Rick', 'Roger', 'Syd']
ages = [23, 24, 23, 21]
instruments = ['Drums', 'Keyboards', 'Bass', 'Guitar']
for person, age, instrument in zip(people, ages, instruments):
    print(person, age, instrument)

# implicit assignment
for data in zip(people, ages, instruments):
    person, age, instrument = data
    print(person, age, instrument)

######################################
# ## The while loop
######################################
n = 39
remainders = []
while n > 0:
    remainder = n % 2  # remainder of division by 2
    remainders.append(remainder)  # we keep track of remainders
    n //= 2  # we divide n by 2

remainders.reverse()
print(remainders)

# more Pythonic way using divmod()
n = 39
remainders = []
while n > 0:
    n, remainder = divmod(n, 2)
    remainders.append(remainder)

remainders.reverse()
print(remainders)

people = ['Nick', 'Rick', 'Roger', 'Syd']
ages = [23, 24, 23, 21]
position = 0
while position < len(people):
    person = people[position]
    age = ages[position]
    print(person, age)
    position += 1

######################################
# ## The break and continue statements
######################################
today = date.today()
tomorrow = today + timedelta(days=1)  # today + 1 day is tomorrow
products = [
    {'sku': '1', 'expiration_date': today, 'price': 100.0},
    {'sku': '2', 'expiration_date': tomorrow, 'price': 50},
    {'sku': '3', 'expiration_date': today, 'price': 20},
]

for product in products:
    if product['expiration_date'] != today:
        continue
    product['price'] *= 0.8  # equivalent to applying 20% discount
    print('Price for sku', product['sku'], 'is now', product['price'])

items = [0, None, 0.0, True, 0, 7]  # True and 7 evaluate to True

found = False  # this is called "flag"
for item in items:
    print('scanning item', item)
    if item:
        found = True  # we update the flag
        break

if found:  # we inspect the flag
    print('At least one item evaluates to True')
else:
    print('All items evaluate to False')

######################################
# ## A special else clause
######################################


class DriverException(Exception):
    pass


people = [('James', 17), ('Kirk', 9), ('Lars', 13), ('Robert', 8)]
# regular way to find a driver
driver = None
for person, age in people:
    if age >= 18:
        driver = (person, age)
        break

if driver is None:
    # raise DriverException('Driver not found.')
    print('Driver not found.')

# using for...else syntax
for person, age in people:
    if age >= 18:
        driver = (person, age)
        break
else:
    # raise DriverException('Driver not found.')
    print('Driver not found.')
