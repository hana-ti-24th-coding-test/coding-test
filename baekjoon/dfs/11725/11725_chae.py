import sys
<<<<<<< HEAD
sys.setrecursionlimit(10**8)
=======
sys.setrecursionlimit(10**6)

>>>>>>> d3947c3 (feat: add 11724, 11725)
N = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]  # 양방향 그래프
for i in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (N + 1)
nodes = [0] * (N + 1)  # 부모 노드를 저장할 리스트


def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            nodes[i] = start  # 현재 노드의 부모를 저장
            dfs(i)


dfs(1)  # 루트가 1
for i in range(2, N + 1):  # 2번 노트부터 출력
    print(nodes[i])
