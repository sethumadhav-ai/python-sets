# 7. Given multiple users and their permissions, find users having common permissions.
user_permissions = {
    "Ava": {"read", "write", "share"},
    "Noah": {"read", "share"},
    "Mia": {"read", "delete", "share"},
}

common_permissions = set.intersection(*user_permissions.values())
print("Permissions common to all users:", common_permissions)
