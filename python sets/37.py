# 2. Find all pairs in a list whose sum equals a target.
numbers = [2, 7, 11, 15, 3, 6, 2]
target = 9
seen = set()
pairs = set()

for number in numbers:
    complement = target - number
    if complement in seen:
        pairs.add((min(number, complement), max(number, complement)))
    seen.add(number)

print("Pairs that sum to", target, ":", pairs)
