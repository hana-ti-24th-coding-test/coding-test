import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

miro = []

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for _ in range(n):
    miro.append(list(map(int, sys.stdin.readline().rstrip())))

route = [[0 for _ in range(m)] for _ in range(n)]
queue = deque([(0, 0)])

route[0][0] = 1

while queue:
    x, y = queue.popleft()
    for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0 <= nx < n) and (0 <= ny < m) and (miro[nx][ny] == 1) and (route[nx][ny] == 0):
                route[nx][ny] = route[x][y] + 1
                queue.append((nx, ny))
            else:
                continue


print(route[-1][-1])