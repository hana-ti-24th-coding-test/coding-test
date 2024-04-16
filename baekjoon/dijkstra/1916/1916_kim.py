import sys
import heapq

def dijkstra(src):
    q = []
    heapq.heappush(q, (0, src))
    distance[src] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 이미 처리된 적 있는 노드는 무시
        if distance[now] < dist:
            continue
        for a in graph[now]:
            cost = dist + a[1]
            if cost < distance[a[0]]:
                distance[a[0]] = cost
                heapq.heappush(q, (cost, a[0]))


INF = 1e9

# 도시 개수
n = int(sys.stdin.readline())

# 버스 개수
m = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
distance = [INF for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

x, y = map(int, sys.stdin.readline().split())
dijkstra(x)

print(distance[y])


