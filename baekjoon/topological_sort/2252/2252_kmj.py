import sys
from collections import deque


def topology_sort(indegree, graph, result, n):
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0: q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)


def main():
    n, m = map(int, sys.stdin.readline().split())
    indegree = [0] * (n + 1)
    result = []
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        indegree[b] += 1

    topology_sort(indegree, graph, result, n)

    for a in result:
        print(a, end=' ')


if __name__ == '__main__':
    main()
