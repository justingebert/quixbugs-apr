def sieve(max):
    primes = []
    for n in range(2, max + 1):
        # A number 'n' is prime if it is not divisible by any of the previously found primes.
        # The original condition 'any(n % p > 0 for p in primes)' was incorrect.
        # It checked if 'n' was NOT divisible by AT LEAST ONE prime, which is not sufficient.
        # The correct check is if 'n' is NOT divisible by ALL previously found primes.
        # For the case when 'primes' is empty (for n=2), 'all([])' evaluates to True,
        # correctly adding 2 as the first prime.
        if all(n % p != 0 for p in primes):
            primes.append(n)
    return primes


"""
Sieve of Eratosthenes
prime-sieve

Input:
    max: A positive int representing an upper bound.

Output:
    A list containing all primes up to and including max
"""
