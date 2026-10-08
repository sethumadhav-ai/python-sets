# 10. Find users who visited all three days.
day1 = {"user1", "user2", "user3"}
day2 = {"user2", "user3", "user4"}
day3 = {"user2", "user3", "user5"}

users = day1 & day2 & day3
print("Users who visited all three days:", users)
