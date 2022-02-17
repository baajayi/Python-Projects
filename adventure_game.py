print("***Welcome to my adventure game***")
print("Your options are the words in CAPITALS")
choice_one = input("You are feeling adventurous today. You packed your bags and off to the bus park you go. Do you take a BUS or a LORRY? \n")
if choice_one.lower() == "bus":
    choice_one_one = input("The bus takes you straight to the entrance to the island of Ikono where you can only CRAWL or CLIMB to enter. What do you do? \n")
    if choice_one_one.lower() == "CRAWL":
        choice_one_one_two = input("You crawl into a lion's den who then makes a voiolent attempt at you. What do you do? do you stay STILL or lie FLAT on the ground or ATTACK the lion first? \n")
        if choice_one_one_two.lower() == "still":
            print("The lion looks away and you can quietly crawl back out of the den and go home. You live, you win the game.")
        elif choice_one_one_two.lower() == "flat":
            print("The lion walks past you, leaves the den, and so you can quietly get out of the den and you can go home peacefully. You live, you win the game.")
        elif choice_one_one_two.lower() == "attack":
            print("You attack a lion? Are you a normal human being? well, the lion attacks you only for you to wake up, it was a dream, you live and you win")
        else:
            print("You made the wrong input, you lost the game, start allover again")
    elif choice_one_one.lower() == "climb":
        choice_one_two = input("You chose to climb a tree and you meet a live python on the third level of climbing. Do you HANG there, JUMP down or THROW a stick at the python? \n")
        if choice_one_two.lower() == "HANG":
            print("You hang in there, the python goes its way and you live and you win")
        elif choice_one_two.lower() == "jump":
            print("Well, you jumped to safety, you win")
        elif choice_one_two.lower() == "throw":
            print("You throw a stick at a python? The python charges towards you and just as it is about to strike your face, you wake up, it's a dream, you are safe and you win")
        else:
            print("You made an invalid entry, you lose the game and have to start all over again")
    else:
        print("You have made an invalid entry, you lost the game and would have to start all over again.")