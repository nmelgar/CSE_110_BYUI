import math


def compute_area_square(side):
    return side * side


def compute_area_rectangle(width, length):
    return width * length


def compute_area_circle(radius):
    return (math.pi) * (radius ** 2)


run = True
shape_choice = ""

print("\n**************************************")
print("Welcome to the area calculator:")
print("You can choose square, rectangle and circle.")
print("\n**************************************")

while run:

    shape_choice = str(
        input("\nWhat shape do you choose? (type quit to exit) "))
    shape_choice = shape_choice.lower()
    if shape_choice == "quit":
        run = False
        print("\nPlease come back later!!!")

    elif shape_choice == "square":
        side = float(input("What's the size for the side? "))
        area = compute_area_square(side)
        print(f"The area of the square is {area: .2f}")

    elif shape_choice == "rectangle":
        width = float(input("What's the width size? "))
        length = float(input("What's the length size? "))
        area = compute_area_rectangle(width, length)
        print(f"The area of the square is {area: .2f}")

    elif shape_choice == "circle":
        radius = float(input("What's the radius? "))
        area = compute_area_circle(radius)
        print(f"The area of the square is {area: .2f}")

    else:
        print("\nSorry, that shape is not available, try different one")
