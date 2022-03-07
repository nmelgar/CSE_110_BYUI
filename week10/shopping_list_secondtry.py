list_of_items = []
run = True

while run:
    item_in_list = str(input("Please enter the items of the shopping list (type: 'quit' to finish) "))
    if item_in_list != "quit":
        list_of_items.append(item_in_list)
    if item_in_list == "quit":
        run = False

print("\nThe shopping list is: ")
for item in list_of_items:
    print(item.capitalize())

print("\nThe shopping list with indexes is: ")
for index in range(len(list_of_items)):
    item = list_of_items[index]
    print(f"{index}. {item}")

item_to_change = int(input("\nWhat item would you like to change? (type a number) "))
new_item = str(input("What is the new item? "))

list_of_items.insert(item_to_change, new_item)

print("\nThe shopping list with indexes is: ")
for index in range(len(list_of_items)):
    item = list_of_items[index]
    print(f"{index}. {item}")

