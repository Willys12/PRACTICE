#!/usr/bin/python3
import math

def multiply_with_loop_imperfect(x, y):
    return x * y

def multiply_with_loop_better(x, y):
    if (x >= 0 and y >= 0) or (x < 0 and y < 0):
        return sum(abs(y) for _ in range(abs(x)))
    elif x < 0:
        return -sum(abs(x) for _ in range(abs(y)))
    else:
        return -sum(abs(y) for _ in range(abs(x)))
