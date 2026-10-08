# 12. Find common elements between two lists without using loops inside loops.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_elements = set(list1).intersection(list2)
print("Common elements:", common_elements)
