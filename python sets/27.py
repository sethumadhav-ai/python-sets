# 4. Find the intersection of multiple sets stored inside a list.
sets_list = [{1, 2, 3, 4}, {2, 3, 5}, {0, 2, 3, 6}]

common_elements = set.intersection(*sets_list)
print("Intersection:", common_elements)
