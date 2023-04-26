import sys
import math
import heapq


def euclidean_distance(x1, x2, y1, y2):

    return math.sqrt((x1-x2) ** 2 + (y1 - y2) ** 2)


def prim(points):

    total_distance = 0.0
    # first point is first in points with distance 0
    frontier = [(0.0, 0)]
    heapq.heapify(frontier)

    # setup unordered map of indexes in points
    points_indexes = set(range(len(points)))
    # unordered map of visited points
    visited = set()

    # we rech end when heap is empty or we have n-1 vertexes in visited
    while frontier and len(visited) < len(points):

        distance, i = heapq.heappop(frontier)

        if i not in visited:
            total_distance += distance
            visited.add(i)
            points_indexes.remove(i)
            x1, y1 = points[i]

            for j in points_indexes:
                x2, y2 = points[j]
                heapq.heappush(
                    frontier, (euclidean_distance(x1, x2, y1, y2), j))
    return total_distance


# read n
n = int(sys.stdin.readline())
result = []
# iterate through testcases
for test in range(n):

    # we add each point to our list of points
    points = []
    m = int(sys.stdin.readline())

    for point in range(m):
        x, y = map(float, sys.stdin.readline().split())
        points.append((x, y))

    # solve using prims algorithm
    result.append(prim(points))

for res in result:
    print(res)
