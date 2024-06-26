# import sys
#
# v = int(sys.stdin.readline())
# e = int(sys.stdin.readline())
# board = [[] for _ in range(v + 1)]
# connections = []
# for _ in range(e):
#     a, b, c = map(int, sys.stdin.readline().split())
#     connections.append([a, b, c])
#
# connections.sort(key=lambda x: x[2])
# print(connections)
# parent = [i for i in range(v + 1)]
# print(parent)
#
#
# def find_parent(parent, x):
#     if x == parent[x]:
#         return x
#     parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
#
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
#
# cost = 0
# for a, b, c in connections:
#     if find_parent(parent, a) != find_parent(parent, b):
#         print(parent)
#         print(a, b, c)
#         union_parent(parent, a, b)
#         cost += c
# # print(parent)
# print(cost)

import sys
def find_parent(parent, x):
    # if x == parent[x]:
    #     return x
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    elif b < a:
        parent[a] = b


v, e = map(int, sys.stdin.readline().split())
parent = [i for i in range(v + 1)]
lines = []
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    lines.append([a, b, c])
lines.sort(key=lambda x: [x[2]])
answer = 0
for a, b, c in lines:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += c
print(answer)
