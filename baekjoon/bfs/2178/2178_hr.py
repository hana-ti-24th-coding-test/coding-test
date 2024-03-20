import sys
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
dir = [[1, 0], [-1, 0], [0, -1], [0, 1]] # 상하좌우
visited = [[False] * M for _ in range(N)]


def bfs(startR, startC):
    queue = deque()
    # 시작노드 큐에 추가후 방문처리
    queue.append((startR, startC, 1)) # 가로, 세로, 이동 수
    visited[startR][startC] = True

    while queue:
        r, c, d = queue.popleft() # 큐의 제일 상단에 있는 값 pop

        if r == N-1 and c == M-1: # 만약 미로의 끝에 도달 했다면 이동 수 출력
            print(d)
            break

        for i in range(4):
            nr = r + dir[i][0]
            nc = c + dir[i][1]

            if nr < 0 or nr > N-1 or nc < 0 or nc > M-1: continue
            if visited[nr][nc] == True: continue
            if graph[nr][nc] == 0: continue

            # 상하좌우로 이동 후의 가로, 세로, 이동 수 큐에 추가 후 방문처리
            queue.append((nr, nc, d+1))
            visited[nr][nc] = True


bfs(0, 0)