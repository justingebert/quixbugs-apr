# Python 3
def possible_change(coins, total):
    if total == 0:
        return 1
    if total < 0:
        return 0
    if not coins:  # If no coins are left, and total is still > 0, no way to make change
        return 0

    first, *rest = coins
    return possible_change(coins, total - first) + possible_change(rest, total)
