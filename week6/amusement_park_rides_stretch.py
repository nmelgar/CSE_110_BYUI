# 1. no under 36 inches may ride, alone or with other
# 2. usually 2 riders sit in the car together
# 2. a single rider if at least 18 yo and at leats 62 inches tall
# 3. if 2 riders and one of them is at
# 3. least 18 years old, they may ride together
first_rider_age = int(input("What is the age of the first rider?: "))
first_rider_height = int(input("What is the height of the first rider?: "))
second_rider = input("Is there a second rider (yes/no)? ")

if second_rider.capitalize() == "No":
    if first_rider_age >= 18 and first_rider_height >= 62:
        print("Enjoy your ride alone")
    elif first_rider_height < 36:
        print("Sorry you can't ride")
    else:
        print("Sorry you can't ride")
elif second_rider.capitalize() == "Yes":
    second_rider_age = int(input("What is the age of the second rider?: "))
    second_rider_height = int(
        input("What is the height of the second rider?: "))

    if first_rider_age >= 18 or second_rider_age >= 18:
        if first_rider_height < 36 or second_rider_height < 36:
            print("Sorry you can't ride")
        else:
            print("Welcome to the ride. Please be safe and have fun!")
    # If there are two riders, but neither one is at least 18 years old, they may still
    # ride as long as they are both at least 12 years old and at least 52 inches tall.
    elif (first_rider_age >= 12 and second_rider_age >= 12) and (first_rider_height >= 52 and second_rider_height >= 52):
        print("Welcome to the ride. Please be safe and have fun!")
    else:
        print("Sorry you can't ride")
