def solution(n: int, s: int, seq: list, cur_sum: int, cur_eq="", idx = 0) -> str|None:
    if idx == len(seq):
        if cur_sum == s:
            return cur_eq
        else:
            return None

    next_plus = solution(n, s, seq, cur_sum+seq[idx], cur_eq+f"+{seq[idx]}", idx+1)
    if next_plus is not None:
        return next_plus

    next_minus = solution(n, s, seq, cur_sum-seq[idx], cur_eq+f"-{seq[idx]}", idx+1)
    if next_minus is not None:
        return next_minus

def read_input(filename: str) -> tuple:
    with open(filename, 'r') as f:
        inpt = list(map(int, f.readline().strip().split()))
        return inpt

def main():
    input = read_input('input.txt')
    n = input[0]
    s = input[-1]
    frst_num = input[1]
    seq = input[2:-1]
    answ = solution(n, s, seq, frst_num, cur_eq=str(frst_num))
    if answ is None:
        answ = 'no solution'
    else:
        answ +=  "=" + str(s)

    with open("answer.txt", "w") as f:
        f.write(answ)
if __name__ == '__main__':
    main()
