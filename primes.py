"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import itertools

def primes(number_of_primes):
    list =[]
    if number_of_primes > 0:
        chkthis = 2
        while len(primes) < N:
            ptest    = [chkthis for i in primes if chkthis%i == 0]
            list  += [] if ptest else [chkthis]
            chkthis += 1
    else:
        raise ValueError
    return list
