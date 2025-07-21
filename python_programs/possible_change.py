# Python 3
def possible_change(coins, total):
    if total == 0:
        return 1
    if total < 0:
        return 0
    if not coins:  # If no coins are left and total is still > 0, no way to make change.
        return 0

    first, *rest = coins
    # Recurse with two options:
    # 1. Use the 'first' coin (and potentially use it again, so pass 'coins')
    # 2. Don't use the 'first' coin (move to the 'rest' of the coins)
    return possible_change(coins, total - first) + possible_change(rest, total)
