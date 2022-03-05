new_item = ""
items = []

while new_item != "quit":
    new_item = str(input("What item would like to add? "))
    items.append(new_item)
    print(f"'{new_item}' has been added to the cart")

# 2 VIEW CART

print("The contents of the shopping cart are")
for item in items:
    print(item)
