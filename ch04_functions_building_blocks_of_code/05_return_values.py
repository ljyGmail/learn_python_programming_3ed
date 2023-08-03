################################
# Return values
################################
# return.none.py
from operator import mul
from functools import reduce


def func():
    pass


func()  # the return of this call won't be collected. It's lost.
a = func()  # the return of this one instead is collected into 'a'
print(f'a: {a}')  # prints: None

# return.single.value.py


def factorial(n):
    if n in (0, 1):
        return 1
    result = n
    for k in range(2, n):
        result *= k
    return result


f5 = factorial(5)  # f5 = 120
print(f'f5: {f5}')

# return.single.value.2.py


def factorial(n):
    return reduce(mul, range(1, n + 1), 1)


f5 = factorial(5)  # f5 = 120
print(f'f5: {f5}')

################################
# ## Returning multiple values
################################
# return.multiple.py


def moddiv(a, b):
    return a // b, a % b


print(f'moddiv(20, 7): {moddiv(20, 7)}')  # prints: (2, 6)
