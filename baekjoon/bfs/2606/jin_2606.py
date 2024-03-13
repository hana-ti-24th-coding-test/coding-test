# 백준 2606 바이러스

def dfs(v):
    visited[v] = 1  # 노드 방문 처리
    for a in g[v] : # 연결 노드 탐색
        if visited[a] == 0 :    # 방문하지 않았으면
            dfs(a)  # 이 노드로 연결 노드 탐색 반복
        # 방문했다면 다음 노드로 for문 돌기


n = int(input())
m = int(input())
g = [[] for _ in range(n+1)]    # 그래프 초기화(n개)

visited = [0]*(n+1) # 방문하지 않을 경우 0

for _ in range(m) :
    x, y = map(int, input().split())
    g[x] += [y]     # x번째 행에 y 추가 = x번 컴퓨터에 y번 연결
    g[y] += [x]     # y번째 행에 x 추가 = 양방향 연결

dfs(1)

print(sum(visited)-1)
