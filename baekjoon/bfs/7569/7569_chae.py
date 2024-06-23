from sys import stdin
from collections import deque
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
M, N, H = map(int, stdin.readline().split())
graph = [[list(map(int, stdin.readline().split())) for _ in range(N)] for _ in range(H)]
queue = deque()
answer = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append([i, j, k])


def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            # 인덱스가 탐색 범위 내이고 토마토가 안 익은 경우일때
            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and graph[nx][ny][nz] == 0:
                # 1로 만든다. 다음 탐색을 위해 큐에 삽입한다.
                graph[nx][ny][nz] = graph[x][y][z] + 1
                queue.append([nx, ny, nz])


bfs()
for i in graph:
    for j in i:
        # 안 익은 토마토가 있으면
        if 0 in j:
            # -1 출력
            print(-1)
            exit(0)  # 프로그램 종료 / 함수 만들어서 return하는 방법도 있음
        # 각 층(graph[i])에서 가장 큰 값을 찾고, 그것을 전체 최대값(answer)과 비교하여 업데이트
        answer = max(answer, max(j))
# max(j)는 1(처음 bfs 시작 조건)이므로 걸린 날짜는 -1을 해야 한다.
print(answer - 1)