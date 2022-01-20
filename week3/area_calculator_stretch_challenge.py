import math

#square - side * side
side_length = (float(input("Enter a length for a side: ")))
square_area_formula = side_length * side_length
print(f"The area of the square is {square_area_formula}")

#rectangle - length * width
print("")
rectangle_side_width = (float(input("Enter the width of a side of the rectangle: ")))
rectangle_area_formula = side_length * rectangle_side_width
print(f"The area of the rectangle is {rectangle_area_formula}")

#circle - 3.14 * radius squared
print("")
circle_area_formula = (math.pi) * (side_length ** 2)  
print(f"The area of the circle is {circle_area_formula}")

#cube volume formula side * side * side
print("")
cube_volume_formula = side_length * 3
print(f"The volume of the cube is {cube_volume_formula}")