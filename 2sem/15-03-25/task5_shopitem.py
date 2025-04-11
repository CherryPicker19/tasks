import sys

class ShopItem:
    def __init__(self, name: str, weight: int|float, price: int|float):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        a = (self.name.lower(), self.weight, self.price)
        return hash(a)

    def __eq__(self, other):
        if hash(other) == hash(self):
            return True
        return False

a = ShopItem("aa", 100, 100)
b = ShopItem("aa", 100, 100)
print(hash(a) == hash(b))
print(a == b)

lst_in = [['Системный блок', 1500, 75890.56], ['Монитор Samsung', 2000, 34000], ['Клавиатура', 200.44, 545], ['Монитор Samsung', 2000, 34000]]

shop_items = {}
repeats = 1
for i in lst_in:
    len_old = len(shop_items)
    shop_items[ShopItem(i[0], i[1], i[2])] = [ShopItem(i[0], i[1], i[2]), repeats]
    if len_old == len(shop_items):
        shop_items[ShopItem(i[0], i[1], i[2])] = [ShopItem(i[0], i[1], i[2]), repeats + 1]

print(shop_items)


