import sys
# 파이썬 재귀 제한 깊이 설정 -> 백준에서 걸림 ㄷㄷ;
sys.setrecursionlimit(10**6)


def dfs(graph, visited, i, result_list):
    visited[i] = 1
    for j in graph[i]:
        if visited[j] == 0:
            result_list[j] = i+1
            dfs(graph, visited, j, result_list)


def main():
    n = int(sys.stdin.readline())
    graph = [[] for _ in range(n)]
    visited = [0 for _ in range(n)]
    result_list = [0 for _ in range(n)]

    for i in range(n - 1):
        a, b = map(int, sys.stdin.readline().strip().split())
        # 아래와 기존에 했던 대칭 그래프 사용 시 메모리 초과... 아래처럼 표현 가능
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    dfs(graph, visited, 0, result_list)

    for i in range(1, n):
        print(result_list[i])


if __name__ == '__main__':
    main()
