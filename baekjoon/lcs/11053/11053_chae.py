import sys
N = int(sys.stdin.readline())
numbers = [0] + list(map(int, sys.stdin.readline().split()))
# dp테이블 생성 및 초기화
dp = [0] * (N + 1)
for i in range(1, N + 1):
    maxx = 0
    for j in range(0, i):  # 0~i-1 중 최대값
        if numbers[i] > numbers[j]:
            maxx = max(maxx, dp[j])
    dp[i] = maxx + 1
# 중간에 최대값 있을 수 있으므로 max로 최대값 찾는다.
print(max(dp))
