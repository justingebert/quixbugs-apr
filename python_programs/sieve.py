def sieve(max):
    primes = []
    is_prime = [True] * (max + 1)
    is_prime[0] = is_prime[1] = False

    for n in range(2, max + 1):
        if is_prime[n]:
            primes.append(n)
            for multiple in range(n * n, max + 1, n):
                is_prime[multiple] = False
    return primes


"""
Sieve of Eratosthenes
prime-sieve

Input:
    max: A positive int representing an upper bound.

Output:
    A list containing all primes up to and including max
"""
