import sys

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


def dfs(now):
    global cnt
    print(now)
    print(visited[1:])
    for nx in computers[now]:
        if not visited[nx]:
            visited[nx] = True
            cnt += 1
            dfs(nx)


visited[1] = True
dfs(1)
print("cnt:", cnt)
