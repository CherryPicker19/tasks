def F(n,m):
    if n == 1 or m == 1:
        return 1
    else:
        return F(n - 1, m) + F(n, m - 1)

n = 10
m = 5
print(F(n,m))
