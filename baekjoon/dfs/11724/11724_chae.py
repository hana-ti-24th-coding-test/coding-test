import sys
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (N + 1)
connected = 0

def dfs(graph, start, visited):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


for i in range(1, N + 1):
    if not visited[i]:
        dfs(graph, i, visited)
        connected += 1

print(connected)