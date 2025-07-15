def sieve(max):
    """Generate all prime numbers up to max using Sieve of Eratosthenes."""
    if max < 2:
        return []

    is_prime = [True] * (max + 1)
    is_prime[0] = False
    is_prime[1] = False

    for num in range(2, int(max**0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, max + 1, num):
                is_prime[multiple] = False

    primes = [n for n in range(2, max + 1) if is_prime[n]]
    return primes


"""
Sieve of Eratosthenes
prime-sieve

Input:
    max: A positive int representing an upper bound.

Output:
    A list containing all primes up to and including max
"""
