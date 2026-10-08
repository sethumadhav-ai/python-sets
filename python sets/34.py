# 11. Find missing numbers from a sequence using sets.
sequence = [1, 2, 4, 6]
expected_numbers = set(range(min(sequence), max(sequence) + 1))
missing_numbers = expected_numbers - set(sequence)

print("Missing numbers:", missing_numbers)
