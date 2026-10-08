# 9. Find users who visited Day 1 and Day 2 but not Day 3.
day1 = {"user1", "user2", "user3"}
day2 = {"user2", "user3", "user4"}
day3 = {"user3", "user5"}

users = (day1 & day2) - day3
print("Visited Day 1 and Day 2, but not Day 3:", users)
