import sys

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x
def union_parent(parent, a, b):
    a = find(parent, a);
    b = find(parent, b);
    if a < b:
        parent[b] = a
    else:
        parent[a] = b