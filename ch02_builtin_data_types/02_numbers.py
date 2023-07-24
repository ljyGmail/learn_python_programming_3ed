####################
# Numbers
####################

####################
## Integers
####################
a = 14
b = 3
print(f'a + b: {a + b}') # addition
print(f'a - b: {a - b}') # subtraction
print(f'a * b: {a * b}') # multiplication
print(f'a / b: {a / b}') # true division
print(f'a // b: {a // b}') # integer division
print(f'a % b: {a % b}') # modulo operation (reminder of division)
print(f'a ** b: {a ** b}') # power operation

# division with negative numbers
print(f'7 / 4: {7 / 4}') # true division
print(f'7 // 4: {7 // 4}') # integer division, truncation returns 1
print(f'-7 / 4: {-7 / 4}') # true division again, result is opposite of previous
print(f'-7 // 4: {-7 // 4}') # integer division, result not the opposite of previous: floored quotient

# truncate a number to an iteger
print(f'int(1.75): {int(1.75)}')
print(f'int(-1.75): {int(-1.75)}')

print(f"int('10110', base=2): {int('10110', base=2)}")

# the power operator ** has a  built-in function counterpart
print(f'pow(10, 3): {pow(10, 3)}')
print(f'10 ** 3: {10 ** 3}')
print(f'pow(10, -3): {pow(10, -3)}')
print(f'10 ** -3: {10 ** -3}')

# modulo operator 
print(f'10 % 3: {10 % 3}') # remainder of the division 10 // 3
print(f'10 % 4: {10 % 4}') # remainder of the division 10 // 4

# the pow() function allows a third argument to perform modular exponentiation
print(f'pow(123, 4): {pow(123, 4)}') # 228886641
print(f'pow(123, 4, 100): {pow(123, 4, 100)}') # 228886641 % 100 == 41
print(f'pow(37, -1, 43): {pow(37, -1, 43)}') # modular inverse of 37 mod 43
print(f'7 * 37 % 43: {7 * 37 % 43}') # proof the above is correct

# add underscores within number literals
n = 1_024
print(f'n: {n}')
hex_n = 0x_4_0_0 # 0x400 == 1024
print(f'hex_n: {hex_n}')

####################
## Booleans
####################
print(f'int(True): {int(True)}') # True behaves like 1
print(f'int(False): {int(False)}') # False behaves like 0
print(f'bool(1): {bool(1)}') # 1 evaluates to True in a Boolean context
print(f'bool(-42): {bool(-42)}') # and so does every non-zero number
print(f'bool(0): {bool(0)}') # 0 evaluates to False
# quick peek at the operators (and, or, not)
print(f'not True: {not True}')
print(f'not False: {not False}')
print(f'True and True: {True and True}')
print(f'False or True: {False or True}')

# Python upcasts booleans to integers and performs the addition
print(f'1 + True: {1 + True}')
print(f'False + 42: {False + 42}')
print(f'7 - True: {7 - True}')

####################
## Real numbers
####################
pi = 3.1415926536 # how many digits of PI can you remember?
radius = 4.5
area = pi * (radius ** 2)
print(f'area: {area}')

import sys
print(f'sys.float_info: {sys.float_info}')

print(f'0.3 - 0.1 * 3: {0.3 - 0.1 * 3}') # this should be 0!!!

####################
## Complex numbers
####################
c = 3.14 + 2.73j
c = complex(3.14, 2.73) # same as above
print(f'c.real: {c.real}') # real part
print(f'c.imag: {c.imag}') # imaginary part
print(f'c.conjugate(): {c.conjugate()}') # conjugate of A + Bj is A - Bj
print(f'c * 2: {c * 2}') # multiplication is allowed
print(f'c ** 2: {c ** 2}') # power operation as well

d = 1 + 1j # addition and subtraction as well
print(f'c - d: {c - d}')

#########################
## Fractions and decimals
#########################
# Fraction
from fractions import Fraction
print(f'Fraction(10, 6): {Fraction(10, 6)}') # mad hatter? => 5/3 it's been simplified

print(f'Fraction(1, 3) + Fraction(2, 3): {Fraction(1, 3) + Fraction(2, 3)}') # 1/3 + 2/3 == 3/3 == 1/1

f = Fraction(10, 6)
print(f'f.numerator: {f.numerator}')
print(f'f.denominator: {f.denominator}')
print(f'f.as_integer_ratio(): {f.as_integer_ratio()}') # returns a tuple

# Decimal
from decimal import Decimal as D # rename for brevity
print(f'D(3.14): {D(3.14)}') # pi, from float, so approximation issues
print(f"D('3.14'): {D('3.14')}") # pi, from a string, so no approximation issues

print(f'D(0.1) * D(3) - D(0.3): {D(0.1) * D(3) - D(0.3)}') # from float, we still have the issue
print(f"D('0.1') * D(3) - D('0.3'): {D('0.1') * D(3) - D('0.3')}") # from string, all perfect

print(f"D('1.4').as_integer_ratio(): {D('1.4').as_integer_ratio()}") # 7/5 = 1.4 (isn't this cool?!)