from collections import Counter
from functools  import partial
# Переделать
class NewList:
    def __init__(self, lst=None):
        self.lst = lst
        if lst == None:
            self.lst = list()
        #self.lst = lst

    def __iter__(self):
        return iter(self.lst)

    @classmethod
    def __validator(cls, dic, item):
        key = (type(item), item)
        if key in dic and dic[key] > 0:
            dic[(type(item), item)] -= 1
            return False
        else:
            return True

    def __sub_body(self, first, other):
        if not isinstance(other, NewList):
            other = NewList(other)
        lst_dict = Counter((type(i), i) for i in other)
        first = list(filter(partial(self.__validator, lst_dict), first))
        return first

    def __sub__(self, other):
        return self.__class__(self.__sub_body(self.lst, other))

    def __rsub__(self, other):
        return self.__class__(self.__sub_body(other, self.lst))

    def __isub__(self, other):
        self.lst = self.__sub_body(self.lst, other)
        return self

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
c = NewList([1,1,1,1,1,1,1,1,1,1])
b = NewList([1,1])
a = c - b
print(a.get_list())
