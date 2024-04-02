from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())  # N : 노드(총 학생 수) , M : 간선(비교결과는 연결정보)
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (N + 1)
# 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(N + 1)]
for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    # A가 B의 앞에 서야 한다는 의미 -> 정점 A에서 B로 이동 가능
    graph[A].append(B)
    # 진입 차수 1 증가
    indegree[B] += 1


# 위상 정렬 함수
def topological_sort():
    # 알고리즘 수행 결과를 담을 리스트
    result = []
    queue = deque()
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
    # 큐가 빌 때까지 반복
    while queue:
         # 큐에서 원소 꺼내기
         now = queue.popleft()
         result.append(now)
         # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
         for i in graph[now]:
             indegree[i] -= 1
             # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
             if indegree[i] == 0:
                 queue.append(i)
    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')

topological_sort()

