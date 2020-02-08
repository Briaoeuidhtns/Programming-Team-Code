from functools import lru_cache
from math import factorial

@lru_cache(None)
def inv(i: int, m: int) -> int:
    if i == 1:
        return 1
    return (m - (m // i) * inv(m % i, m) % m) % m


@lru_cache(None)
def choose_mod(n: int, k: int, m: int) -> int:
    '''Faster for large n / under mod'''
    return (factorial(n) * inv(factorial(k), m) % m * inv(factorial(n - k), m) % m)


@lru_cache(None)
def choose_small(n: int, k: int) -> int:
    '''Faster for small n'''
    if n < 0 or k < 0:
        raise ValueError

    if k == n or k == 0:
        return 1
    return choose_small(n - 1, k - 1) + choose_small(n - 1, k)
