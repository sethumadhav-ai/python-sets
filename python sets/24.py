# 1. Find the first duplicate element in a list using a set.
numbers = [4, 2, 7, 2, 5, 4]
seen = set()
first_duplicate = None

for number in numbers:
    if number in seen:
        first_duplicate = number
        break
    seen.add(number)

print("First duplicate:", first_duplicate)
