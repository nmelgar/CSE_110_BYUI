import math
grade = math.floor(float(input("what's your grade percentage?: ")))

print(grade)

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
elif grade < 60:
    letter = "F"
else:
    print("You didn't get a correct grade")

sign = ""
if grade >= 97:
    sign = ""
elif grade <= 60:
    sign = ""
elif grade % 10 >= 7:
    sign = "+"
elif grade % 10 <= 6:
    sign = "-"
print(f"Your letter grade is {letter}{sign}")


if grade >= 70:
    print("Congratulations you passed the class!!")
else:
    print("Sorry, you should take the course again :(")
