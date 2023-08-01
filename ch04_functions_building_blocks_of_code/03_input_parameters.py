################################
# Input parameters
################################

################################
# ## Argument-passing
################################
# key.points.argument.passing.py
x = 3


def func(y):
    print(y)


func(x)  # prints: 3

#####################################
# ## Assignment to parameter names
#####################################
# key.points.assignment.py
x = 3


def func(x):
    x = 7  # defining a local x, not changing the global one


func(x)
print(x)  # prints: 3

#####################################
# ## Changing a mutable object
#####################################
# key.points.mutable.py
x = [1, 2, 3]


def func(x):
    x[1] = 42  # this affects the 'x' argument!


func(x)
print(x)  # prints: [1, 42, 3]

# key.points.mutable.assignment.py
x = [1, 2, 3]


def func(x):
    x[1] = 42  # this changes the original 'x' argument!
    x = 'something else'  # this points x to a new string object


func(x)
print(x)  # still prints: [1, 42, 3]

#####################################
# ## Passing arguments
#####################################

#####################################
# ### Positional arguments
#####################################
# arguments.positional.py


def func(a, b, c):
    print(a, b, c)


func(1, 2, 3)  # prints: 1 2 3

#####################################
# ### Keyword arguments
#####################################
# arguments.keyword.py


def func(a, b, c):
    print(a, b, c)


func(a=1, c=2, b=3)  # prints: 1 3 2

# arguments.positional.keyword.py


def func(a, b, c):
    print(a, b, c)


func(42, b=1, c=2)

# positional arguments have to be listed before any keyword arguments
# func(b=1, c=2, 42) # SyntaxError

#####################################
# ### Iterable unpacking
#####################################
# arguments.unpack.iterable.py


def func(a, b, c):
    print(a, b, c)


values = (1, 3, -7)
func(*values)  # equivalent to func(1, 3, -7)

#####################################
# ### Dictionary unpacking
#####################################
# arguments.unpack.dict.py


def func(a, b, c):
    print(a, b, c)


values = {'b': 1, 'c': 2, 'a': 42}
func(**values)  # equivalent to func(b=1, c=2, a=42)

#####################################
# ### Combining argument types
#####################################
# arguments.combined.py
"""
Arguments must be passed in the following order:
    * First, positional arguments: both ordinary (name) and iterable unpacking
    * Next come keyword arguments (name=value), which can be mixed with iterable unpacking (*name)
    * Finally, there is dictionary unpacking (**name), which can be mixed with keyword arguments (name=value)
"""


def func(a, b, c, d, e, f):
    print(a, b, c, d, e, f)


func(1, *(2, 3), f=6, *(4, 5))
func(*(1, 2), e=5, *(3, 4), f=6)
func(1, **{'b': 2, 'c': 3}, d=4, **{'e': 5, 'f': 6})
func(c=3, *(1, 2), **{'d': 4}, e=5, **{'f': 6})

# arguments.multiple.value.py


def func(a, b, c):
    print(a, b, c)


# func(2, 3, a=1) # func() got multiple values for argument 'a'
