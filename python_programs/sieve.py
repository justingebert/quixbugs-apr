import math


def sieve(max_val):  # Renamed 'max' to 'max_val' to avoid shadowing built-in function
    if max_val < 2:
        return []

    # Create a boolean list `is_prime` of size `max_val + 1`
    # and initialize all entries to True.
    # `is_prime[i]` will be False if `i` is not prime, True otherwise.
    is_prime = [True] * (max_val + 1)
    is_prime[0] = False  # 0 is not prime
    is_prime[1] = False  # 1 is not prime

    # Iterate from p = 2 up to sqrt(max_val).
    # All numbers greater than sqrt(max_val) that are not primes
    # will have a prime factor less than or equal to sqrt(max_val).
    for p in range(2, int(math.sqrt(max_val)) + 1):
        # If is_prime[p] is still True, then it is a prime number
        if is_prime[p]:
            # Mark all multiples of p (starting from p*p) as not prime.
            # Multiples less than p*p would have already been marked by
            # smaller prime factors. For example, 2*p is marked by 2.
            for multiple in range(p * p, max_val + 1, p):
                is_prime[multiple] = False

    # Collect all numbers that are marked as prime
    primes = []
    for n in range(2, max_val + 1):
        if is_prime[n]:
            primes.append(n)

    return primes


"""
Sieve of Eratosthenes
prime-sieve

Input:
    max_val: A positive int representing an upper bound.

Output:
    A list containing all primes up to and including max_val
"""
