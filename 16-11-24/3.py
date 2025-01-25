def unique_subsets(elements):
    result = set()
    unique_elements = list(set(elements))

    def backtrack(start, current_subset):
        if current_subset:
            result.add(tuple(sorted(current_subset)))

        for i in range(start, len(unique_elements)):
            current_subset.append(unique_elements[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()

    backtrack(0, [])
    return list(map(list, result)), len(result)

input1 = [1, 2, 3, 4]
subsets1, count1 = unique_subsets(input1)
print("Subsets: ", subsets1)
print("Number of subsets: ", count1)
