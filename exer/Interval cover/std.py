import sys
import queue


def fill_file():
    file = "in.txt"
    with open(file) as f:
        l = f.readlines()
    return l


def prune(mt, AtoB):
    a = mt[0]
    b = mt[1]
    A = float(AtoB[0])
    B = float(AtoB[1])

    a = A if a < A else a
    b = B if b > B else b

    a = None if a > B else a
    b = None if b < A else b

    return tuple((a, b, mt[2]))


def get_values_std(AtoB):

    n = int(sys.stdin.readline())
    listOfIntervals = []

    for i in range(n):
        values = sys.stdin.readline().split()
        if "-" in values[0]:
            a = float(values[0].strip("-"))

            a -= 2*a
        else:
            a = float(values[0])
        if "-" in values[1]:
            b = float(values[1].strip("-"))
            b -= 2*b
        else:
            b = float(values[1])
        myTuple = (a, float(b), i)
        myTuple = prune(myTuple, AtoB)
        if myTuple[0] == None or myTuple[1] == None:
            pass
        else:
            listOfIntervals.append(myTuple)

    return listOfIntervals


def get_values(l, AtoB):

    n = int(l.pop(0))
    listOfIntervals = []

    for i in range(n):
        values = tuple(l.pop(0).split())

        if "-" in values[0]:
            a = float(values[0].strip("-"))
            a -= 2*a
        else:
            a = float(values[0])
        if "-" in values[1]:
            b = float(values[1].strip("-"))
            b -= 2*b
        else:
            b = float(values[1])

        myTuple = (a, b, i)
        myTuple = prune(myTuple, AtoB)
        if myTuple[0] == None or myTuple[1] == None:
            pass
        else:
            listOfIntervals.append(myTuple)

    return listOfIntervals


def solve(A_B, intervals):

    n = len(intervals)
    amount = 0
    indexes = []
    if n == 1:
        amount = 1
        indexes.append(0)

    if n < 1:
        return -1, indexes

    A = A_B[0]
    B = A_B[1]

    limiter = A
    current_largest = 0

    for i in range(n):
        a = intervals[i][0]
        b = intervals[i][1]

        if a > limiter:
            if a > intervals[current_largest][1]:
                return -1, indexes
            amount += 1
            indexes.append(intervals[current_largest][2])
            limiter = intervals[current_largest][1]
            current_largest = i

        if a <= limiter and limiter < b:
            if b > intervals[current_largest][1]:
                current_largest = i
            else:
                pass

    if a <= limiter and limiter < b:
        amount += 1
        indexes.append(intervals[current_largest][2])
        limiter = intervals[current_largest][1]

    return (amount, indexes) if limiter == B else (-1, indexes)


# l = fill_file()
end = False
while AtoB := tuple(sys.stdin.readline().split()):
    # while not end:
    ans = ""

   # AtoB = tuple(l.pop(0).split())
    AtoB = (float(AtoB[0]), float(AtoB[1]))

    intervals = get_values_std(AtoB)

    # intervals = get_values(l, AtoB)

    #
    # if len(l) < 1:
    #     end = True
    #     pass

    intervals.sort(key=lambda x: x[0])
    least_amount, correct = solve(AtoB, intervals)

    if least_amount == -1:
        print("impossible")
    else:
        print(least_amount)
        for i in range(len(correct)):
            ans += str(correct[i]) + " "
        print(ans)


# list = fill_from_l(l)
# print(type(ans), n)
# covered = abs(B-A)
# L = redo(A, B, n, temp)
# L = mergesort(L,0,len(L)-1)
