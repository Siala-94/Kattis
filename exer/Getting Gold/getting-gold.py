import sys
import numpy as np


Action_Queue = []
W, H = sys.stdin.readline().split()
GRID = np.empty(shape=(int(H), int(W)), dtype=str)


def read():

    sp = ()
    for i in range(int(H)):
        line = sys.stdin.readline()
        line = list(line)
        line.pop()

        j = 0
        for l in line:
            if l == "P":
                sp = (i, j)
            GRID[i, j] = l
            j += 1
    return sp


def Trap(pos):
    return GRID[pos[0], pos[1]] == "T"


def addable(pos):
    if GRID[pos[0], pos[1]] == "#" or GRID[pos[0], pos[1]] == "V":
        return False
    else:

        return False if pos in Action_Queue else True


def expand(current_point):

    right = (current_point[0], current_point[1]+1)
    left = (current_point[0], current_point[1]-1)
    down = (current_point[0]+1, current_point[1])
    up = (current_point[0]-1, current_point[1])

    if Trap(right) == False and Trap(left) == False and Trap(down) == False and Trap(up) == False:
        if addable(right):
            Action_Queue.append(right)
        if addable(left):
            Action_Queue.append(left)
        if addable(down):
            Action_Queue.append(down)
        if addable(up):
            Action_Queue.append(up)


def solve(starting_point):
    gold = 0
    current_point = starting_point

    GRID[current_point[0], current_point[1]] = "V"
    expand(current_point)

    while Action_Queue:
        current_point = Action_Queue.pop(0)

        if GRID[current_point[0], current_point[1]] == "G":
            gold += 1

        GRID[current_point[0], current_point[1]] = "V"
        expand(current_point)

    return gold


sp = read()


amount = solve(sp)
print(GRID, amount)
