# Переделать
class NewList:
    def __init__(self, lst: list):
        if lst == None:
            self.lst = list()
        self.lst = lst

    def __iter__(self):
        return iter(self.lst)

    def __sub__(self, other):
        #вычетаем элемент лишь 1 раз
        if not isinstance(other, NewList):
            other = NewList(other)
        lst = self.lst.copy()
        other_lst = other.lst.copy()

        lst_dict = {}
        for i in self.lst:
            j = None
            if lst_dict.get((type(i), i), None) is None:
                lst_dict[(type(i), i)] = 1
            else:
                lst_dict[(type(i), i)] = lst_dict[(type(i), i)] + 1

        other_dict = {}
        for i in other:
            if (type(i), i) in lst_dict:
                lst_dict[(type(i), i)] -= 1

        answ = []
        for i in lst_dict:
            if i[1] > 0:
                answ.append(i[1])

        lst_copy = list()
        subs = list()
        for i in lst:
            flag = True
            for j in other_lst:
                if i == j and type(i) == type(j):
                    subs.append(i)
                    other_lst.remove(j)
                    flag = False
            if flag:
                lst_copy.append(i)
        print('ANSW: ',answ)
        return NewList(lst_copy)


    def __rsub__(self, other):

        if not isinstance(other, NewList):
            other = NewList(other)
        other_lst = self.lst.copy()
        lst = other.lst.copy()
        lst_copy = list()
        subs = list()
        for i in lst:
            flag = True
            for j in other_lst:
                if i == j and type(i) == type(j):
                    subs.append(i)
                    other_lst.remove(j)
                    flag = False
            if flag:
                lst_copy.append(i)
        return NewList(lst_copy)

    def __isub__(self, other):
        if not isinstance(other, NewList):
            other = NewList(other)
        lst = self.lst.copy()
        other_lst = other.lst.copy()
        lst_copy = list()
        subs = list()
        for i in lst:
            flag = True
            for j in other_lst:
                if i == j and type(i) == type(j):
                    subs.append(i)
                    other_lst.remove(j)
                    flag = False
            if flag:
                lst_copy.append(i)
        self.lst = lst_copy.copy()
        return NewList(lst_copy)

    def get_list(self):
        return self.lst

lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
print(res_1.get_list())
print(lst2.get_list())
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
print(lst1.get_list())
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
print(res_2.get_list())
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
print(res_3.get_list())
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
print(res_4.get_list())
a = NewList([1])
b = NewList([1, 1])
c = a - b
print(c.get_list())