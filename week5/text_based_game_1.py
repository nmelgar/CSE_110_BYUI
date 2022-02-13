print("*********************************"
      "\n¡¡WORLD IS UNDER A NEW PANDEMIC!!"
      "\nPeople are becoming zombies that eat brains!"
      "\nYou will have to do everything to survive")
player_name = input("What's your name? ")
print(f"Hello {player_name.capitalize()}! Try to survive")
print("*********************************")


def death_function():
    print("You died :(")


def win_function():
    print(f"CONGRATULATIONS {player_name.capitalize()}! you survived...")
    print("for now.....")
    print("The END????")


print("You wake up in a hospital without knowing what happened, ",
      "\nmany ideas come to your mind and you don't know what you will do.")
hide_run = input("What will you do, HIDE or RUN?: ")
####FIRST SCENARIO OF THE GAME, USER DECIDES TO HIDE#######################################
# 1st IF-ELSE BLOCK
if hide_run.lower() == "hide":
    print(f"\nYou decided to {hide_run}. As you remain at the hospital, "
          "you find out \nthere are many people there, they are as confused as you."
          "\nYou realize few of them have name-tags in their chests, so you think "
          "\nit would be nice to have a partner to go with you.")

    partner_decision = input("What partner will you choose? MARTHA or KEN?: ")
    # CHOOSE PARTNER 1
    if partner_decision.lower() == "martha":
        print(f"You choose {partner_decision} as partner. While you speak about what "
              "you will do. You listen a lot of weird noises, people begin to run "
              "towards the exit.")
        print(f"A zombie comes really fast and attacks {partner_decision}."
              "\nShe begs for her life while forcing with the zombie to don't be bite.")
        fight_or_leave = input(
            "Will you fight with the zombie or let her die? FIGHT or LEAVE?: ")
        if fight_or_leave.lower() == "fight":
            print("While you were distracted a zombie attacked and bit you.")
            death_function()
        elif fight_or_leave.lower() == "leave":
            print(f"You decided to {fight_or_leave} and you kill the zombie."
                  "\nAs you run you see all the people running toward the cinema and hotel,"
                  "so you realize there aren't more option since all the ways are closed.")
            run_cinema_hotel_decision = input(
                "Where will you go? CINEMA or HOTEL?: ")
            if run_cinema_hotel_decision.lower() == "cinema":
                print(f"Many people are coming to the {run_cinema_hotel_decision} along with you."
                      "You are in, but zombies are inside too, so you can't go back."
                      "You can just go to the roof. You see the elevator is empty and not many people are using the stairs.")
                stairs_or_elevator = input(
                    "Which path will you take? ELEVATOR or STAIRS? ")
                if stairs_or_elevator.lower() == "elevator":
                    print(f"You took the {stairs_or_elevator} and it is moving fine."
                          "You arrive to the roof. Less than 20 people are there."
                          "2 helicopters arrive and you have to choose one as fast as you can"
                          " since the roof is full of crazy zombies")
                    helicopter_color = input(
                        "Which helicopter will you choose? GREEN or BLUE? ")
                    if helicopter_color.lower() == "green":
                        print(f"You took the {helicopter_color} helicopter."
                              "You feel safe, but a crash sounded at the back of the helicopter"
                              "Zombies are inside the helicopter! The pilot lost control and the helicopter crashes.")
                        death_function()
                    elif helicopter_color.lower() == "blue":
                        print(f"You took the {helicopter_color} helicopter."
                              f"You feel safe while along with {partner_decision} as the pilot drives to the mountains")
                        win_function()
                    else:
                        death_function()
                elif stairs_or_elevator.lower() == "stairs":
                    # print(f"You took the {stairs_or_elevator} and it is moving fine."
                    #       "While you are going up, it begins to shake and a zombie enters the elevator"
                    #       "from the top of it. You are so tired to fight")
                    print(f"You took the {stairs_or_elevator} and you run so fast, since there are 3 floors."
                          "While you are running so fast a zombie tackles you. You are so tired to fight")
                    death_function()
                else:
                    death_function()

            elif run_cinema_hotel_decision.lower() == "hotel":
                print(f"Many people are coming to the {run_cinema_hotel_decision} along with you."
                      "You are in, but zombies are inside too, so you can't go back."
                      "You can just go to the roof. You see the elevator is empty and not many people are using the stairs.")
                stairs_or_elevator = input(
                    "Which path will you take? ELEVATOR or STAIRS? ")
                if stairs_or_elevator.lower() == "stairs":
                    print(f"You took the {stairs_or_elevator} and have to run since many zombies run behind you."
                          "You arrive to the roof. Less than 20 people are there."
                          "2 helicopters arrive and you have to choose one as fast as you can"
                          " since the roof is full of crazy zombies")
                    helicopter_color = input(
                        "Which helicopter will you choose? GREEN or BLUE? ")
                    if helicopter_color.lower() == "blue":
                        print(f"You took the {helicopter_color} helicopter."
                              "You feel safe, but a crash sounded at the back of the helicopter"
                              "Zombies are inside the helicopter! The pilot lost control and the helicopter crashes.")
                        death_function()
                    elif helicopter_color.lower() == "green":
                        print(f"You took the {helicopter_color} helicopter."
                              "You feel safe while the pilot drives to the mountains")
                        win_function()
                    else:
                        death_function()
                elif stairs_or_elevator.lower() == "elevator":
                    print(f"You took the {stairs_or_elevator} and it is moving fine."
                          "While you are going up, it begins to shake and a zombie enters the elevator"
                          "from the top of it. You are so tired to fight")
                    death_function()
                else:
                    death_function()
        else:
            death_function()
    # CHOOSE PARTNER 2
    elif partner_decision.lower() == "ken":
        print(f"You choose {partner_decision} as partner. While you speak about what "
              "you will do. You listen a lot of weird noises, people begin to run "
              "towards the exit")
        print(f"A zombie comes really fast and attacks {partner_decision}."
              "\nShe begs for her life while forcing with the zombie to don't be bitten.")
        fight_or_leave = input(
            "Will you fight with the zombie or let him die? FIGHT or LEAVE?: ")
        if fight_or_leave.lower() == "fight":
            print(f"You decided to {fight_or_leave} and you kill the zombie."
                  "\nAs you run you see all the people running toward the cinema and hotel,"
                  "so you realize there aren't more option since all the ways are closed.")
            run_cinema_hotel_decision = input(
                "Where will you go? CINEMA or HOTEL?: ")
            if run_cinema_hotel_decision.lower() == "cinema":
                print(f"Many people are coming to the {run_cinema_hotel_decision} along with you."
                      "You are in, but zombies are inside too, so you can't go back."
                      "You can just go to the roof. You see the elevator is empty and not many people are using the stairs.")
                stairs_or_elevator = input(
                    "Which path will you take? ELEVATOR or STAIRS? ")
                if stairs_or_elevator.lower() == "elevator":
                    print(f"You took the {stairs_or_elevator} and it is moving fine."
                          "You arrive to the roof. Less than 20 people are there."
                          "2 helicopters arrive and you have to choose one as fast as you can"
                          " since the roof is full of crazy zombies")
                    helicopter_color = input(
                        "Which helicopter will you choose? GREEN or BLUE? ")
                    if helicopter_color.lower() == "green":
                        print(f"You took the {helicopter_color} helicopter."
                              "You feel safe, but a crash sounded at the back of the helicopter"
                              "Zombies are inside the helicopter! The pilot lost control and the helicopter crashes.")
                        death_function()
                    elif helicopter_color.lower() == "blue":
                        print(f"You took the {helicopter_color} helicopter."
                              f"You feel safe while along with {partner_decision} as the pilot drives to the mountains")
                        win_function()
                    else:
                        death_function()
                elif stairs_or_elevator.lower() == "stairs":
                    # print(f"You took the {stairs_or_elevator} and it is moving fine."
                    #       "While you are going up, it begins to shake and a zombie enters the elevator"
                    #       "from the top of it. You are so tired to fight")
                    print(f"You took the {stairs_or_elevator} and you run so fast, since there are 3 floors."
                          "While you are running so fast a zombie tackles you. You are so tired to fight")
                    death_function()
                else:
                    death_function()

            elif run_cinema_hotel_decision.lower() == "hotel":
                print(f"Many people are coming to the {run_cinema_hotel_decision} along with you."
                      "You are in, but zombies are inside too, so you can't go back."
                      "You can just go to the roof. You see the elevator is empty and not many people are using the stairs.")
                stairs_or_elevator = input(
                    "Which path will you take? ELEVATOR or STAIRS? ")
                if stairs_or_elevator.lower() == "stairs":
                    print(f"You took the {stairs_or_elevator} and have to run since many zombies run behind you."
                          "You arrive to the roof. Less than 20 people are there."
                          "2 helicopters arrive and you have to choose one as fast as you can"
                          " since the roof is full of crazy zombies")
                    helicopter_color = input(
                        "Which helicopter will you choose? GREEN or BLUE? ")
                    if helicopter_color.lower() == "blue":
                        print(f"You took the {helicopter_color} helicopter."
                              "You feel safe, but a crash sounded at the back of the helicopter"
                              "Zombies are inside the helicopter! The pilot lost control and the helicopter crashes.")
                        death_function()
                    elif helicopter_color.lower() == "green":
                        print(f"You took the {helicopter_color} helicopter."
                              "You feel safe while the pilot drives to the mountains")
                        win_function()
                    else:
                        death_function()
                elif stairs_or_elevator.lower() == "elevator":
                    print(f"You took the {stairs_or_elevator} and it is moving fine."
                          "While you are going up, it begins to shake and a zombie enters the elevator"
                          "from the top of it. You are so tired to fight")
                    death_function()
                else:
                    death_function()
        elif fight_or_leave.lower() == "leave":
            print("While you were distracted a zombie attacked and bit you.")
            death_function()
        else:
            death_function()
    else:
        death_function()
####THE OTHER SCENARIO OF THE GAME, USER DECIDES TO RUN#######################################
elif hide_run.lower() == "run":
    print(f"you chose {hide_run.capitalize()}")
    print(f"\nYou decided to {hide_run}. As you left the hospital, "
          "you find out \nthere are many people outthere, they are as confused as you."
          "\nYou realize this is a big problem, so you think "
          "\nyou need to take a fast decision in order to survive."
          "\nYou fastly consider to keep running, go to the cinema, or go the hotel.")
    ####MAIN DECISION###################
    run_cinema_hotel_decision = input(
        "What will you do? RUN, CINEMA or HOTEL?: ")
    ####FIRST DECISION###################
    if run_cinema_hotel_decision.lower() == "run":
        print(f"As you {run_cinema_hotel_decision} a zombie comes really fast and attacks an old woman."
              "\nShe begs for her life while forcing with the zombie to don't be bitten.")
        fight_or_leave = input(
            "Will you fight with the zombie or let her die? FIGHT or LEAVE?: ")
        if fight_or_leave.lower() == "fight":
            print(f"You decided to {fight_or_leave} and you kill the zombie."
                  "The old woman is really greatful with you. But now you are tired."
                  "\nAs you run you see all the people running toward the cinema and hotel,"
                  "so you realize there aren't more option since all the ways are closed.")
            run_cinema_hotel_decision = input(
                "Where will you go? CINEMA or HOTEL?: ")
            if run_cinema_hotel_decision.lower() == "cinema":
                print(f"Many people are coming to the {run_cinema_hotel_decision} along with you."
                      "You are in, but zombies are inside too, so you can't go back."
                      "You can just go to the roof. You see the elevator is empty and not many people are using the stairs.")
                stairs_or_elevator = input(
                    "Which path will you take? ELEVATOR or STAIRS? ")
                if stairs_or_elevator.lower() == "elevator":
                    print(f"You took the {stairs_or_elevator} and it is moving fine."
                          "You arrive to the roof. Less than 20 people are there."
                          "2 helicopters arrive and you have to choose one as fast as you can"
                          " since the roof is full of crazy zombies")
                    helicopter_color = input(
                        "Which helicopter will you choose? GREEN or BLUE? ")
                    if helicopter_color.lower() == "green":
                        print(f"You took the {helicopter_color} helicopter."
                              "You feel safe, but a crash sounded at the back of the helicopter"
                              "Zombies are inside the helicopter! The pilot lost control and the helicopter crashes.")
                        death_function()
                    elif helicopter_color.lower() == "blue":
                        print(f"You took the {helicopter_color} helicopter."
                              "You feel safe while the pilot drives to the mountains")
                        win_function()
                    else:
                        death_function()
                elif stairs_or_elevator.lower() == "stairs":
                    # print(f"You took the {stairs_or_elevator} and it is moving fine."
                    #       "While you are going up, it begins to shake and a zombie enters the elevator"
                    #       "from the top of it. You are so tired to fight")
                    print(f"You took the {stairs_or_elevator} and you run so fast, since there are 3 floors."
                          "While you are running so fast a zombie tackles you. You are so tired to fight")
                    death_function()
                else:
                    death_function()

            elif run_cinema_hotel_decision.lower() == "hotel":
                print(f"Many people are coming to the {run_cinema_hotel_decision} along with you."
                      "You are in, but zombies are inside too, so you can't go back."
                      "You can just go to the roof. You see the elevator is empty and not many people are using the stairs.")
                stairs_or_elevator = input(
                    "Which path will you take? ELEVATOR or STAIRS? ")
                if stairs_or_elevator.lower() == "stairs":
                    print(f"You took the {stairs_or_elevator} and have to run since many zombies run behind you."
                          "You arrive to the roof. Less than 20 people are there."
                          "2 helicopters arrive and you have to choose one as fast as you can"
                          " since the roof is full of crazy zombies")
                    helicopter_color = input(
                        "Which helicopter will you choose? GREEN or BLUE? ")
                    if helicopter_color.lower() == "blue":
                        print(f"You took the {helicopter_color} helicopter."
                              "You feel safe, but a crash sounded at the back of the helicopter"
                              "Zombies are inside the helicopter! The pilot lost control and the helicopter crashes.")
                        death_function()
                    elif helicopter_color.lower() == "green":
                        print(f"You took the {helicopter_color} helicopter."
                              "You feel safe while the pilot drives to the mountains")
                        win_function()
                    else:
                        death_function()
                elif stairs_or_elevator.lower() == "elevator":
                    print(f"You took the {stairs_or_elevator} and it is moving fine."
                          "While you are going up, it begins to shake and a zombie enters the elevator"
                          "from the top of it. You are so tired to fight")
                    death_function()
                else:
                    death_function()

        elif fight_or_leave.lower() == "leave":
            print("While you were distracted a zombie attacked and bit you.")
            death_function()
        else:
            death_function()
        ####SECOND DECISION###################
    elif run_cinema_hotel_decision.lower() == "cinema":
        print(f"Many people are coming to the {run_cinema_hotel_decision} along with you."
              "You are in, but zombies are inside too, so you can't go back."
              "You can just go to the roof. You see the elevator is empty and not many people are using the stairs.")
        stairs_or_elevator = input(
            "Which path will you take? ELEVATOR or STAIRS? ")
        if stairs_or_elevator.lower() == "elevator":
            print(f"You took the {stairs_or_elevator} and it is moving fine."
                  "You arrive to the roof. Less than 20 people are there."
                  "2 helicopters arrive and you have to choose one as fast as you can"
                  " since the roof is full of crazy zombies")
            helicopter_color = input(
                "Which helicopter will you choose? GREEN or BLUE? ")
            if helicopter_color.lower() == "green":
                print(f"You took the {helicopter_color} helicopter."
                      "You feel safe, but a crash sounded at the back of the helicopter"
                      "Zombies are inside the helicopter! The pilot lost control and the helicopter crashes.")
                death_function()
            elif helicopter_color.lower() == "blue":
                print(f"You took the {helicopter_color} helicopter."
                      "You feel safe while the pilot drives to the mountains")
                win_function()
            else:
                death_function()
        elif stairs_or_elevator.lower() == "stairs":
            # print(f"You took the {stairs_or_elevator} and it is moving fine."
            #       "While you are going up, it begins to shake and a zombie enters the elevator"
            #       "from the top of it. You are so tired to fight")
            print(f"You took the {stairs_or_elevator} and you run so fast, since there are 3 floors."
                  "While you are running so fast a zombie tackles you. You are so tired to fight")
            death_function()
        else:
            death_function()
        ####THIRD DECISION###################
    elif run_cinema_hotel_decision.lower() == "hotel":
        print(f"Many people are coming to the {run_cinema_hotel_decision} along with you."
              "You are in, but zombies are inside too, so you can't go back."
              "You can just go to the roof. You see the elevator is empty and not many people are using the stairs.")
        stairs_or_elevator = input(
            "Which path will you take? ELEVATOR or STAIRS? ")
        if stairs_or_elevator.lower() == "stairs":
            print(f"You took the {stairs_or_elevator} and have to run since many zombies run behind you."
                  "You arrive to the roof. Less than 20 people are there."
                  "2 helicopters arrive and you have to choose one as fast as you can"
                  " since the roof is full of crazy zombies")
            helicopter_color = input(
                "Which helicopter will you choose? GREEN or BLUE? ")
            if helicopter_color.lower() == "blue":
                print(f"You took the {helicopter_color} helicopter."
                      "You feel safe, but a crash sounded at the back of the helicopter"
                      "Zombies are inside the helicopter! The pilot lost control and the helicopter crashes.")
                death_function()
            elif helicopter_color.lower() == "green":
                print(f"You took the {helicopter_color} helicopter."
                      "You feel safe while the pilot drives to the mountains")
                win_function()
            else:
                death_function()
        elif stairs_or_elevator.lower() == "elevator":
            print(f"You took the {stairs_or_elevator} and it is moving fine."
                  "While you are going up, it begins to shake and a zombie enters the elevator"
                  "from the top of it. You are so tired to fight")
            death_function()
        else:
            death_function()
    else:
        death_function()

else:
    death_function()
