def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial


first_name = input("Enter your first name: ")
first_name_initial = get_initial(force_uppercase=False, name=first_name)

print("Your initial is: " + first_name_initial)


# ASSIGN A DEFAULT VALUE FOR A PARAMETER
# def get_initial(name, force_uppercase=True):
#     if force_uppercase:
#         initial = name[0:1].upper()
#     else:
#         initial = name[0:1]
#     return initial

# first_name = input("Enter your first name: ")
# first_name_initial = get_initial(first_name, False)

# print("Your initial is: " + first_name_initial)


# ASSIGN THE VALUES OF PARAMETERS BY NAME WHEN YOU CALL THE FUNCTION
# def get_initial(name, force_uppercase):
#     if force_uppercase:
#         initial = name[0:1].upper()
#     else:
#         initial = name[0:1]
#     return initial


# first_name = input("Enter your first name: ")
# Following line is using name notation
# first_name_initial = get_initial(force_uppercase=True, name=first_name)

# print("Your initial is: " + first_name_initial)
