import sys


def solveKnapsack(capacity, items):
    n = len(items)

    # setting up table
    table = [[0 for j in range(capacity + 1)] for i in range(n+1)]

    # filling the table
    for i in range(1, n+1):
        weight, value = items[i-1]
        for j in range(1, capacity + 1):
            if weight > j:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = max(
                    table[i - 1][j], table[i - 1][j - weight] + value)

    # going back to fill the result
    result = []
    j = capacity
    for i in range(n, 0, -1):
        if table[i][j] != table[i - 1][j]:
            result.append(i - 1)
            j -= items[i - 1][0]
    # reverse since its backwards
    result.reverse()

    return len(result), result


while line := sys.stdin.readline().split():

    capacity, n = map(int, line)

    items = []

    for _ in range(n):
        value, weight = map(int, sys.stdin.readline().split())
        items.append((weight, value))

    numberOfItems, indexes = solveKnapsack(capacity, items)
    print(numberOfItems)
    print(' '.join(map(str, indexes)))
