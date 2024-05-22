import sys
import heapq
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
INF = int(1e9) # 무한을 의미하는 값

graph = [[] for i in range(N + 1)]
# 방문체크
visited = [False] * (N + 1)
# 최단 거리 테이블을 무한으로 초기화
distance = [INF] * (N + 1)
for _ in range(M):
    a, b, cost = map(int, sys.stdin.readline().split())
    # a번 노드에서 b번 노드까지 가는 비용이 cost라는 의미
    graph[a].append((b, cost))

start, end = map(int, sys.stdin.readline().split())


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
    # distance[start] = 0
    # visited[start] = True
    # for j in graph[start]:
    #     distance[j[0]] = j[1]
    # for i in range(N - 1):
    #     now = get_smallest_node()
    #     visited[now] = True
    #     for j in graph[now]:
    #         min_cost = distance[now] + j[i]
    #         if min_cost < distance[j[0]]:
    #             distance[j[0]] = min_cost
    q = []
    # 시작 노드로 가기 위한 최단거리는 0으로 설정하며, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                # cost, i[0] 순으로 오름차순 정렬을 해야 한다.
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

# for i in range(1, N + 1):
#     if distance[i] == INF:
#         print("INFINITY")
#     else:

print(distance[end])



# list = [[2,99],[99,3],[5,2],[1,2],[3,4],[99,66],[98,67]]
#
#
# list.sort(key=lambda x:([x[0],x[1]]))
# print(list)
