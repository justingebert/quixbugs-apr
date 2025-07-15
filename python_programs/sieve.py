def sieve(max):
    if max < 2:
        return []

    # Create a boolean list where is_prime[i] is True if i is prime
    is_prime = [True] * (max + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    # Start checking from p = 2
    # We only need to iterate up to sqrt(max)
    # Any composite number n must have a prime factor less than or equal to sqrt(n)
    p = 2
    while (p * p) <= max:
        # If is_prime[p] is still True, then p is a prime number
        if is_prime[p]:
            # Mark all multiples of p (starting from p*p) as not prime
            # Multiples less than p*p would have already been marked by smaller primes
            for multiple in range(p * p, max + 1, p):
                is_prime[multiple] = False
        p += 1  # Move to the next number

    # Collect all numbers that are marked as prime
    primes = []
    for n in range(2, max + 1):
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
