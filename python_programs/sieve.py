def sieve(max):
    """
    Sieve of Eratosthenes
    prime-sieve

    Input:
        max: A positive int representing an upper bound.

    Output:
        A list containing all primes up to and including max
    """
    if max < 2:
        return []

    # Create a boolean array "is_prime[0..max]" and initialize
    # all entries it as true. A value in is_prime[i] will
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * (max + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    # Iterate from p = 2 up to sqrt(max).
    # The loop runs while p*p is less than or equal to max.
    # This optimization ensures we only iterate up to the square root of max.
    # Numbers greater than sqrt(max) would have a prime factor
    # less than or equal to sqrt(max), which would have already been processed.
    p = 2
    while p * p <= max:
        # If is_prime[p] is still true, then it is a prime
        if is_prime[p]:
            # Mark all multiples of p (starting from p*p) as not prime.
            # Multiples less than p*p would have already been marked by
            # smaller prime factors. For example, 2*3=6 would be marked by 2,
            # not 3 if we started from 2*p. So we start from p*p.
            for multiple in range(p * p, max + 1, p):
                is_prime[multiple] = False
        p += 1

    # Collect all prime numbers
    primes = [i for i, prime_status in enumerate(is_prime) if prime_status]
    return primes
