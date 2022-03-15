# use the open function
# check the folder where it is
with open("week11/courses.txt") as courses_file:
    for line in courses_file:
        #to clean the white spaces
        line = line.strip()

        #line = "CSE 110,98.5"
        parts = line.split(",")

        #parts = ["CSE 110", "98.5"]
        name = parts[0]
        grade = float(parts[1])

        bonus_grade = grade + 3
        print(f"{name} - Grade: {grade:.2f}, after bonus: {bonus_grade}")

# the previous code will open and close the file
# print("The file is close now.")
