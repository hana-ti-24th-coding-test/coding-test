import sys
from collections import deque
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([c, b])
s, e = map(int, sys.stdin.readline().split())
result = [int(10e9)] * (n + 1)
print(result)
for g in graph:
    print(g)

def dijkstra(s):
    q = []
    heapq.heappush(q, [0, s])
    result[s] = 0
    while q:
        cost, now = heapq.heappop(q)
        if cost > result[now]:
            continue
        for weight, nx in graph[now]:
            newCost = result[now] + weight
            if newCost < result[nx]:
                result[nx] = newCost
                heapq.heappush(q, [newCost, nx])


dijkstra(s)
print(result[e])