word = input("Input word: ")
val = int(input("Input int: "))
schet = (val - 2) + val
final = []

for n in range(0, val):
    for i in range(0, len(word), schet):
        #print(n == val - 1 and i == len(word) - 1)
        if n == val - 1 and i == len(word) - 1:
            final.append(word[i - n])
            break
        if i == 0:
            #print(word[n])
            if n != val -1:
                final.append(word[n])
        elif i == len(word) - 1:
            #print(word[ (-1 * n) -1])
            if n != val - 1:
                final.append(word[ (-1 * n) -1])
        elif word[i - n] == word[i + n]:
            #print(word[i + n])
            if n != val - 1:
                final.append(word[i + n])
        elif word[i - n] == word[i]:
            break
        else:
            #print(word[i - n], word[i + n])
            if n == val - 1 and i != 0:
                final.append(word[i - n])
            else:
                final.append(word[i - n])
                final.append(word[i + n])

fin_string = ''.join(final)
print(fin_string)
