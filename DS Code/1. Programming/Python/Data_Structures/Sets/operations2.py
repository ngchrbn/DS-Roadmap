employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn',
            'John', 'Jane']

gym_members = ['April', 'John', 'Corey']

developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']

# Employees that are gym_members and developers (intersection)
gym_members_dev = set(gym_members).intersection(developers)

# Employees that are neither gym members nor developers(difference)
notgym_mb_dev = set(employees).difference(gym_members, developers)

# ⚠ Notice that you don't have to cast to params for the methods


print("Employees:", employees)
print("Gym members:", gym_members)
print("Developers:", developers, "\n")
print("Employees that are gym members and developers:",
        gym_members_dev)
print("Employees that are neither gym members nor developers:",
        notgym_mb_dev)