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
    for index in range(len(menu)):
        menu_item = menu[index]
        print(f"{index + 1}. {menu_item}")

    action = int(input("\nPlease enter an action: "))

    add_item = ""
    add_price = ""

    if action <= len(menu):
        #IF 0 as INVALID NUMBER
        if action == 0:
            print("Please try a valid number!")

        # 1. ADD ITEM
        if action == 1:
            add_item = str(input("\nWhat item would you like to add? "))
            items.append(add_item)
            add_price = (float(input(f"What is the price of {add_item}? ")))
            prices.append(add_price)
            print(f"'{add_item.capitalize()}' has been added to the cart")

        # 2. VIEW CART
        if action == 2:
            if len(items) == 0:
                print("The shopping cart is empty")
            else:
                total_items = 1
                print("The contents of the shopping cart are:")
                for index in range(len(items)):
                    add_item = items[index]
                    add_price = prices[index]
                    print(f"{index +1}. {add_item.capitalize()} - ${add_price: .2f}")

                    #count the number of items in the cart
                    total_items += index 
                    if total_items == 1:
                        print(f"\nThere is {total_items} item in the cart")
                    else:
                        print(f"\nThere are {total_items} items in the cart")

        #3. REMOVE AN ITEM
        if action == 3:
            if len(items) == 0:
                print("There are not items to remove")
            else:
                print("")
                remove_item = int(input("Which item would you like to remove? "))
                remove_item -= 1
                if remove_item >= len(items):
                    print("Item is not in the list")
                else:
                    items.pop(remove_item)
                    prices.pop(remove_item)
                    print(f"Item has been deleted")

        #4. COMPUTE TOTAL
        total_cost = 0
        if action == 4:
            if len(items) == 0:
                print("There are not items in the list to get the total")
            else:
                for price in prices:
                    total_cost += price
                print(f"The total price of the items in the shopping cart is ${total_cost: .2f}")

        # 5. QUIT
        if action == 5:
            run = False
            print("Thank you, come back again!")

    else:
        print("Please try a valid number!")
