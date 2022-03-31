import math
run = True

while run:
    print("\n*******************************************")
    print("You can calculate the area: square, rectangle and circle")
    print("Type quit to exit the program")
    shape_choice = str(input("\nWhat's the shape you want to calculate the area? "))
    shape_choice = shape_choice.lower()

    if shape_choice == "quit":
        run = False
        print("Please come back later!!!!!")

    elif shape_choice == "square":
        # function for the square

        def compute_area_square(side):
            area = side * side
            return area

        side_length = (
            float(input("Enter the length for a side of the square: ")))
        side_length_final = compute_area_square(side_length)
        print(f"The area of a square is: {side_length_final}")
        print("*******************************************")

    elif shape_choice == "rectangle":
        # function for the rectangle

        def compute_area_rectangle(width, side):
            area = side * width
            return area

        side_length = (
            float(input("Enter the length for a side of the rectangle: ")))
        width_length = (
            float(input("Enter a length for the width of the rectangle: ")))
        rectangle_final = compute_area_rectangle(width_length, side_length)
        print(f"The area of the rectangle is: {rectangle_final}")
        print("*******************************************")

    elif shape_choice == "circle":
        # function for the circle

        def compute_area_circle(side):
            area = (math.pi) * (side ** 2)
            return area
        side_length = (
            float(input("Enter the radius for the circle: ")))
        circle_area = compute_area_circle(side_length)
        print(f"The area of the circle is: {circle_area: .2f}")
        print("*******************************************")


# cube volume formula side * side * side
# print("")
# cube_volume_formula = side_length * 3
# print(f"The volume of the cube is {cube_volume_formula}")
