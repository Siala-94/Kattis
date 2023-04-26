import sys
import numpy as np

ActionQueue = []

for i in range(20):
    getline = sys.stdin.readline()
    if getline == "-1":
        break
    else:
        X, Y, T, L, W = map(int, getline.split())

    GRID = np.empty((X+2, Y+2), dtype=str)

    for x in range(X+2):
        GRID[x, 0] = "W"
        GRID[x, Y+1] = "W"
    for y in range(Y+2):
        GRID[0, y] = "W"
        GRID[X+1, y] = "W"

    leaks = [*map(int, sys.stdin.readline().split())]
    print(len(leaks))
    for j in range(0, len(leaks), 2):
        GRID[leaks[j], leaks[j+1]] = "L"
    print(GRID)

    w = 0
    # maxcoordinate = 4*W
    walls = []
    while w < 4*W:
        wall = [*map(int, sys.stdin.readline().split())]

        for j in range(0, len(wall), 4):
            
            GRID[wall[j:j+2], wall[j+1:]] = "B"
            walls.append((wall[j], wall[j+1]))
            w += 2

    print(GRID)
