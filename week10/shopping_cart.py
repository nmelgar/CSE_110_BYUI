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
        add_item = str(input("\nWhat item would you like to add? "))
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

    #3 REMOVE AN ITEM
    if action == 3:
        print("")
        remove_item = int(input("Which item would you like to remove? "))
        remove_item -= 1
        if remove_item >= len(items):
            print("Item is not in the list")
        else:
            items.pop(remove_item)
            prices.pop(remove_item)
            print(f"Item has been deleted")

    #COMPUTE TOTAL
    total = 0
    if action == 4:
        for price in prices:
            total += price
        print(f"The total price of the items in the shopping cart is {total}")

    # 5. QUIT
    if action == 5:
        run = False
        print("Thank you, come back again!")
