import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

parent = [0] * (N+1)

edges = []
result = 0

for i in range(1, N+1):
    parent[i] = i

def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)

    if a < b:
        parent[b] = a
    else :
        parent[a] = b

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge

    if findParent(parent, a) != findParent(parent, b):
        unionParent(parent, a, b)
        result += cost

print(result)