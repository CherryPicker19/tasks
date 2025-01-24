def rimsk(rim : str):
    #rim = rim + '0'
    translt = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    otr = ['V', 'X', 'L', 'C', 'D', 'M']
    pol = ['V', 'L', 'D', 'M']
    tmp = []
    is_pol = 1
    for i in range(len(rim) - 1):
        if rim[i + 1] in otr:
            if rim[i] in pol or rim[i] == rim[i + 1]:
                is_pol = 1
            else:
                is_pol = -1
        else:
            is_pol = 1
        tmp.append(translt.get(rim[i]) * is_pol)
    tmp.append(translt.get(rim[-1]))
    return sum(tmp)

print(rimsk('MMXX'))