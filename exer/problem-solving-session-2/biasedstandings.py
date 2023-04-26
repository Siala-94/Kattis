import sys
import heapq
import math


def solve(Teams, N):
    Teams.sort(key=lambda x: x[1])
    badness = 0

    for i, team in enumerate(Teams):
        desiredPlacement = team[1]
        acutalPlacement = i + 1
        badness += abs(desiredPlacement-acutalPlacement)

    return badness


T = int(sys.stdin.readline())

space = sys.stdin.readline()
badness = []

for t in range(T):
    N = int(sys.stdin.readline())
    teams = []

    for n in range(N):
        tn, r = sys.stdin.readline().split()
        teams.append((tn, int(r)))
    badness.append(solve(teams, N))
    if t == T-1:
        break
    space = sys.stdin.readline()


for bad in badness:
    print(bad)
