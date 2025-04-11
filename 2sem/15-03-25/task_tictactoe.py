import random

class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        if self.value == 0:
            return True
        else:
            return False

class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_0 = 2

    def __init__(self):
        self.pole = (
        (Cell(), Cell(), Cell()),
        (Cell(), Cell(), Cell()),
        (Cell(), Cell(), Cell())
        )

    def __getitem__(self, i):
        if not isinstance(i[0], int) or not isinstance(i[1], int):
            raise IndexError("Incorrect pole index")
        return self.pole[i[0]][i[1]].value

    def __setitem__(self, key, value):
        if not isinstance(key[0], int) or not isinstance(key[1], int):
            raise IndexError("Incorrect pole index")
        self.pole[key[0]][key[1]].value = value
        return None

    def __bool__(self):
        for i in self.pole:
            for j in i:
                if j.value == 0:
                    return False
        return True

    def show(self):
        for i in self.pole:
            print()
            for j in i:
                print(j.value, ' ', end='')
        print()

    def human_go(self):
        flag = True
        while flag:
            x = int(input("Input coordinate X: "))
            y = int(input("Input coordinate Y: "))
            if self.pole[x][y].value == self.FREE_CELL:
                self[x, y] = self.HUMAN_X
                flag = False
            else:
                print("Wrong coordinates!")
                continue

    def computer_go(self):
        flag = True
        while flag:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if self.pole[x][y].value == self.FREE_CELL:
                self[x, y] = self.COMPUTER_0
                flag = False
            else:
                continue

    def have_smbd_won(self, cell_type: int) -> int:
        have_won = False
        winning_pos = {
            ((0, 0), (0, 1), (0, 2)),
            ((1, 0), (1, 1), (1, 2)),
            ((2, 0), (2, 1), (2, 2)),
            ((0, 0), (1, 0), (2, 0)),
            ((0, 1), (1, 1), (2, 1)),
            ((0, 2), (1, 2), (2, 2)),
            ((0, 0), (1, 1), (2, 2)),
            ((2, 2), (1, 1), (0, 0)),
        }
        for i in winning_pos:
            a = i[0]
            b = i[1]
            c = i[2]
            if self[a[0], a[1]] == cell_type and self[b[0], b[1]] == cell_type and self[c[0], c[1]] == cell_type:
                have_won = True
            else:
                continue
        return have_won

    def is_human_win(self):
        return self.have_smbd_won(self.HUMAN_X)

    def is_computer_win(self):
        return self.have_smbd_won(self.COMPUTER_0)

    def is_draw(self):
        for i in self.pole:
            for j in i:
                if j.value == 0:
                    return False
        if self.have_smbd_won(self.HUMAN_X) or self.have_smbd_won(self.COMPUTER_0):
            return False
        return True

game = TicTacToe()
print(game[1, 2])
game[1, 2] = 1
game.show()
game.computer_go()
game.show()
print(game.have_smbd_won(1))

game1 = TicTacToe()
game[0, 0] = 1
game[1, 1] = 1
game[2, 2] = 1
game.show()
print(game.have_smbd_won(1))
print(game.is_human_win())

print(game.is_draw())
print(bool(game))
