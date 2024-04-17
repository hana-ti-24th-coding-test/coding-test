import sys

# 최소 신장 트리 : 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리
# 노드와 간선(Union 연산)의 개수 입력받기
V, E = map(int, sys.stdin.readline().split())
# 간선을 담을 리스트
edges = []
for i in range(E):
    # 비용 순으로 정렬하기 위해 cost를 첫번째 원소로 하는 튜플 생성
    A, B, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, A, B))
# 비용 순으로 오름차순 정렬
edges.sort()
# 최종 비용
result = 0
# 가장 긴 간선 제거할 수 있음
last_edge = 0
# 부모 노드 초기화
parent = [0] * (V + 1)
# 부모를 자기 자신으로 초기화
for i in range(1, V + 1):
    parent[i] = i


# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 간선을 하나씩 확인하며
for edge in edges:
    # cost, A, B 세 개의 변수에 순서대로 할당
    cost, A, B = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, A) != find_parent(parent, B):
        union_parent(parent, A, B)
        result += cost
        # 가장 긴 간선을 제거한다.
        last_edge = cost

print(result - last_edge)