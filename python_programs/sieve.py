def sieve(max):
    if max < 2:
        return []

    # Create a boolean list `is_prime[i]` which is true if i is prime
    # Initialize all entries as True
    is_prime = [True] * (max + 1)

    # 0 and 1 are not prime numbers
    is_prime[0] = False
    is_prime[1] = False

    # Iterate from 2 up to the square root of max
    # Any composite number N will have at least one prime factor less than or equal to sqrt(N)
    for p in range(2, int(max**0.5) + 1):
        # If p is still marked as prime
        if is_prime[p]:
            # Mark all multiples of p (starting from p*p) as not prime
            # Multiples smaller than p*p (e.g., 2*p, 3*p) would have already been marked by their smaller prime factors
            for multiple in range(p * p, max + 1, p):
                is_prime[multiple] = False

    # Collect all numbers for which `is_prime` is True
    primes = []
    for n in range(2, max + 1):  # Start from 2 as 0 and 1 are explicitly handled
        if is_prime[n]:
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
