import heapq
import sys
import time


def solve(M, N, children_wishes):

    remainder = sum(wishes) - M  # number of remaining candies

    anger = 0
    for i, wish in enumerate(wishes):
        kids = N - i  # number of remaining kids
        candies = min(wish, remainder / kids)
        anger += (candies * candies)
        remainder -= candies
    print(anger)


M, N = map(int, sys.stdin.readline().split())
wishes = [int(sys.stdin.readline()) for _ in range(N)]
print(solve(M, N, wishes))
