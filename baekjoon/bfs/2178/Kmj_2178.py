import sys
from collections import deque


def bfs(i, j, graph, n, m):
    q = deque()
    q.appendleft((i, j))

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while q:
        x, y = q.pop()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if (nx <= 0 < n) and (0 <= ny < m) and graph[nx][ny] == 1:
                q.appendleft((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

    return graph[n-1][m-1]


def main():
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n)]

    for i in range(n):
        tmp = sys.stdin.readline().strip()
        for j in tmp:
            graph[i].append(int(j))

    print(bfs(0,0,graph,n,m))


if __name__ == '__main__':
    main()
