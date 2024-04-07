import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
INF = int(1e9) # 무한을 의미하는 값

graph = [[] for i in range(N + 1)]
# 방문체크
visited = [False] * (N + 1)
# 최단 거리 테이블을 무한으로 초기화
distance = [INF] * (N + 1)
for _ in range(M):
    a, b, cost = map(int, sys.stdin.readline())
    # a번 노드에서 b번 노드까지 가는 비용이 cost라는 의미
    graph[a].append((b, cost))

start, end = map(int, sys.stdin.readline())


# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, N + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


# 다익스트라
def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(N - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            min_cost = distance[now] + j[i]
            if min_cost < distance[j[0]]:
                distance[j[0]] = min_cost


dijkstra(start)

for i in range(1, N + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

