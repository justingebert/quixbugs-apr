def sieve(max):
    primes = []
    for n in range(2, max + 1):
        # A number 'n' is prime if it is not divisible by any previously found prime.
        # The original condition `any(n % p > 0 for p in primes)` was incorrect.
        # - `any(...)` evaluates to False for an empty `primes` list, preventing 2 from being added.
        # - `n % p > 0` means 'n' is not divisible by 'p'. We need 'n' to be not divisible
        #   by *any* previously found prime, so `all` is appropriate here.
        # - If `n % p == 0` for any `p`, then `n` is not prime. So we check `n % p != 0`.
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
