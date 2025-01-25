s = input("Input: ")
copys = s
outs = ''
povtors = ''
indexFirst = 0
indexLast = 0
mass = []

for i in range(len(s)):
    povtors += s[i]
    #print(povtors)
    if povtors.count(s[i]) <= 1:
        outs += s[i]
     #   print(outs)
    else:
        mass.append(outs)
        outs = ''
        indexLast = povtors.find(s[i])
        povtors = ''

      #  print(indexLast)
print(mass)

