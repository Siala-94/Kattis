import bisect
import sys


def longestIncreasingSubsequence(seq):
    n = len(seq)
    subseq = [0]
    R = [(2 ^ 31)+1] * n
    for i, number in enumerate(seq):

        position = bisect.bisect_left(subseq, number)

        # more than max?
        if position > len(subseq)-1:
            subseq.append(number)
            R[i] = subseq[position-1]
        # else insert in position
        else:
            subseq[position] = number
            # less than min?
            if position > 0:
                R[i] = subseq[position-1]

    num = subseq[-1]
    result = []

    for i in range(n-1, -1, -1):
        if seq[i] == num:
            result.append(i)
            num = R[i]

    return result[::-1]


while sys.stdin.readline():

    seq = list(map(int, sys.stdin.readline().split()))
    res = longestIncreasingSubsequence(seq)

    print(len(res))
    print(" ".join([str(i) for i in res]))
