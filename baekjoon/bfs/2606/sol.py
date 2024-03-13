from collections import deque
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    # 양방향 그래프(인접리스트)
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, len(graph)):
    graph[i].sort()  # 1번 노드부터 정렬
visited = [False] * (n + 1)
infected = []  # 총 방문한(감염된) 노드를 담을 리스트


def BFS(graph, start, visited):
    # bfs는 queue 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌때까지 반복
    while queue:
        # 큐에 가장 먼저 들어온 노드 뽑기
        v = queue.popleft()
        # 먼저 들어온 노드의 방문 여부 확인
        for i in graph[v]:
            if not visited[i]:
                # 아직 방문하지 않은 노드를 큐에 넣기
                queue.append(i)
                # 큐에 넣었다면 방문 처리 해주기
                visited[i] = True
                # 감염된 노드 리스트에 추가
                infected.append(i)


def DFS(graph, start, visited):
    visited[start] = True
    for i in graph[start]:
        # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        if not visited[i]:
            DFS(graph, i, visited)
            infected.append(i)


BFS(graph, 1, visited)
# DFS(graph, 1, visited)
print(len(infected))