import sys
sys.setrecursionlimit(10 ** 5)

def dfs(i, j, graph, n, m):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for a in range(4):
        nx = i + dx[a]
        ny = j + dy[a]
        if ( 0 <= nx  < n) and (0 <= ny < m) and graph[nx][ny] == 1:
            graph[nx][ny] = graph[i][j] + 1
            dfs(nx, ny, graph, n, m)
    return graph[n-1][m-1]



def main():
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n)]
    sol = 0
    for i in range(n):
        tmp = sys.stdin.readline().strip()
        for j in tmp:
            graph[i].append(int(j))

    for i in range(n):
        for j in range(m):
            sol = dfs(i, j, graph, n, m)

    print(sol)



if __name__ == '__main__':
    main()
