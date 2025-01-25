def group_strings(strings):
    groups = {}
    for s in strings:
        key = (len(s), ''.join(sorted(s)))
        if key in groups:
            groups[key].append(s)
        else:
            groups[key] = [s]
    return list(groups.values())


input1 = ["qwe", "ewq", "asd", "dsa", "dsas", "qwee", "zxc", "cxz", "xxz", "z", "s", "qweasdzxc", "zzxc"]
output1 = group_strings(input1)
print(output1)

input2 = ["a", "a", ""]
output2 = group_strings(input2)
print(output2)
