import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (N + 1)
connected = 0 # 연결 요소의 개수


# bfs 함수 정의
def bfs(graph, start, visited):
    global connected
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


def dfs(graph, start, visited):
    global connected
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


# bfs 함수가 한 번 끝마칠 때마다 1 더하기
for i in range(1, N + 1):
    if not visited[i]:
        bfs(graph, i, visited)
        dfs(graph, i, visited)
        connected += 1


print(connected)