print("WELCOME TO MAD LIBS")
print("-----------------------------------")
print("Let's start!")
user_number = input("\nChoose a number between 1 and 3: ")

if user_number == "1":
    print(f"You chose {user_number}")
    plural_noun = input("\nEnter a plural noun: ")
    plural_noun_1 = input("Enter another plural noun: ")
    verb = input("Enter a verb: ")
    story_1 = (f"\nWhen I go to the arcade with my {plural_noun}"
               " there are lots of games to play. \nI spend "
               "lots of time there with my friends. In the game X-Men "
               f"you can be different {plural_noun_1}. \nThe "
               f"point of the game is to {verb} every "
               "robot. You also need to save people. \nThen you can "
               "go to the next level."
               "\nI need to visit arcade more frequently!")
    print("---------------------------------------------------")
    print(story_1)
    print("---------------------------------------------------")

elif user_number == "2":
    print(f"You chose {user_number}")
    proper_noun = input("\nEnter a person's name: ")
    noun = input("Enter a noun: ")
    adjective = input("Enter an adjective(feeling): ")
    verb = input("Enter a verb: ")
    adjective_2 = input("Enter another adjective(feeling): ")
    animal = input("Enter an animal (in plural): ")
    story_2 = (f"\nThis weekend I am going camping with {proper_noun}."
               f"\nI packed my lantern, sleeping bag, and {noun}. "
               f"\nI am so {adjective} to {verb} in a tent."
               f"\nI am {adjective_2} we might see {animal}, "
               "they are kind of dangerous."
               "\nI have high hopes about this camping!")

    print("---------------------------------------------------")
    print(story_2)
    print("---------------------------------------------------")

elif user_number == "3":
    print(f"You chose {user_number}")
    verb = input("\nEnter a verb: ")
    color = input("Enter a color: ")
    verb_ing = input("Enter a verb ending in ing: ")
    adverb = input("Enter an adverb ending in ly: ")
    number = input("Enter a number: ")
    time = input("Enter a measure of time: ")
    story_3 = (f"\nI love camping, as in previous stories, it is amazing!"
               f"\nToday we are going to hike, fish, and {verb}."
               f"\nI have heard that the {color} lake is great for {verb_ing}."
               f"\nThen we will {adverb} hike through the forest for {number} {time}."
               "\nIt seems it will be an amazing camping day!")
    print("---------------------------------------------------")
    print(story_3)
    print("---------------------------------------------------")

else:
    print("OOPss!!! Please choose a number between 1 and 5")
