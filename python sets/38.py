# 3. Find all triplets whose sum equals a target.
numbers = [-1, 0, 1, 2, -1, -4]
target = 0
sorted_numbers = sorted(numbers)
triplets = set()

for index in range(len(sorted_numbers) - 2):
    left = index + 1
    right = len(sorted_numbers) - 1
    while left < right:
        total = sorted_numbers[index] + sorted_numbers[left] + sorted_numbers[right]
        if total == target:
            triplets.add(
                (sorted_numbers[index], sorted_numbers[left], sorted_numbers[right])
            )
            left += 1
            right -= 1
        elif total < target:
            left += 1
        else:
            right -= 1

print("Triplets that sum to", target, ":", triplets)
