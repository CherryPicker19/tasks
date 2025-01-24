n = 3 # количество пар скобок
def f(s, m, left, right):

    if m == n * 2:
        return [s]

    res  = []
    if right > left:
        return

    if left < n:
        res += f(s + "(", m + 1, left + 1, right)

    if right < left:
        res += f(s + ")", m + 1, left, right + 1)

    return res

print(f("", 0, 0, 0))
