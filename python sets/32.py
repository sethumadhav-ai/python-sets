# 9. Find whether a list contains duplicate values in O(n) time using a set.
numbers = [1, 2, 3, 4, 2]
seen = set()
contains_duplicates = False

for number in numbers:
    if number in seen:
        contains_duplicates = True
        break
    seen.add(number)

print("Contains duplicates:", contains_duplicates)
