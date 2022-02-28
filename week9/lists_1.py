clients = []

# create the list like this if you know what the elements are
# clients = ["emily", "john", "ana"]

# if you dont know what the elements are
# you can append the elements to the list
# clients.append("mary")

new_client =""
while len(clients) < 6:
    new_client = input("What's the name of the client? ")
    clients.append(new_client)

for client in clients:
    print(client)

# clients_length = len(clients)
# print(clients_length)