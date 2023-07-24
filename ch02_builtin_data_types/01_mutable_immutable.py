####################
# Mutable or immutable? That is the question
####################
age = 42
print(f'age: {age}')

age = 43
print(f'age: {age}')

age = 42
print(f'id(age): {id(age)}')

age = 43
print(f'id(age): {id(age)}')

class Person:
    def __init__(self, age):
        self.age = age

fab = Person(age=42)
print(f'fab.age: {fab.age}')
print(f'id(fab): {id(fab)}')
print(f'id(fab.age): {id(fab.age)}')

fab.age = 25 # I wish!
print(f'id(fab): {id(fab)}') # will be the same
print(f'id(fab.age): {id(fab.age)}') # will be different