import sys
from collections import deque

# 이차원 배열의 상하좌우 탐색을 위해서 방향을 전환할 수 있는 배열을 만든다.
dx = [0, 1, 0, -1]  # 동남서북
dy = [1, 0 , -1, 0]

# 함수 정의
def bfs(graph, x, y):
    queue = deque((x, y))
    graph[x][y] = 0 #방문처리
    while queue:
        x, y = queue.popleft()
        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 인덱스 범위를 넘어가면 다음 탐색을 한다.
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny]:
                queue.append((nx, ny))
                graph[nx][ny] = 0


T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    # 인접 그래프가 아닌 인접 행렬을 사용, 좌표평면계를 만든다.
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(K):
        a, b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1  #배추 있음

    worms = 0 # 지렁이 수
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(a, b)
                worms += 1
    print(worms)


