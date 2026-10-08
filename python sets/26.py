# 3. Find all duplicate values without using count().
numbers = [4, 2, 7, 2, 5, 4, 9, 7]
seen = set()
duplicates = set()

for number in numbers:
    if number in seen:
        duplicates.add(number)
    else:
        seen.add(number)

print("Duplicate values:", duplicates)
