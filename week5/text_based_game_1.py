place = ["hotel", "cinema"]
way = ["stairs", "elevator"]
action = ["fight", "stop fighting", "run", "hide"]
state = ["win", "lose"]
vehicle = ["green", "blue"]
weapon = ["bat", "gun"]
partner = ["martha", "ken"]

print("*********************************")
print("¡¡WORLD IS UNDER A NEW PANDEMIC!!")
print("People are becoming zombies that eat brains!")
print("You will have to do everything to survive")
print("*********************************")

print("You wake up in a hospital without knowing what happened, ",
"\nmany ideas come to your mind and you don't know what you will do.")
hide_run = input("What will you do, HIDE or RUN?: ")
if hide_run.lower() == "run":
    print(f"you chose {hide_run.capitalize()}")
    print(f"You decided to {hide_run}, now you need to choose your weapon")

elif hide_run.lower() == "hide":
    print(f"you chose {hide_run.capitalize()}")
    print(f"You decided to {hide_run}, now you need to choose your weapon")

else:
    print("You died :(")