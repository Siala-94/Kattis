import heapq
import sys


n = int(sys.stdin.readline())
items = [*(map(int, input().split()))]
m = int(sys.stdin.readline())

adj = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, d = map(int, input().split())
    adj[a].append((b, d))
    adj[b].append((a, d))


dist = [float('inf')] * n
max_items = [0] * n
pq = [(0, 0, 0)]  # distance, location, max_items

while pq:
    d, u, items_picked = heapq.heappop(pq)
    if u == n:
        print(d, max_items[n-1])
        break
    if d > dist[u]:  # already processed this node with a shorter path
        continue

    dist[u] = d
    max_items[u] = items_picked
    for v, w in adj[u]:
        if d + w < dist[v]:
            heapq.heappush(pq, (d+w, v, max(items_picked, items[v])))
        else:
            print("impossible")
