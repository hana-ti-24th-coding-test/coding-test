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
count = - 1

def bfs(graph, x, y):
    global count
    queue = deque([(x, y)])
    graph[y][x] = 0 # 방문처리
    while queue:
        x, y = queue.popleft()
        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 인덱스 범위를 넘어가면 다음 탐색을 한다.
            if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 1:
                if graph[N - 1][M - 1]:
                    queue.append((nx, ny))
                    graph[ny][nx] = 0
                    count += 1
                else:
                    break


for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            bfs(graph, j, i)

print(count)

