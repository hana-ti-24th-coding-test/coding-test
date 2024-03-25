import sys


def dfs(graph, visited, i):
    visited[i] = 1
    for idx, value in enumerate(graph[i]):
        if visited[idx] == 0 and value == 1:
            dfs(graph, visited, idx)


def main():
    n, m = map(int, sys.stdin.readline().split())
    graph = [[0 for _ in range(n)] for _ in range(n)]
    visited = [0 for _ in range(n)]

    cnt = 0

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a - 1][b - 1] = 1
        graph[b - 1][a - 1] = 1

    for i in range(n):
            if visited[i] == 0:
                dfs(graph, visited, i)
                cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
