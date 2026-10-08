# 6. Given employee skill sets, find employees having all required skills.
employee_skills = {
    "Ava": {"Python", "SQL", "Git"},
    "Noah": {"Python", "JavaScript"},
    "Mia": {"Python", "SQL", "Docker"},
}
required_skills = {"Python", "SQL"}

qualified_employees = {
    employee
    for employee, skills in employee_skills.items()
    if required_skills.issubset(skills)
}
print("Employees with all required skills:", qualified_employees)
