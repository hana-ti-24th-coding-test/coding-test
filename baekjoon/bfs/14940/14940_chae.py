import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            queue.append((i, j))
            visited[i][j] = 0
        elif graph[i][j] == 0:
            visited[i][j] = 0  # 갈 수 없는 땅은 0으로 설정


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 탐색 범위 안이고 갈 수 있는 땅일때
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and graph[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))


bfs()
for i in visited:
    for j in i:
        print(j, end=" ")
    print()
