from operator import truediv


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value if  self.MIN_DIMENSION <= value <= self.MAX_DIMENSION else self.__a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value if  self.MIN_DIMENSION <= value <= self.MAX_DIMENSION else self.__b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        self.__c = value if  self.MIN_DIMENSION <= value <= self.MAX_DIMENSION else self.__c

    def __gt__(self, other):
        if self.a > other.a and self.b > other.b and self.c > other.c:
            return True
        return False

    def __ge__(self, other):
        if self.a >= other.a and self.b >= other.b and self.c >= other.c:
            return True
        return False

    def __lt__(self, other):
        if self.a < other.a and self.b < other.b and self.c < other.c:
            return True
        return False

    def __le__(self, other):
        if self.a <= other.a and self.b <= other.b and self.c <= other.c:
            return True
        return False

class ShopItem:
    def __init__(self, name: str, price: int|float, dim: Dimensions):
        self.name = name
        self.price = price
        self.dim = dim

d3 = Dimensions(500, 200, 200) # a, b, c - габаритные размеры
print(d3 >= d3)

lst_shop = [
    ShopItem("кеды", 1024, Dimensions(40, 30, 120)),
    ShopItem("зонт", 500.24, Dimensions(10, 20, 50)),
    ShopItem("холодильник", 40000, Dimensions(2000, 600, 500)),
    ShopItem("табуретка", 2000.99, Dimensions(500, 200, 200))
]

lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)

for i in lst_shop_sorted:
    print(f"{i.name}, {i.price}, [{i.dim.a} {i.dim.b} {i.dim.c}]")
print('===========')
for i in lst_shop:
    print(f"{i.name}, {i.price}, [{i.dim.a} {i.dim.b} {i.dim.c}]")