# 10. Find the longest consecutive sequence in an unsorted list.
# Example: [100, 4, 200, 1, 3, 2].
numbers = [100, 4, 200, 1, 3, 2]
number_set = set(numbers)
longest_sequence = []

for number in number_set:
    if number - 1 not in number_set:
        sequence = []
        current = number
        while current in number_set:
            sequence.append(current)
            current += 1
        if len(sequence) > len(longest_sequence):
            longest_sequence = sequence

print("Longest consecutive sequence:", longest_sequence)
