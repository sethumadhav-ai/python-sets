# 6. Find the elements that occur in at least two lists.
lists = [[1, 2, 3, 4], [2, 3, 5], [3, 6]]
occurrences = {}

for values in lists:
    for value in set(values):
        occurrences[value] = occurrences.get(value, 0) + 1

result = {value for value, count in occurrences.items() if count >= 2}
print("Elements in at least two lists:", result)
