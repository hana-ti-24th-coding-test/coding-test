import sys
N = int(sys.stdin.readline())
A = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0] * (N + 1)
for i in range(1, N + 1):
    maxx = 0
    for j in range(i):
        if A[i] > A[j]:
            maxx = max(maxx, dp[j])
    dp[i] = maxx + 1
    # print(dp)
print(max(dp))



