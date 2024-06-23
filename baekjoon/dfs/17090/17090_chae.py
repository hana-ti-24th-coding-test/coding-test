import sys
N, M = map(int, sys.stdin.readline().split())
maze = [list(sys.stdin.readline()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0
