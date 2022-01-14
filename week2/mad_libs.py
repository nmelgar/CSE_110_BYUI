print("WELCOME TO MAD LIBS")
print("-----------------------------------")
print("Let's start!")
user_number = input("Choose a number between 1 and 5: ")

if user_number == "1":
    print(f"You chose {user_number}")
    plural_noun = input("Enter a plural noun: ")
    plural_noun_2 = input("Enter another plural noun: ")
    verb = input("Enter a verb: ")
    story_1 = (f"When I go to the arcade with my {plural_noun}"
               " there are lots of games to play. \nI spend"
               "lots of time there with my friends. In the game X-Men "
               f"you can be different {plural_noun_2}. \nThe "
               f"point of the game is to {verb} every "
               "robot. You also need to save people. \nThen you can "
               "go to the next level.")
    print(story_1)
elif user_number == "2":
    print("You chose 2")
elif user_number == "3":
    print("You chose 3")
elif user_number == "4":
    print("You chose 4")
elif user_number == "5":
    print("You chose 5")
else:
    print("OOPss!!! Please choose a number between 1 and 5")
