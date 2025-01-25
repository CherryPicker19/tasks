mport itertools 
a = [1, 1, 2]
b = []
c = []
answ = []
b = itertools.permutations(a)
for i in b:
    c.append(list(i))
for j in c:
    if j not in answ:
        answ.append(j)
print(answ)
