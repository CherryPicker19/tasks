def read_input(filename: str) -> tuple:
    with open(filename, 'r') as f:
        N, L, K = map(int, f.readline().strip().split())
        pieces = [tuple(map(int, f.readline().strip().split())) for _ in range(K)]
    return N, L, K, pieces

def mark_tiles(x: int, y: int, board: list):
    moves = ((0, -1), (0, 1), (3, 0), (-3, 0), (0, -3), (0, 3), (-1, -2), (-1, 2), (-1, 0), (1, -2), (1, 2), (1, 0), (-2, -1), (-2, 1), (2, -1), (2, 1))
    for i in moves:
        if x + i[0] < 0 or y + i[1] < 0 or x + i[0] > n-1 or y + i[1] > n-1:
            continue
        else:
            board[x+i[0]][y+i[1]] = '*'
    board[x][y] = '#'

def clear_tiles(x: int, y: int, board: list):
    board[x][y] = '0'
    for x in range(n):
        for y in range(n):
            if board[x][y] == '*':
                board[x][y] = '0'
    for x in range(n):
        for y in range(n):
            if board[x][y] == '#':
                mark_tiles(x, y, board)

def can_be_placed(x: int, y: int, board) -> bool:
    moves = ((0, -1), (0, 1), (3, 0), (-3, 0), (0, -3), (0, 3), (-1, -2), (-1, 2), (-1, 0), (1, -2), (1, 2), (1, 0), (-2, -1), (-2, 1), (2, -1), (2, 1))
    for i in moves:
        if x + i[0] < 0 or y + i[1] < 0 or x + i[0] > n - 1 or y + i[1] > n - 1:
            continue
        else:
            if board[x + i[0]][y+i[1]] == '#' or board[x][y] == '#':
                return False
            else:
                continue
    return True

def place_figure(x: int, y: int, l: int, cur_solution: list, placed_figures: list, board: list, cache: set):
    if l == 0:
        cur_solution.sort()
        cur_solution_t = tuple(cur_solution)
        if cur_solution_t in cache:
            return None
        cache.update(cur_solution_t)
        answ = cur_solution + placed_figures
        #print(*answ)
        for el in answ:
            f.write(str(el) + " ")
        #f.write(f"{cur_solution + placed_figures}"[1:-1] + '\n')
        f.write('\n')
        return None
    for i in range(x, n):
        for j in range(y if i == x else 0, n):
            if can_be_placed(i, j, board):
                cur_solution.append((i, j))
                mark_tiles(i, j, board)
                place_figure(i, j, l - 1, cur_solution, placed_figures, board, cache)
                clear_tiles(i, j, board)
                cur_solution.pop()

def main():
    global n, l, f, const_pieces
    n, l, k, const_pieces = read_input('input.txt')
    board = [['0' for i in range(n)] for j in range(n)]
    for i in const_pieces:
        mark_tiles(i[0], i[1], board)
    f = open('output2.txt', 'w')
    cache = set()
    print(f'Размер доски: {n}, Нужно поставить фигур: {l}, Уже стоят фигур: {k}')
    place_figure(0, 0, l, [], const_pieces, board, cache)
    f.close()
    f = open('output2.txt', 'r+')
    a = f.readline()
    if a == '':
        f.write('no solution')
    else:
        a = str(a).strip().split(sep=' ')
        c = [ele.replace(',', '') for ele in a]
        b = [ele.replace('(', '') for ele in c]
        d = [ele.replace(')', '') for ele in b]
        p = []
        for i in range(1, len(d), 2):
            p.append((d[i-1], d[i]))
        d = []
        for i in p:
            d.append((int(i[0]), int(i[1])))
        for i in d:
            mark_tiles(i[0], i[1], board)
        for i in board:
            print(*i)
    f.close()
if __name__ == '__main__':
    main()