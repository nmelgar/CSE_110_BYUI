# This line imports or includes the library we will need
from PIL import Image

# This line opens the image and loads it into a variable called "image_original"
image_original = Image.open("images/beach.jpg")

# Also, please be aware that while in mathematics, the origin (0, 0)
# is located in the bottom left. In computer graphics, it is located in the top left.

# get the size
width, height = image_original.size

# access the pixels of the image
pixels_original = image_original.load()

# access r g b values of an individual pixel at ant spot
# see and print the color of a pixel at certain coordinates
r, g, b = pixels_original[1, 1]
print(r, g, b)

# Don't forget to use parentheses around your (r, g, b)
# you can set new red, green, and blue values for the pixel at location x, y
#this will assign a new value to the pixel at 1, 1
pixels_original[1, 1] = (60, 255, 51)

# This line attempts to open a new window to display the image.
image_original.show()

image_original.save("new_beach_image.jpg")