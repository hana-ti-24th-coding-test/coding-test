import sys
sys.setrecursionlimit(10**5)

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(u, graph):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v, graph)

count = 0

for i in range(1, n+1):
    if not visited[i]:
        dfs(i, graph)
        count += 1

print(count)