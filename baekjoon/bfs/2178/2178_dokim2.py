
import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# def bfs(i, j):
#     q = deque()
#     q.append([i, j])
#     visited[i][j] = 1
#     while q:
#         x, y = q.popleft()
#         for d in range(4):
#             nx, ny = x + dx[d], y + dy[d]
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and board[nx][ny] == 1:
#                 q.append([nx, ny])
#                 visited[nx][ny] = visited[x][y] + 1
#     return

def dfs(x, y, visited):
    global answer
    if x == n - 1 and y == m - 1:
        answer = min(answer, visited[-1][-1])
        return

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and board[nx][ny] == 1:
            visited[nx][ny] = visited[x][y] + 1
            dfs(nx, ny, visited)
            visited[nx][ny] = 0


n, m = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int,sys.stdin.readline().rstrip())))
visited = [[0] * m for _ in range(n)]
# bfs(0, 0)
# print(visited[-1][-1])

answer = int(10e9)
visited[0][0] = 1
dfs(0, 0, visited)
print(answer)