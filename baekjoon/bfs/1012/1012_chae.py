import sys
from collections import deque

# 이차원 배열의 상하좌우 탐색을 위해서 방향을 전환할 수 있는 배열을 만든다.
dx = [0, 1, 0, -1]  # 동남서북
dy = [1, 0 , -1, 0]

# 함수 정의
def bfs(graph, x, y):
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
                queue.append((nx, ny))
                graph[ny][nx] = 0


T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    # 인접 그래프가 아닌 인접 행렬을 사용, 좌표평면계를 만든다.
    # 주의!!! 가로 M, 세로 N일때 세로행먼저 선택하므로 x, y는 [y][x]가 된다!!!
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(K):
        a, b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1  # 배추 있음

    worms = 0 # 지렁이 수
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(graph, j, i)
                worms += 1
    print(worms)