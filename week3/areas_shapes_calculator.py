import math

#square - side * side
square_side_length = (float(input("Enter the length of a side of the square: ")))
square_area_formula = square_side_length * square_side_length
print(f"The area of the square is {square_area_formula}")

#rectangle - length * width
print("")
rectangle_side_length = (float(input("Enter the length of a side of the rectangle: ")))
rectangle_side_width = (float(input("Enter the width of a side of the rectangle: ")))
rectangle_area_formula = rectangle_side_length * rectangle_side_width
print(f"The area of the rectangle is {rectangle_area_formula}")

#circle - 3.14 * radius squared
print("")
circle_radius = (float(input("Enter the radius of the circle: ")))
# pi = 3.14
circle_area_formula = (math.pi) * (circle_radius ** 2)  
print(f"The area of the circle is {circle_area_formula}")

#cube