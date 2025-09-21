firstname, middlename, lastname = input("Enter your full name(First name, Middle name, Last name)").split()

firstname = firstname.strip().capitalize()
middlename = middlename.strip().capitalize()
lastname = lastname.strip().capitalize()

middle_initial = middlename[0] + "."

print(f"{lastname}, {firstname} {middle_initial}")