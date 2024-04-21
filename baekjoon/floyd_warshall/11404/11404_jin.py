INF = int(1e9)


n = int(input())
m = int(input())

g = [[INF] * (n+1) for _ in range(n+1)]     # 그래프를 무한으로 초기화

for _ in range(m) :
    a, b, c = map(int, input().split())
    if g[a][b] != INF :     # 노선이 하나가 아닌 경우
        g[a][b] = min(g[a][b], c)   # 비용이 더 작은 것으로 삽입
    else :
        g[a][b] = c         # a -> b 갈 때 비용 c

for a in range(1, n+1) :        # 이 코드 없이 삽입할 때 a != b인 위치에만 삽입할 수도 있음
    for b in range(1, n+1) :
        if a==b :           # 자기 자신으로 가는 노선
            g[a][b] = 0     # 0으로 초기화

for i in range(1, n+1) :            # 이미 방문한 노드를 거쳐 가도록 해야 하므로 가장 상위 for문
    for j in range(1, n+1) :
        for k in range(1, n+1) :
            g[j][k] = min(g[j][k], g[j][i] + g[i][k])       # 다른 노드를 거쳐서 가는 비용과 비교하여 최소를 결정


for i in range(1, n+1) :
    for j in range(1, n+1) :
        if g[i][j] == INF :
            print(0, end=" ")
        else :
            print(g[i][j], end=" ")
    print()