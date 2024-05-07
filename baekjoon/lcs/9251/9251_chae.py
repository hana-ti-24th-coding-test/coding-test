# import sys
# x = sys.stdin.readline()
# y = sys.stdin.readline()
x = list(input())
y = list(input())


def lcs(x, y):
    m, n = len(x), len(y)
    if m == 0 or n == 0:
        return 0
    else:
        if x[-1] == y[-1]:
            return lcs(x[:(m - 1)], y[:(n - 1)]) + 1
        else:
            return max(lcs(x[:m], y[:n - 1]), lcs(x[:(m - 1)], y[:n]))


print(lcs(x, y))


def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print()


def lcs(x, y):
    x, y = [' '] + x, [' '] + y
    m, n = len(x), len(y)
    c = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if x[i] == y[j]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i][j - 1], c[i - 1][j])
    return c


# x = list(input())
# y = list(input())
print_matrix(lcs(x, y))