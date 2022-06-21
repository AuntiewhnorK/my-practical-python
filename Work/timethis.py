"""
Practical Python - Decorators

Auntiewhnor Kpolie
6/21/2022

Decorator wrapper that prints
how long it took for this function
to execute
"""
import time


def timethis(func):  # decorator
    # wrapper to count execution time in seconds
    def wrapper(*args, **kwargs):
        start = time.time()
        run = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__module__}.{func.__name__}: {end-start:2f} seconds to execute")

    return wrapper
