import sys
import time
import heapq
import random
# start = time.time()


def fill_txt():
    v = []
    file = "scratch.txt"
    with open(file) as f:
        lines = f.readlines()

    n = int(lines[0])

    for i in range(n + 1):
        val = int(lines[i])
        v.append(val)
    v.pop(0)

    return v, n


def test():
    v = []
    n = 10
    for i in range(n):
        val = random.randint(1, n)
        v.append(val)
    v[-1] = n+1
    return v, n


def fill_std():
    n = int(sys.stdin.readline())
    for i in range(n):
        v.append(int(sys.stdin.readline()))
    return v, n


def edge_cases(v, n):

    if v[-1] != n+1:
        return True
    if n < 2:
        return True
    return False


def fill(v):
    l = [0]*(len(v)+1)
    q = []

    for e in v:
        l[e-1] += 1
    for i in range(len(v)+1):
        if l[i] == 0:
            q.append(i+1)
    heapq.heapify(q)
    return l, q


n = int
v = []

# v,n = test()
v, n = fill_txt()
# v, n = fill_std()

u = [None] * n
end = False

end = edge_cases(v, n)

if end:
    print("Error")
else:
    l, HQ = fill(v)

    for i in range(n):
        index = v[i] - 1
        val = heapq.heappop(HQ)
        u[i] = val
        if i != n:
            l[index] -= 1
            if l[index] == 0:
                heapq.heappush(HQ, v[i])

    sys.stdout = open(1, "w", buffering=100000)
    print("\n".join([str(s) for s in u]))

    # print("-----%s seconds -----", (time.time() - start))
