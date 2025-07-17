def sieve(max):
    if max < 2:
        return []

    sieve_list = [True] * (max + 1)
    sieve_list[0] = False
    sieve_list[1] = False

    for num in range(2, int(max**0.5) + 1):
        if sieve_list[num]:
            for multiple in range(num * num, max + 1, num):
                sieve_list[multiple] = False

    primes = [n for n in range(2, max + 1) if sieve_list[n]]
    return primes


"""
Sieve of Eratosthenes
prime-sieve

Input:
    max: A positive int representing an upper bound.

Output:
    A list containing all primes up to and including max
"""
