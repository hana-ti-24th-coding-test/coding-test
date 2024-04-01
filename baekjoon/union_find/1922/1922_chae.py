import sys

#  모든 컴퓨터를 연결하는데 필요한 최소비용 => 최소 신장 트리
# 노드와 간선(Union 연산)의 개수 입력받기
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
# 간선을 담을 리스트
edges = []
for i in range(M):
    A, B, cost = map(int, sys.stdin.readline().split())
    # 비용 순으로 정렬하기 위해 cost를 첫번째 원소로 하는 튜플 생성
    edges.append((cost, A, B))
# 비용 순으로 오름차순 정렬
edges.sort()
# 최종 비용
result = 0
# 부모 노드 초기화
parent = [0] * (N + 1)
# 부모를 자기 자신으로 초기화
for i in range(1, N + 1):
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

print(result)
