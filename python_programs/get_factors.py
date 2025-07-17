def get_factors(n):
    if n == 1:
        return []

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return [i] + get_factors(n // i)

    # If no factors found and n > 1, n is prime
    if n > 1:
        return [n]
    return []
