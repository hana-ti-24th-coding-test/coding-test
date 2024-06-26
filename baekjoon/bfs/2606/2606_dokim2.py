# 백준 실버 3, 바이러스

import sys
from collections import deque


n = int(sys.stdin.readline())
computers = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

pairCnt = int(sys.stdin.readline())
for _ in range(pairCnt):
    a, b = map(int, sys.stdin.readline().split())
    computers[a].append(b)
    computers[b].append(a)

# for com in computers:
#     print(com)

cnt = 0

def bfs(start):
    global cnt
    q = deque()
    visited[start] = True
    q.append(start)

    while q:
        # print(q)
        now = q.popleft()
        for i in range(len(computers[now])):
            nxt = computers[now][i]
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                cnt += 1


bfs(1)
# for i in range(1, len(computers)):
#     if not visited[i]:
#         bfs(i)
#         cnt += 1

print(cnt)










