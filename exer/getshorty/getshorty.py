import heapq
import sys
import math


def greedy_dijkstras(adjancyList, start, end):

    pq = [(start, -1)]

    sizes = {}

    for edge in range(end+1):
        sizes[edge] = math.inf
    sizes[start] = -1

    while pq:
        node = heapq.heappop(pq)[0]

        if node == end:
            return -sizes[end]

        for adjacent_node, adjacent_fraction in adjacencyList[node]:

            newDistance = sizes[node] * adjacent_fraction

            if newDistance < sizes[adjacent_node]:
                sizes[adjacent_node] = newDistance

                heapq.heappush(pq, (adjacent_node, newDistance))


sizes = []
while True:

    n, m = map(int, sys.stdin.readline().split())

    if n == 0 or m == 0:
        break

    adjacencyList = [[] for _ in range(n)]

    for edge in range(m):
        x, y, f = map(float, sys.stdin.readline().split())

        adjacencyList[int(x)].append((int(y), f))
        adjacencyList[int(y)].append((int(x), f))

    sizes.append(greedy_dijkstras(adjacencyList, 0, n-1))

for size in sizes:
    print(f"{size:.4f}")
