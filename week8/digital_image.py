# This line imports or includes the library we will need
from PIL import Image

# This line opens the image and loads it into a variable called "image_original"
image_cat = Image.open("images/cat_small.jpg")

# get the size of an image
# width, height = image_original.size
# print(width, height)
image_size = image_cat.size
print(image_size)


# access the pixels of the image
pixels_original = image_cat.load()

# access individual pixels at certain spot
print(pixels_original[200, 100])
r, g, b = pixels_original[100, 200]

# print the color of that particular pixel


# replace the color at certain location to a new color

# [x, 300] are the coordinates that will be used


# This line attempts to open a new window to display the image.
image_cat.show()

# save image to a new file
# image_original.save("the_file_goes_here.jpg")

###########SPECIAL NOTES ABOUT THE PROJECT###########
# Be aware that while in mathematics, the origin (0, 0)
# is located in the bottom left. In computer graphics, it is located in the top left.

# put the r,g,b variables in that order, the computer wont understand other order
