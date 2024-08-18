# calculating factorial of given numbers using 3 different approaches.
# method 1: Recursive
# method 2: Iterative
# method 3: Reduce
from timeit import timeit
from functools import reduce

print('\n-----------------FACTORIALS-------------------\n')

# Recursive
setup_string = """
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
"""
execution_time = timeit("factorial(5)", setup=setup_string, number=1000)
print(f'Recursive: {execution_time:.6f} sec')

# Iterative
setup_string = """
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
"""
execution_time = timeit("factorial(5)", setup=setup_string, number=1000)
print(f'Iterative: {execution_time:.6f} sec')

# Reduce
setup_string = """
from functools import reduce
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))
"""
execution_time = timeit("factorial(5)", setup=setup_string, number=1000)
print(f'Reduce: {execution_time:.6f} sec')

print('\n-----------------END OF FACTORIALS-------------------\n')

# Calculating the sum of factorials of numbers from 1 to 100 using 3 different approaches.
