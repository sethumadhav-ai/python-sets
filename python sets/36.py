# 1. Find the longest substring without repeating characters using a set.
text = "abcabcbb"
window = set()
left = 0
longest_substring = ""

for right, character in enumerate(text):
    while character in window:
        window.remove(text[left])
        left += 1
    window.add(character)
    if right - left + 1 > len(longest_substring):
        longest_substring = text[left:right + 1]

print("Longest substring:", longest_substring)
print("Length:", len(longest_substring))
