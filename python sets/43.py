# 8. Find the number of unique visitors from multiple days.
visitors_by_day = [
    {"user1", "user2", "user3"},
    {"user2", "user4"},
    {"user1", "user5"},
]

unique_visitors = set.union(*visitors_by_day)
print("Number of unique visitors:", len(unique_visitors))
