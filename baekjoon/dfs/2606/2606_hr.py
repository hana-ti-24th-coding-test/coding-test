import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)

count = 0
def dfs(start):
    global count
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            count += 1
            dfs(i)


dfs(1)
print(count)