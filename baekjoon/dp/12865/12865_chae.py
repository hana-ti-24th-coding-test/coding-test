import sys
N, K = map(int, sys.stdin.readline().split())
stuff = [[0, 0]]  # 1번 인덱스부터 실제 물건 정보를 저장하기 위해 0번을 0으로 채워준다.
backpack = [[0] * (K + 1) for _ in range(N + 1)]  # i번째 물건까지 고려했을 때 무게 j이하의 배낭에 담을 수 있는 최대 가치를 저장

for i in range(N):
    stuff.append(list(map(int, sys.stdin.readline().split())))
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight, value = stuff[i][0], stuff[i][1]
        if j < weight:  # 배낭의 무게가 현재 물건의 무게보다 작으면 현재 물건을 담을 수 없으므로
            backpack[i][j] = backpack[i - 1][j]  # backpack[i][j]는 이전 물건까지 고려했을 때의 최대 값(backpack[i - 1][j])을 저장
        else:
            # 현재 물건을 담는 경우와 담지 않는 경우를 비교하여 더 큰 값을 선택
            backpack[i][j] = max(value + backpack[i - 1][j - weight], backpack[i - 1][j])
print(backpack[N][K])
