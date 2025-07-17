# Python 3
def possible_change(coins, total):
    if total == 0:
        return 1
    if total < 0:
        return 0
    # If there are no coins left and total is still greater than 0,
    # it's impossible to make change.
    if not coins:
        return 0

    first, *rest = coins
    # Option 1: Use the first coin. We can use it again, so 'coins' is passed.
    # We reduce the total by the value of the first coin.
    ways_with_first_coin = possible_change(coins, total - first)

    # Option 2: Do not use the first coin. Move to the next set of coins ('rest').
    # The total remains the same as we haven't used any coin from this branch.
    ways_without_first_coin = possible_change(rest, total)

    return ways_with_first_coin + ways_without_first_coin
