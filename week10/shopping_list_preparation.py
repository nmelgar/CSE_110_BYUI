run = True
list_of_items = []

while run:
    items_input = str(input("Please enter the items of the shopping list(type: 'quit' to finish) "))
    if items_input != "quit":
        list_of_items.append(items_input)
    if items_input == "quit":
        run = False

print("\nThe shopping list is:")
for item in list_of_items:
    print(item)

print("\nThe shopping list with indexes is:")
for i in range(len(list_of_items)):
    item = list_of_items[i]
    print(f"{i}. {item}")

change_item = int(input("What item would you like to change? (type the number) "))
new_item = str(input("What is the new item? "))

list_of_items.pop(change_item)
#insert the item to change at the specific position
list_of_items.insert(change_item, new_item)

print("\nThe shopping list with indexes is:")
for i in range(len(list_of_items)):
    item = list_of_items[i]
    print(f"{i}. {item}")



