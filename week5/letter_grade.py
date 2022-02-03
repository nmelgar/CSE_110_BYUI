grade = float(input("what's your grade percentage?: "))

if grade >= 90:
    if grade >= 97:
        letter = "A"
    elif grade >= 90 and grade <= 96:
        letter = "A-"
elif grade >= 80:
    if grade >= 87:
        letter = "B+"
    elif grade >= 80 and grade <= 86:
        letter = "B-"
elif grade >= 70:
    if grade >= 77:
        letter = "C+"
    elif grade >= 70 and grade <= 76:
        letter = "C-"
elif grade >= 60:
    if grade >= 67:
        letter = "D+"
    elif grade >= 60 and grade <= 66:
        letter = "D-"
elif grade < 60:
    letter = "F"
else:
    print("You didn't get a correct grade")
print(f"Your letter grade is {letter}")

if grade >= 70:
    print("Congratulations you passed the class!!")
else:
    print("Sorry, you should take the course again :(")
