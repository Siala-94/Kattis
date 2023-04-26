import sys


def fill():
    birds = []
    ind = sys.stdin.readline()
    l, d, n = ind.split()
    for i in range(int(n)):
        ind = sys.stdin.readline()
        begin = int(ind) - int(d) + 1

        end = int(ind) + int(d) - 1

        bird = (begin, end)
        birds.append(bird)
    return int(l), int(d), birds


def solve(l, d, birds):

    maxdist = l-6
    current = 6
    # end = current
    amount = 0

    if len(birds) == 0:
        amount += int(abs(maxdist-current)/d)
        return amount+1

    if current < birds[0][0]:
        amount = 1
        current += d

    for i in range(len(birds)):

        if current < birds[i][0]:
            # room for more?
            amount += 1
            current += d
            amount += int(abs((birds[i][0] - current))/d)  # ?
            current = birds[i][1] + d - 1

        else:
            current = birds[i][1] + 1

    # current = 34

    if current <= maxdist:

        amount += 1
        current += d

        val = int(((maxdist - current))/d)

        if val > 0:
            amount += val

    return amount


l, d, birds = fill()

birds.sort(key=lambda x: x[0])
amount = solve(l, d, birds)

print(amount)
