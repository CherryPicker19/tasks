n = int(input("Input N: "))
c = int(input("Input C: "))
l = [4, -5, -7, 12, -2, 5]
flag = False
l.sort() # [-7, -5, -2, 4, 5, 12]
L = 0
R = len(l) - 1
otvet = (l[L] + l[L + 1] + l[L + 2] + l[R]) + 1
while l[L + 2] != R:
    sum4 = l[L] + l[L + 1] + l[L + 2] + l[R]
    if sum4 == otvet or flag:
        print(sum4)
        break;
    if sum4 > otvet and sum4 < c or sum4 < otvet and sum4 > c:
        otvet = sum4
        L += 1
        flag = True

    else:
        flag = True
        R -= 1


print(otvet)


