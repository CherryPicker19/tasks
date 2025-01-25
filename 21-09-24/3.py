def is_skobki(s: str, acc: list, idx_last=0, longest=[], l=[]) -> bool:
    if idx_last == len(s):
        if acc == []:
            return True
        else:
            return max(l, default=False)

    acc.append(s[idx_last])
    if len(acc) == 1:
        return is_skobki(s, acc, idx_last+1)

    if acc[-2] in open_brackets and acc[-1] in close_brackets:
        if couples.get(acc[-2]) == couples.get(acc[-1]):
            longest.insert(0, acc[-2])
            longest.append(acc[-1])
            acc.pop()
            acc.pop()
            return is_skobki(s, acc, idx_last+1)
    if longest != []:
        a = ''.join(longest)
        l.append(a)
        longest.clear()
    return is_skobki(s, acc, idx_last+1)#

def main():
    global open_brackets, close_brackets, couples
    open_brackets = {"(", "{", "["}
    close_brackets = {")", "}", "]"}
    couples = {"(": 1, ")": 1, "{": 2, "}": 2, "[": 3, "]": 3}
    s = "{[(]){[()]}}"
    print(is_skobki(s, []))

if __name__ == '__main__':
    main()
