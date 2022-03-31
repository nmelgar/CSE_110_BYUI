message = input("What is your message? ")

# Receives a string and prints it out, exactly as received.
def display_regular():
    print(message)
# Receives a string, converts it to upper case, and then prints it out.
def display_uppercase():
    print(message.upper())

# Receives a string, converts it to lower case, and then prints it out.
def display_lowercase():
    print(message.lower())

display_regular()
display_uppercase()
display_lowercase()
