import sys

# with open('main.in', 'r') as f:
#     sys.stdin = f


def solver(A, B, intervals):

    start = A
    end = A-1

    interval_count = 0
    cover = []

    curr_index = 0

    intervals.sort()

    for interval in intervals:
        if interval[0] <= start and interval[2] >= 0:
            if end < interval[1]:
                curr_index = interval[2]
                end = interval[1]
        else:
            if end < interval[0]:
                break

            if start != end:
                start = end
                interval_count += 1
                cover.append(curr_index)

            if end >= B:
                break

            if interval[0] <= start:
                end = interval[1]
                curr_index = interval[2]

    if end < B:
        return []
    else:
        if start != end:
            interval_count += 1
            cover.append(curr_index)
        return cover


while line := sys.stdin.readline().split():
    A, B = map(float, line)
    n = int(sys.stdin.readline())

    intervals = []
    for i in range(n):
        interval = tuple(map(float, sys.stdin.readline().split()))
        intervals.append(interval + (i,))

    intervalCover = solver(A, B, intervals)

    print(len(intervalCover) if intervalCover else "impossible")

    if intervalCover:
        print(" ".join(str(i) for i in intervalCover))
