def lcs(x, y) :
    x, y = [' '] + x, [' '] + y
    n, m = len(x), len(y)
    c = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(1, n) :
        for j in range(1, m) :
            if x[i] == y[j] :
                c[i][j] = c[i-1][j-1] +1
            else :
                c[i][j] = max(c[i][j-1], c[i-1][j])
    return c[i][j]

x = list(input())
y = list(input())

print(lcs(x, y))