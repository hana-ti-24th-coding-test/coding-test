from collections import deque

n = int(input())
m = int(input())

# 그래프 초기화
com = [[] for _ in range(n+1)]

for _ in range(m):
    # 그래프 생성
    a, b = map(int, input().split())
    com[a].append(b)
    com[b].append(a)

# 방문 표시용 list
visited = [False]*(n+1)

# 큐
queue = deque([1])
cnt = 0

# bfs
while queue:
    x = queue.popleft()
    # 방문 표시
    visited[x] = True

    # 그래프 탐색
    for i in com[x]:
        # 미방문 노드 탐색
        if not visited[i]:
            visited[i] = True
            # 방문 예정 노드
            queue.append(i)
            cnt += 1

print(cnt)