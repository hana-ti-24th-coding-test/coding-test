import sys
sys.setrecursionlimit(int(10e7))

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(v, visited):
    for e in graph[v]:
        if not visited[e]:
            visited[e] = True
            dfs(e, visited)


cnt = 0
for j in range(1, n + 1):
    if not visited[j]:
        dfs(j, visited)
        cnt += 1

print(cnt)
