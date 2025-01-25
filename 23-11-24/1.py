def santa_user(elfs : list):
    answ = {}
    for element in elfs:
        if len(element) == 1:
            answ.setdefault(element[0], None)
        else:
            answ.setdefault(element[0], element[1])
    return answ

elfs = []
n = int(input("Input amount of elfs: "))
for i in range(n):
    name = input("Input name & surname: ")
    id = input("Input mail(if exists): ")
    if id == '':
        elfs.append([name, None])
    else:
        elfs.append([name, id])
#elfs = [['name1 surname1', 12341234], ["name2 surname2", 244312421], ['name3 surname3']]
print(santa_user(elfs))
print(elfs)
