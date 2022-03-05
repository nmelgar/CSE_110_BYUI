print("Add the name of your friends to a list")
print('Type "end" to stop adding friends to the list')

friends = []
new_friend = ""

while new_friend != "end":
    new_friend = str(input("Type the of a friend: "))
    
    if new_friend != "end":
        friends.append(new_friend)

print("Your friends are: ")
for friend in friends:
    print(friend)
    
