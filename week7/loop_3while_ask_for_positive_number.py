number = int(input("Please type a positive number: "))

while number < 0:
    print("Sorry, that is negative number. Please try again.")
    number = int(input("Please type a positive number: "))
print(f"The number is {number}")