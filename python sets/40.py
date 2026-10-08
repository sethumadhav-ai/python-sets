# 5. Find duplicate records based on multiple fields using sets.
records = [
    {"name": "Ava", "email": "ava@example.com", "department": "Sales"},
    {"name": "Noah", "email": "noah@example.com", "department": "IT"},
    {"name": "Ava B.", "email": "ava@example.com", "department": "Sales"},
    {"name": "Mia", "email": "mia@example.com", "department": "IT"},
]
seen_records = set()
duplicate_records = []
fields = ("email", "department")

for record in records:
    key = tuple(record[field] for field in fields)
    if key in seen_records:
        duplicate_records.append(record)
    else:
        seen_records.add(key)

print("Duplicate records:", duplicate_records)
