def sieve(max):
    if max < 2:
        return []
    sieve = [True] * (max + 1)
    sieve[0] = False
    sieve[1] = False
    for num in range(2, int(max**0.5) + 1):
        if sieve[num]:
            for multiple in range(num * num, max + 1, num):
                sieve[multiple] = False
    return [num for num in range(2, max + 1) if sieve[num]]


"""
Sieve of Eratosthenes
prime-sieve

Input:
    max: A positive int representing an upper bound.

Output:
    A list containing all primes up to and including max
"""
