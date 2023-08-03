################################
# Recursive functions
################################
# recursive.factorial.py
import sys


def factorial(n):
    if n in (0, 1):  # base case
        return 1
    return factorial(n-1) * n  # recursive case


f5 = factorial(5)
print(f'f5: {f5}')

# check recursion limit
print(sys.getrecursionlimit())
