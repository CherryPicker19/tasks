numb = int(input("Input: "))
copyNumb = numb
invNumb = 0
first_dig = 0
isOtr = False
if numb < 0:
    isOtr = True
    numb = numb * -1

while(True):
    second_dig = numb % 10
    numb = numb // 10
    invNumb = invNumb * 10 + second_dig

    if numb == 0:
        break
if (invNumb < 127 or invNumb > -128) and isOtr == False:
    print("Output: ", invNumb)
if invNumb < 127 or invNumb > -128:
    print("Output: ", invNumb * -1)
else:
    print("No solution")
