n = int(input())
a = list(map(int, input().split()))

res = [1 for _ in range(n)]

for i in range(n) :
    for j in range(i) :
        if (a[j] < a[i]) :
            res[i] = max(res[i], res[j]+1)

print(max(res))