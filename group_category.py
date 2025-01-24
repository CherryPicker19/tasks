l = ["qwe", "ewq", "asd", "dsa", "dsas", "qwee", "zxc", "cxz", "xxz", "z", "s", "qweasdzxc", "zzxc"]
d1 = {}
d2 = {}

for i in l:
    d1[len(i)] = [j for j in l if len(j) == len(i)]
    d2[i[0]] = [j for j in l if j[0] == i[0]]

res1 = [i for i in d1.values()]
res2 = [i for i in d2.values()]

print(res1, res2, sep='\n')