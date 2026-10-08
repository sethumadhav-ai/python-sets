# 5. Find the union of multiple sets stored inside a list.
sets_list = [{1, 2, 3}, {3, 4}, {4, 5, 6}]

all_elements = set.union(*sets_list)
print("Union:", all_elements)
