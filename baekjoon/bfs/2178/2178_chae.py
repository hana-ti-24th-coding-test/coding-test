import sys
from collections import deque

# 이차원 배열의 상하좌우 탐색을 위해서 방향을 전환할 수 있는 배열을 만든다.
dx = [0, 1, 0, -1]  # 동남서북
dy = [1, 0 , -1, 0]

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]
for i in range(N):
    str = sys.stdin.readline().strip()
    for j in range(M):
        graph[i].append(int(str[j]))

def bfs(graph):
    queue = deque([(0, 0, 1)])  # 시작점에서 시작하고 거리를 함께 저장
    graph[0][0] = 0  # 시작점 방문처리
    while queue:
        x, y, distance = queue.popleft()
        # 도착점에 도달했을 때
        if x == M - 1 and y == N - 1:
            return distance  # 현재까지의 거리 반환
        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 인덱스 범위를 넘어가면 다음 탐색을 한다.
            if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 1:
                queue.append((nx, ny, distance + 1))  # 다음 위치와 거리를 큐에 추가
                graph[ny][nx] = 0  # 방문처리
    return -1  # 도착점에 도달하지 못했을 때


result = bfs(graph)
print(result)
