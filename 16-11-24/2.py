def func(list1 : list, list2 : list):
    list1 = set(list1)
    list2 = set(list2)
    answ1 = (len(list1 & list2), list(list1 & list2))
    answ2 = (len(list1 ^ list2), list(list1 ^ list2))
    answ3 = (len(list1 - list2), list(list1 - list2))
    answ4 = (len(list2 - list1), list(list2 - list1))
    return answ1, answ2, answ3, answ4


list1 = [0, 33, 37, 6, 10, 44, 13, 47, 16, 18, 22, 25]
list2 = [1, 38, 48, 8, 41, 7, 12, 47, 16, 40, 20, 23, 25]
print(func(list1, list2))
