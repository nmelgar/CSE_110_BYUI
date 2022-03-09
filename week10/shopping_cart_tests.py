from os import remove


action = ""
items = ["ITEM1", "ITEM2", "ITEM3"]
prices = [25.2, 45.3, 67.2]
run = True



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
        print(f"The total price of the items in the shopping cart is ${total: .2f}")

    # 5. QUIT
    if action == 5:
        run = False
        print("Thank you, come back again!")
