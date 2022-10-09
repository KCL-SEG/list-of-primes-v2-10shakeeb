"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import itertools

def primes(number_of_primes):
    D = {}
    q = 2

    while True:
        if number_of_primes <= 0:
            raise ValueError
        elif q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
            q += 1

    list = list(itertools.islice(gen_primes(), number_of_primes))
    return list
