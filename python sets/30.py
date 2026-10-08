# 7. Find the elements that occur in all lists.
lists = [[1, 2, 3, 4], [2, 3, 5], [0, 2, 3, 6]]

common_elements = set(lists[0]).intersection(*(set(values) for values in lists[1:]))
print("Elements in all lists:", common_elements)
