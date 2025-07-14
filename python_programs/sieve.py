def sieve(max_val):
    primes = []
    is_prime = [True] * (max_val + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, max_val + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, max_val + 1, p):
                is_prime[i] = False
    return primes


"""
Sieve of Eratosthenes
prime-sieve

Input:
    max_val: A positive int representing an upper bound.

Output:
    A list containing all primes up to and including max_val
"""
