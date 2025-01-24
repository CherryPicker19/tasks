names = ['sber', 'tin', '1']
banks = [10000, 3000, 1234]

if len(names) == 2:
    print(max(banks))
sbanks = {}
for i in range(len(banks)):
    sbanks.setdefault(names[i])
    sbanks[names[i]] = banks[i]

banks.insert(0, 0)
names.insert(0,'a')

for i in range(2, len(banks)):
    if banks[i] + banks[i - 2] > banks[i - 1]:
        banks[i] = banks[i] + banks[i - 2]
        names[i] = [names[i - 2], names[i]]
    else:
        banks[i] = banks[i - 1]
        names[i] = names[i - 1]
answ = []
if len(names) == 3:
    a = 0
    if type(names[-1]) == type(list()):
        a = names[-1][-1]
    else:
        a = names[-1]
    print(banks[-1])
    print(a)
    answ.append((a, banks[-1]))
    answ.insert(0, banks[-1])

    #print(sbanks.get(names[-1]))

elif len(names) > 1:
    while True:
        if type(names[-1]) == type(str()):
            answ.append(names[-1])
            break
        else:
            a, b = names[-1]
            names[-1] = a
            answ.append(b)
    answ.reverse()
    for i in range(len(answ)):
        answ[i] = (answ[i], sbanks[answ[i]])
    answ.insert(0, banks[-1])
else:
    answ = []
print(answ)
