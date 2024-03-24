# 풀이 참고

def dfs(start) :

    for i in graph[start] :
        if visited[i] == 0 :
            visited[i] = start
            dfs(i)


n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1) :
    x, y = map(int, input().split())
    graph[x] += [y]
    graph[y] += [x]

visited = [0] * (n+1)

dfs(1)

for j in range(2, n+1) :
    print(visited[j])