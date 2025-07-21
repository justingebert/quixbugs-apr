def sieve(max):
    if max < 2:
        return []

    # Create a boolean array `is_prime[0...max]` and initialize all entries to True.
    # `is_prime[i]` will be False if i is not prime, else True.
    is_prime = [True] * (max + 1)
    is_prime[0] = False
    is_prime[1] = False

    # Start checking from p = 2
    p = 2
    while p * p <= max:
        # If is_prime[p] is still True, then it is a prime number
        if is_prime[p]:
            # Mark all multiples of p (starting from p*p) as not prime
            for multiple in range(p * p, max + 1, p):
                is_prime[multiple] = False
        p += 1

    # Collect all prime numbers
    primes = [number for number, is_it_prime in enumerate(is_prime) if is_it_prime]

    return primes


"""
Sieve of Eratosthenes
prime-sieve

Input:
    max: A positive int representing an upper bound.

Output:
    A list containing all primes up to and including max
"""
