def sieve(max):
    # Create a boolean array "is_prime[0..max]" and initialize
    # all entries as true. A value in is_prime[i] will finally be
    # false if i is Not a prime, else true.
    is_prime = [True] * (max + 1)
    is_prime[0] = is_prime[1] = False

    # Use the sieve algorithm to mark non-primes
    for i in range(2, int(max**0.5) + 1):
        if is_prime[i]:
            # Update all multiples of i starting from i*i
            for j in range(i * i, max + 1, i):
                is_prime[j] = False

    # Collect and return primes
    return [num for num in range(2, max + 1) if is_prime[num]]


"""
Sieve of Eratosthenes
prime-sieve

Input:
    max: A positive int representing an upper bound.

Output:
    A list containing all primes up to and including max
"""
