# This line imports or includes the library we will need
from PIL import Image

# This line opens the image and loads it into a variable called "image_original"
image_original = Image.open("images/cat_small.jpg")

# get the size of an image
width, height = image_original.size

# access the pixels of the image
pixels_original = image_original.load()

# access individual pixels at certain spot
r, g, b = pixels_original[100, 200]

# print the color of that particular pixel
print(r, g, b)

# replace the color at certain location to a new color
pixels_original[100, 200] = (255, 0, 255)

# This line attempts to open a new window to display the image.
image_original.show()

# save image to a new file
# image_original.save("the_file_goes_here.jpg")

###########SPECIAL NOTES ABOUT THE PROJECT###########
# Be aware that while in mathematics, the origin (0, 0)
# is located in the bottom left. In computer graphics, it is located in the top left.

# put the r,g,b variables in that order, the computer wont understand other order
