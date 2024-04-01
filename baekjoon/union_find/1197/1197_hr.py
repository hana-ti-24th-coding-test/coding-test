import sys

V, E = map(int, sys.stdin.readline().split()) #노드, 간선 개수

parent = [0] * (V+1)

edges = []
result = 0

for i in range(1, V+1): #부모 노드 자기 자신으로 초기화
    parent[i] = i

def findParent(parent, x):
    if(parent[x] != x): #자기 자신이 루트 노드가 아니라면
        parent[x] = findParent(parent, parent[x]) #재귀함수를 통해 루트노드르 찾음
    return parent[x]

def unionParent(parent, a, b): #각 노드가 속한 집합 합치기
    a = findParent(parent, a)
    b = findParent(parent, b)

    #두 노드 중 작은 값으로 부모 노드 설정
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split()) #A노드, B노드, 간선의 가중치
    edges.append((C, A, B)) #가중치인 C를 제일 먼저 써서 정렬 기준을 C로 만듬

edges.sort()

for edge in edges:
    cost, a, b = edge

    if(findParent(parent, a) != findParent(parent, b)): #두 노드가 같은 집합이 아니라면
        unionParent(parent, a, b) #합쳐줌
        result += cost

print(result)





