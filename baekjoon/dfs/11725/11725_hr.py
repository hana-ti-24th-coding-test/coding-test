import sys
sys.setrecursionlimit(10 ** 8)

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
parent = [0] * (N+1)

for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    for i in graph[node]:
        if parent[i] == 0:
            parent[i] = node; # 자신의 부모노드를 탐색이 시작한 값으로 넣어줌
            dfs(i)

dfs(1)

for i in range(2, N+1):
    print(parent[i])


