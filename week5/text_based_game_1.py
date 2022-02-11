place = ["hotel", "cinema"]
way = ["stairs", "elevator"]
action = ["fight", "stop fighting", "run", "hide"]
state = ["win", "lose"]
vehicle = ["green", "blue"]
weapon = ["bat", "gun"]
partner = ["martha", "ken"]


def death_function():
    print("You died :(")


print("*********************************")
print("¡¡WORLD IS UNDER A NEW PANDEMIC!!")
print("People are becoming zombies that eat brains!")
print("You will have to do everything to survive")
print("*********************************")

print("You wake up in a hospital without knowing what happened, ",
      "\nmany ideas come to your mind and you don't know what you will do.")
hide_run = input("What will you do, HIDE or RUN?: ")
# 1st IF-ELSE BLOCK
if hide_run.lower() == "hide":
    print(f"You decided to {hide_run}. As you remain at the hospital, "
          "you find out \nthere are many people there, they are as confused as you."
          "\nYou realize few of them have name-tags in their chests, so you think "
          "\nit would be nice to have a partner to go with you.")
    partner_decision = input("What partner will you choose? MARTHA or KEN?: ")
    if partner_decision.lower == "martha":
        print(f"You choose {partner_decision} as partner. While you speak about what "
              "you will do. You listen a lot of weird noises, people begin to run "
              "towards the exit")
    elif partner_decision.lower == "ken":
        print(f"You choose {partner_decision} as partner. While you speak about what "
              "you will do. You listen a lot of weird noises, people begin to run "
              "towards the exit")
    else:
        death_function()
elif hide_run.lower() == "run":
    print(f"you chose {hide_run.capitalize()}")
    print(f"You decided to {hide_run}, ")
else:
    death_function()
