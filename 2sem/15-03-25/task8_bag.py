class Thing:
    def __init__(self, name: str, weight: int|float):
        self.name = name
        self.weight = weight

class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.cur_weight = 0
        self.things = list()

    def __getitem__(self, idx):
        if idx > len(self.things) or idx < 0:
            raise IndexError('неверный индекс')
        return self.things[idx]

    def __setitem__(self, idx, value):
        if idx > len(self.things) or idx < 0:
            raise IndexError('неверный индекс')
        self.things[idx] = value

    def __delitem__(self, idx):
        if idx > len(self.things) or idx < 0:
            raise IndexError('неверный индекс')
        self.things.pop(idx)

    def add_thing(self, thing):
        if thing.weight + self.cur_weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        self.things.append(thing)

bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))
bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
print(bag[2].name) # рубашка
bag[1] = Thing('платок', 100)
print(bag[1].name) # платок
del bag[0]
print(bag[0].name) # платок
t = bag[4] # генерируется исключение IndexError