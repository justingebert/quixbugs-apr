def sieve(max):
    primes = []
    if max < 2:
        return primes
    numbers = [True] * (max + 1)
    numbers[0] = numbers[1] = False
    for p in range(2, int(max**0.5) + 1):
        if numbers[p]:
            for i in range(p * p, max + 1, p):
                numbers[i] = False
    for p in range(2, max + 1):
        if numbers[p]:
            primes.append(p)
    return primes


"""
Sieve of Eratosthenes
prime-sieve

Input:
    max: A positive int representing an upper bound.

Output:
    A list containing all primes up to and including max
"""
