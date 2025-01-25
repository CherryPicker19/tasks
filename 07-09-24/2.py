numb = int(input("Input: "))
copyNumb = numb
invNumb = 0
first_dig = numb % 10

print(numb)

while(True):
    second_dig = numb % 10
    numb = numb // 10
    first_dig = first_dig * 10 + second_dig
    if first_dig == copyNumb:
        #print("True")
        break
    elif first_dig > copyNumb:
        #print("False")
        break
print(first_dig)
