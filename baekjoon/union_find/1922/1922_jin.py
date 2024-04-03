def find_parent(parent, x) :  # 특정 원소가 속한 집합 찾기
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b) :    # 두 원소가 속한 집합 찾기
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

n = int(input())
m = int(input())
parent = [0] * (n + 1)

edges = []
result = 0

for i in range(1, n+1) :
    parent[i] = i

for _ in range(m) :
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))  # 비용순 정렬 위해 튜플 사용

edges.sort()                    # 최대 가중치일 경우 내림차순 정렬

for edge in edges :
    cost, a, b = edge
    # 사이클 발생 확인
    if find_parent(parent, a) != find_parent(parent, b) :
        union_parent(parent, a, b)
        result += cost

print(result)
