import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(u, graph, visited):
    for v in graph[u]:
        if visited[v] == None:
            visited[v] = u
            dfs(v, graph, visited)

visited = [None] * (n+1)
dfs(1, graph, visited)

for i in range(2, n+1):
    print(visited[i])