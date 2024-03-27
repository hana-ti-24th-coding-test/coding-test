def dfs(start) :
    if start >= len(visited) :  # 노드 개수 넘어갈 시
        return
    if sum(visited) == len(visited)-1 :
        return

    visited[start] = 1

    for i in graph[start] :
        if visited[i] == 0 :
            dfs(i)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m) :
    u, v = map(int, input().split())
    graph[u] += [v]
    graph[v] += [u]     # 양방향 연결

visited = [0] * (n+1)
global conn
conn = 0

for i in range(1, n+1) :
    if visited[i] == 0 :
        dfs(i)
        conn += 1   # 연결이 한 번 끊기면 연결요소 개수 추가

print(conn)

