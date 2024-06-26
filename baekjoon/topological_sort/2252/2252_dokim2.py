import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

def topologySort():
    q = deque()
    for i in range(1, len(indegree)):
        if indegree[i] == 0 and not visited[i]:
            q.append(i)
            visited[i] = True

    while q:
        now = q.popleft()
        print(now, end=" ")
        for nx in graph[now]:
            indegree[nx] -= 1
            if indegree[nx] == 0:
                q.append(nx)
                visited[nx] = True

topologySort()

