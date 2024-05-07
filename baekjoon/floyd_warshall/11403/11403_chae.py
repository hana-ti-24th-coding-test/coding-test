import sys
INF = int(1e9)
N = int(sys.stdin.readline())
# # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
# graph = [[INF] * (N + 1) for _ in range(N + 1)]
# # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
# for a in range(1, N + 1):
#     for b in range(1, N + 1):
#         if a == b:
#             graph[a][b] = 0
# # 각 간선에 대한 정보를 입력받아 그 값으로 초기화
# for _ in range(N):
#     a, b, cost = map(int, sys.stdin.readline().split())
#     graph[a][b] = cost
# # 점화식에 따라 플로이드 워셜 알고리즘 수행
# for k in range(1, N + 1):
#     for a in range(1, N + 1):
#         for b in range(1, N + 1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
# for a in range(1, N + 1):
#     for b in range(1, N + 1):
#         if graph[a][b] == INF:
#             print(0, end=" ")
#         else:
#             print(graph[a][b], end=" ")
#     print()
graph = []
for _ in range(N):
    input = list(map(int, sys.stdin.readline().replace('0', str(INF)).split()))
    graph.append(input)
# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
for a in range(N):
    for b in range(N):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()
