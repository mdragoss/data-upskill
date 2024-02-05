"""Helper functions for the project."""
import time

tuple_factory = lambda x: tuple([value for value in x if value is not None])


def time_function(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print(
            f'Function {func.__name__} took {end - start} seconds to complete'
        )

    return wrapper
