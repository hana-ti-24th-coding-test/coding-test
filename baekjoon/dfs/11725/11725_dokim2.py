import sys
sys.setrecursionlimit(10**6)
from collections import deque

n = int(input())
board = [[] for _ in range(n+1)]
visited = [0] * (n + 1)
for _ in range(n - 1):
    v1, v2 = map(int, sys.stdin.readline().split())
    board[v1].append(v2)
    board[v2].append(v1)


def dfs(s):
    for i in board[s]:
        if visited[i] == 0:
            visited[i] = s
            dfs(i)

dfs(1)

for x in range(2, n+1):
    print(visited[x])

'''
            1
        6       4
    3         2     7
5
'''