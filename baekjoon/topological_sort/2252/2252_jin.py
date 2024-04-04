from collections import deque

def topology() :
    result = []
    q = deque()

    for i in range(1, n+1) :    # 진입차수 0인 노드로 큐 초기화
        if indegree[i] == 0 :
            q.append(i)

    while q :
        now = q.popleft()
        result.append(now)

        for i in graph[now] :   # 현재 노드와 연결된 모든 노드 순회
            indegree[i] -= 1    # 진입차수 하나씩 제거
            if indegree[i] == 0 :
                q.append(i)

    for i in result :
        print(i, end = ' ')


n, m = map(int, input().split())

indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m) :
    a, b = map(int, input().split())

    graph[a].append(b)
    indegree[b] += 1


topology()
