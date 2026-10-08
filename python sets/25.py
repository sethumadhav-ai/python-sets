# 2. Find the first non-repeating element in a list.
numbers = [4, 2, 7, 2, 5, 4, 9]
frequencies = {}

for number in numbers:
    frequencies[number] = frequencies.get(number, 0) + 1

first_non_repeating = next(
    (number for number in numbers if frequencies[number] == 1),
    None,
)
print("First non-repeating element:", first_non_repeating)
