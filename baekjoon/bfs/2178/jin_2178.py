# bfs
# 백준 2178 미로찾기

from collections import deque

def bfs(x, y) :
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4):  # 상하좌우
            # 이동할 x, y 좌표
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간 벗어난 경우 무시    => 항상 사용하는 게 좋음 (오류 방지)
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1     # 누적 거리에 1 더하여
                queue.append((nx, ny))  # 현재 좌표 갱신

    return graph[n - 1][m - 1]


n, m = map(int, input().split(' '))

graph = []
for i in range(n) :
    graph.append(list(map(int, input())))

# 이동할 방향 정의     => 유용하게 쓰인다!
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 동, 서, 남, 북, 북동, 북서, 남동, 남서
# dx = [0, 0, 1, -1, 1, 1, -1, -1]
# dy = [1, -1, 0, 0, 1, -1, 1, -1]

print(bfs(0, 0))


# cf) 주어진 맵을 변경하지 않고 하는 법!
# visited[x][y] = True
# if graph[nx][ny] == 1 and visited[nx][ny] == 0 :
#       visited[nx][ny] = visited[x][y] + 1