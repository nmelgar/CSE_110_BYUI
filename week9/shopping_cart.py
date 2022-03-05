action = ""
run = True
items = []
print("\nWelcome to the Shopping Cart program")

while run:
    print("")
    print("Please select one of the following:")
    menu = ["Add item", "View Cart", "Remove Item", "Compute total", "Quit"]
    for index, menu_item in enumerate(menu):
        if index >= 0:
            index += 1
        print(f"{index}.", menu_item)

    action = int(input("\nPlease enter an action: "))

    new_item = ""
    # 1. ADD ITEM
    if action == 1:
        new_item = str(input("\nWhat item would like to add? "))
        items.append(new_item)
        print(f"'{new_item}' has been added to the cart")

    # 2 VIEW CART
    if action == 2:
        print("The contents of the shopping cart are:")
        for item in items:
            print(item.capitalize())

    # 5. QUIT
    if action == 5:
        run = False
        print("Thank you, come back again!")
