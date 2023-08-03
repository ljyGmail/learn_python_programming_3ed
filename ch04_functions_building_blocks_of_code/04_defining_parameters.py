################################
# Defining parameters
################################
"""
Function parameters can be classified into five groups:
* Positional or keyword parameters: allow both positional and keyword arguments
* Variable positional parameters: collect an arbitrary number of positional arguments in a tuple
* Variable keyword parameters: collect an arbitrary number of keyword arguments in a dictionary
* Positional-only parameters: can only be passed as positional arguments
* Keyword-only parameters: can only be passed as keyword arguments
"""

################################
# ## Optional parameters
################################
# parameters.default.py


def func(a, b=4, c=88):
    print(a, b, c)


func(1)  # prints: 1 4 88
func(b=5, a=7, c=9)  # prints: 7 5 9
func(42, c=9)  # prints: 42 4 9
func(42, 43, 44)  # prints: 42 43 44

######################################
# ## Variable positional parameters
######################################
# parameters.variable.positional.py


def minimum(*n):
    # print(type(n))  # n is a tuple
    if n:
        mn = n[0]
        for value in n[1:]:
            if value < mn:
                mn = value
        print(mn)


minimum(1, 3, -7, 9)  # n = (1, 3, -7, 9) => prints: -7
minimum()  # n = () - prints: nothing

######################################
# ## Variable keyword parameters
######################################
# parameters.variable.keyword.py


def func(**kwargs):
    print(kwargs)


func(a=1, b=42)  # prints: {'a': 1, 'b': 42}
func()  # prints: {}
func(a=1, b=46, c=99)  # prints: {'a': 1, 'b': 46, 'c': 99}

# parameters.variable.db.py


def connect(**options):
    conn_params = {
        'host': options.get('host', '127.0.0.1'),
        'port': options.get('port', 5432),
        'user': options.get('user', ''),
        'pwd': options.get('pwd', ''),
    }
    print(conn_params)
    # we then connect to the db
    # db.connect(**conn_params)


connect()
connect(host='127.0.0.42', port=5433)
connect(port=5431, user='fab', pwd='gandalf')

######################################
# ## Positional-only parameters
######################################
# parameters.positional.only.py


def func(a, b, /, c):
    print(a, b, c)


func(1, 2, 3)  # prints: 1 2 3
func(1, 2, c=3)  # prints: 1 2 3
# func(1, b=2, c=3)

# parameters.positional.only.optional.py


def func(a, b=2, /):
    print(a, b)


func(4, 5)  # prints 4 5
func(3)  # prints 3 2

# fully emulate behaviors of existing C-coded functions:


def divmod(a, b, /):
    "Emulate the built in divmod() function"
    return (a // b, a % b)

# using positional-only parameters implies that whatever is on the left of /
# remains available for use in variable keyword arguments


def func_name(name, /, **kwargs):
    print(name)
    print(kwargs)


func_name('Positional-only name', name='Name in **kwargs')
# Prints:
# Positional-only name
# {'name': 'Name in **kwargs'}

######################################
# ## Keyword-only parameters
######################################
# parameters.keyword.only.py


def kwo(*a, c):
    print(a, c)


kwo(1, 2, 3, c=7)  # prints: (1, 2, 3) 7
kwo(c=4)  # prints: () 4
# kwo(1, 2) # breaks, invalid syntax, with the following error
# TypeError: kwo() missing 1 required keyword-only argument: 'c'


def kwo2(a, b=42, *, c):
    print(a, b, c)


kwo2(3, b=7, c=99)  # prints: 3 7 99
kwo2(3, c=13)  # prints: 3 42 13
# kwo2(3, 23)  # breaks, invalid syntax, with the following error
# TypeError: kwo2() missing 1 required keyword-only argument: 'c'

######################################
# ## Combining input parameters
######################################
"""
* Positional-only parameters come first, followed by a /.
* Normal parameters go after any positional-only parameters.
* Variable positional parameters go after normal parameters.
* Keyword-only parameters go after variable positional parameters.
* Variable keyword parameters always go last.
* For positional-only and normal parameters, any required parameters have
    to be defined before any optional parameters. This means that if you have
    an optional position-only parameter, all your normal parameters must be 
    optional too. This rule doesn't affect keyword-only parameters.
"""
# parameters.all.py


def func(a, b, c=7, *args, **kwargs):
    print('a, b, c:', a, b, c)
    print('args:', args)
    print('kwargs:', kwargs)


func(1, 2, 3, 5, 7, 9, A='a', B='b')

# parameters.all.pkwonly.py


def allparams(a, /, b, c=42, *args, d=256, e, **kwargs):
    print('a, b, c:', a, b, c)
    print('d, e:', d, e)
    print('args:', args)
    print('kwargs:', kwargs)


allparams(1, 2, 3, 4, 5, 6, e=7, f=9, g=10)

######################################
# ## More signature examples
######################################

######################################
# ## Avoid the trap! Mutable defaults
######################################
# parameters.defaults.mutable.py


def func(a=[], b={}):
    print(a)
    print(b)
    print('#'*12)
    a.append(len(a))  # this will affect a's default value
    b[len(a)] = len(a)  # and this will affect b's one


func()
func()
func()

# parameters.defaults.mutable.intermediate.call.py
func()
func(a=[1, 2, 3], b={'B': 1})
func()

# parameters.defaults.mutable.no.trap.py


def func(a=None):
    if a is None:
        a = []
    # do whatever you want with 'a' ...
