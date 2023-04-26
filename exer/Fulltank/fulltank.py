import sys


def getlines(x):
    return [[*map(int, input().split())] for _ in range(x)]


# def solve(shortest_paths, edges, gas_prices):

#     for i in range(n):

#     return 0


n, m = map(int, sys.stdin.readline().split())

gas_prices = [*map(int, sys.stdin.readline().split())]

edges = getlines(n)
edges.sort(key=lambda x: x[0])

q = int(sys.stdin.readline())

queries = getlines(q)

graph = [[] for _ in range(n)]

for u, v, c in edges:
    graph[u].append((v, c))


for querie in queries:
    Hmap = {}
    # price = solve(Hmap, edges, gas_prices,n)
