import sys
sys.setrecursionlimit(10 ** 5) #재귀깊이를 수정하지 않으면 런타임 에러 발생

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0

def dfs(start):
    visited[start] = True # 정점 start와 연결되어 있는 모든 정점 방문처리

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

for i in range(1, N+1):
    if not visited[i]: # 방문되지 않은 정점이라면 연결되지 않은 것이라 파악 해 count + 1, 해당 정점과 연결된 정점들 방문 처리
        dfs(i)
        count += 1

print(count)

