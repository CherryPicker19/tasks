class ListMath:
    def __init__(self, lst: list):
        self.lst_math = list()
        for i in lst:
            if type(i) == int or type(i) == float:
                self.lst_math.append(i)

    def __add__(self, other):
        return ListMath(list(map(lambda x: x + other, self.lst_math)))

    __radd__ = __add__

    def __iadd__(self, other):
        self.lst_math = list(map(lambda x: x + other, self.lst_math))
        return self

    def __sub__(self, other):
        return ListMath(list(map(lambda x: x - other, self.lst_math)))

    __rsub__ = __sub__

    def __isub__(self, other):
        self.lst_math = list(map(lambda x: x + other, self.lst_math))
        return self

    def __mul__(self, other):
        return ListMath(list(map(lambda x: x * other, self.lst_math)))

    __rmul__ = __mul__

    def __imul__(self, other):
        self.lst_math = list(map(lambda x: x * other, self.lst_math))
        return self

    def __truediv__(self, other):
        return ListMath(list(map(lambda x: x / other, self.lst_math)))

    def __rtruediv__(self, other):
        return ListMath(list(map(lambda x: other / x, self.lst_math)))

    def __itruediv__(self, other):
        self.lst_math = list(map(lambda x: x / other, self.lst_math))
        return self

lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]
print(lst.lst_math)
print((lst + 5).lst_math)
print(lst.lst_math)
lst2 = ListMath([1, "abc", -5])
print(lst2.lst_math)
print(lst.lst_math)
lst += 5
print(lst.lst_math)
lst = lst + 76 # сложение каждого числа списка с определенным числом
lst = 6.5 + lst # сложение каждого числа списка с определенным числом
lst += 76.7 # сложение каждого числа списка с определенным числом
lst = lst - 76 # вычитание из каждого числа списка определенного числа
lst = 7.0 - lst # вычитание из числа каждого числа списка
lst -= 76.3
lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
lst *= 5.54
lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
lst = 3 / lst # деление числа на каждый элемент списка
lst /= 13.0