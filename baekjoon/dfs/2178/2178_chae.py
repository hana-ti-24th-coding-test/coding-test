import sys

sys.setrecursionlimit(10**7)  # 재귀 깊이 설정

# 이차원 배열의 상하좌우 탐색을 위해서 방향을 전환할 수 있는 배열을 만든다.
dx = [0, 1, 0, -1]  # 동남서북
dy = [1, 0, -1, 0]

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]
for i in range(N):
    str_input = sys.stdin.readline().strip()
    for j in range(M):
        graph[i].append(int(str_input[j]))


def dfs(x, y, distance):
    if x == M - 1 and y == N - 1:
        return distance  # 도착점에 도달한 경우 현재까지의 거리 반환
    graph[y][x] = 0  # 방문한 위치 표시
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 1:
            # 인접한 노드를 방문하지 않았다면 재귀적으로 호출하여 깊이 우선 탐색 수행
            result = dfs(nx, ny, distance + 1)
            if result != -1:  # 도착점에 도달한 경우
                return result
    return -1  # 도착점에 도달하지 못한 경우


result = dfs(0, 0, 1)
print(result)
