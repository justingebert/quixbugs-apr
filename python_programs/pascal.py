def pascal(n):
    if n == 0:
        return []
    rows = [[1]]
    for r_idx in range(1, n):
        prev_row = rows[r_idx - 1]
        current_row = [1]
        for c_idx in range(1, r_idx):
            current_row.append(prev_row[c_idx - 1] + prev_row[c_idx])
        current_row.append(1)
        rows.append(current_row)

    return rows


"""
Pascal's Triangle
pascal



Input:
    n: The number of rows to return

Precondition:
    n >= 1

Output:
    The first n rows of Pascal's triangle as a list of n lists

Example:
    >>> pascal(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
"""
