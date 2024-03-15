import sys

T = int(sys.stdin.readline())
M, N, K = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(M)] for _ in range(N)]
for i in range(K):
    a, b = map(int, sys.stdin.readline().split())
    graph[b][a] = 1

