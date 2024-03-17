import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(i, j):
    q = deque()
    q.append([i, j])
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = True
    return



t = int(sys.stdin.readline())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    board = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        y, x = map(int, sys.stdin.readline().split())
        # print(x, y)
        board[x][y] = 1

    # for b in board:
    #     print(b)

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)
