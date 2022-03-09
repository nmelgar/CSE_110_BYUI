action = ""
items = []
prices = []
run = True

print("******************************************")
print("Welcome to the Shopping Cart program")

while run:
    print("")
    print("Please select one of the following:")
    menu = ["Add item", "View Cart", "Remove Item", "Compute total", "Quit"]
    # for index, menu_item in enumerate(menu):
    #     if index >= 0:
    #         index += 1
    #     print(f"{index}.", menu_item)
    for index in range(len(menu)):
        menu_item = menu[index]
        print(f"{index + 1}. {menu_item}")

    action = int(input("\nPlease enter an action: "))

    add_item = ""
    add_price = ""
    # 1. ADD ITEM
    if action == 1:
        add_item = str(input("\nWhat item would like to add? "))
        items.append(add_item)
        add_price = (float(input(f"What is the price of {add_item}? ")))
        prices.append(add_price)
        print(f"'{add_item}' has been added to the cart")

    # 2 VIEW CART
    if action == 2:
        print("The contents of the shopping cart are:")
        for index in range(len(items)):
            add_item = items[index]
            add_price = prices[index]
            print(f"{index +1}. {add_item.capitalize()} - ${add_price: .2f}")
        # for item in items:
        #     print(item.capitalize())

    # 5. QUIT
    if action == 5:
        run = False
        print("Thank you, come back again!")
