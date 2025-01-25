s = input("Input: ")
s = s.lower() + ' '
word = ''
lists = []
for c in s:
    if c == ' ' or c == '':
        lists.append(word + ' ')
        word = ''
    else:
        word += c

lists.reverse()
outputs = ''.join(lists)
print(outputs.capitalize())
