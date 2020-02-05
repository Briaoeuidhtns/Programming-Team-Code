from math import gcd


# Assumes m is prime
def mod_inverse(x, y, m):
    if gcd(a, m) != 1:
        raise ValueError("Inverse doesn't exist")

    # If a and m are relatively prime, then modulo inverse is a^(m-2) mod m
    return pow(a, m - 2, m)
