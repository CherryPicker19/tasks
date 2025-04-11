from random import randint

class Cell:
    def __init__(self, __is_mine=False, __number=0, __is_open=False):
        self.__is_mine = __is_mine
        self.__number = __number
        self.__is_open = __is_open

    def __bool__(self):
        return not self.__is_open

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        if not isinstance(value, bool):
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if not isinstance(value, int):
            raise ValueError("недопустимое значение атрибута")
        self.__number = value

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        if not isinstance(value, bool):
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = value

class GamePole:
    _instance = None

    def __new__(cls, n, m, total_mines):
        if cls._instance is None:
            cls._instance = super(GamePole, cls).__new__(cls)
            # initialization
            cls.n = n
            cls.m = m
            cls.total_mines = total_mines
            cls.__pole_cells = tuple(tuple(Cell() for i in range(m)) for j in range(n))
        return cls._instance

    @property
    def pole(self):
        return self.__pole_cells

    def show_pole(self):
        for i in self.__pole_cells:
            print()
            for j in i:
                x = '?' if not j.is_open else j.number
                #x = '*' if j.is_mine else j.number
                print(x, end=' ')
        print()

    def init_pole(self):
        # place mines
        repeats = list()
        for _ in range(self.total_mines):
            i = randint(0, len(self.__pole_cells) - 1)
            j = randint(0, len(self.__pole_cells[0]) - 1)
            while (i,j) in repeats:
                i = randint(0, len(self.__pole_cells) - 1)
                j = randint(0, len(self.__pole_cells[0]) - 1)
            repeats.append((i, j))
            #print(i, j)
            self.__pole_cells[i][j].is_mine = True
            #print(i, j)
            pos = ((1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, 1), (-1, -1), (1, -1))
            for k in pos:
                #if 0 <= i+k[0] < len(self.__pole_cells) and 0 <= j+k[1] < len(self.__pole_cells[0]):
                try:

                    if not self.__pole_cells[i + k[0]][j + k[1]].is_mine and i + k[0] > -1 and j + k[1] > -1:
                        self.__pole_cells[i + k[0]][j + k[1]].number += 1
                        #print(i + k[0], j + k[1])
                        #self.show_pole()
                except:
                    continue

    def open_cell(self, i, j):
        if not isinstance(i, int) or not isinstance(j, int) or i > len(self.__pole_cells) - 1 or j > len(self.__pole_cells):
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.__pole_cells[i][j].is_open = True

#a = Cell()
#print(bool(a))
#b = GamePole(5, 5, 10)
#b.init_pole()
#b.show_pole()
#print(b.pole[0][0])
pole = GamePole(10, 20, 10) # создается поле размерами 10x20 с общим числом мин 10
pole.init_pole()
#pole.show_pole()
if pole.pole[0][1]:
    pole.open_cell(0, 1)
if pole.pole[3][5]:
    pole.open_cell(3, 5)
#pole.open_cell(30, 100) # генерируется исключение IndexError
pole.show_pole()
