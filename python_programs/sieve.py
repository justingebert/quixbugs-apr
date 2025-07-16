def sieve(max):
    if max < 2:
        return []

    is_prime = [True] * (max + 1)
    is_prime[0] = False
    is_prime[1] = False

    for number in range(2, int(max**0.5) + 1):
        if is_prime[number]:
            for multiple in range(number * number, max + 1, number):
                is_prime[multiple] = False

    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes


"""
Sieve of Eratosthenes
prime-sieve

Input:
    max: A positive int representing an upper bound.

Output:
    A list containing all primes up to and including max
"""
