from PIL import Image

image_cat = Image.open("images/cat.jpg")
image_beach = Image.open("images/beach.jpg")
new_image = Image.new("RGB", image_beach.size)
(width, height) = image_cat .size

pixels_original = new_image.load()
pixels_cat = image_cat.load()


for y in range(0, height):
    for x in range(0, width):
        (r, g, b) = pixels_cat[x, y]
        pixels_cat[x, y] = (r, 2, b)
image_beach.paste(image_cat, (0, 0))
image_beach.show()
