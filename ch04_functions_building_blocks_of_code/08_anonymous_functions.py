################################
# Anonymous functions
################################
# filter.regular.py
def is_multiple_of_five(n):
    return not n % 5


def get_multiples_of_five(n):
    return list(filter(is_multiple_of_five, range(n)))


print(f'get_multiples_of_five(30): {get_multiples_of_five(30)}')

# filter.lambda.py


def get_multiples_of_five(n):
    return list(filter(lambda k: not k % 5, range(n)))


print(f'get_multiples_of_five(40): {get_multiples_of_five(40)}')

# lambda.explained.py
# example 1: adder


def adder(a, b):
    return a+b


# is equivalent to:
def adder_lambda(a, b): return a + b

# example 2: to uppercase


def to_upper(s):
    return s.upper()


# is equivalent to:
def to_upper_lambda(s): return s.upper()
