#Check Point Project: Terminal Adventure Game
import random
import stats_player_monster
import fight_turns
import training_instance

running = True
menu = True
first_enter = True
first_food = True
first_login = True

first_training = 0
drunk = 0
local = 0
flee_attempt = 0
home_local_training = 1

ME_HP = stats_player_monster.ME_HP
PW_HP = stats_player_monster.PW_HP

while running:
    
    while menu:
        if first_login:
            print(" _______________________________________ ")
            print("|                                       |")
            print("|  Welcome to Terminal Adventure Game!  |")
            print("|_______________________________________|")
            first_login = False
            print(" ____________________________ ")
            print("|                            |")
            print("|   Choose game difficult:   |")
            print("|   1 - Easy.                |")
            print("|   2 - Hard.                |")
            print("|____________________________|")
            difficult = int(input(""))
            print(" ________________________ ")
            print("|                        |")
            print("|   Choose your class:   |")
            print("|   1 - Warrior.         |")
            print("|   2 - Mage.            |")
            print("|________________________|")
            player = int(input(""))
        else:
            print(" _______________________________ ")
            print("|                               |")
            print("|   Where do you wanto to go?   |")
            print("|   1 - House.                  |")
            print("|   2 - Tavern.                 |")
            print("|   3 - Dungeon.                |")
            print("|   0 - Exit Game.              |")
            print("|_______________________________|")
            print("")
            local = int(input(""))
            print("")
            menu = False
        if local > 0 or local <= 4:

            while local == 1: #Way to House
                if drunk == 5: #If get drunk in tavern will be carried to home
                    print("You remmember the sound of your house's door...")
                    first_enter == False 
                else:
                    if first_enter and drunk != 4: #If going to home first time print message, else only get options
                        print("You open the door and feel the warm of your home...")
                        first_enter = False
                    print(" __________________________________ ")
                    print("|                                  |")
                    print("|   In your house you decide to:   |")
                    print("|   1 - Go to bed.                 |")
                    print("|   2 - Eat something.             |")
                    print("|   3 - Pratice some skills.       |")
                    print("|   4 - Leave home.                |")
                    print("|   0 - Exit Game.                 |")
                    print("|__________________________________|")
                    print("")
                    home_local = int(input(""))
                if home_local == 1: #Go to bed sleep
                    if drunk == 5: #Wakeup after get drunk in tavern
                        print("")
                        print("You are so drunk and didn't remmember nothing...")
                        print("The people of village get you to your house...")
                        print("You feel an severe headache")
                        print("")
                        drunk = 4
                    else: #Normal choice to sleep
                        print("")
                        print("Time to rest, take a breath, relax and prepare to a new day.")
                        print(".")
                        print(".")
                        print(".")
                        print("You wake up feeling much better, ready to new adventure's day.")
                        print("")
                        fight_turns.reset_PHP()
                        drunk = 0 #Ends drunk state.
                        first_training = 0 #Able to pratice skills again.
                        first_food == True #Able to eat again.
                elif home_local == 2: #Get something to eat.
                    if first_food == False: #Can't eat much
                        print("")
                        print("You are full and can't eat more..")
                        print("")
                    else: #First time eating
                        print("")
                        print("You take the best of your hunting and eat some pieces grilled in firepit.")
                        print(".")
                        print(".")
                        print(".")
                        print("You're satisfied and happy.")
                        print("")
                        fight_turns.reset_PHP()
                        drunk = 0
                        first_food = False #Full to eat again.
                        first_training = 0 #Reenergized to pratice skills again.
                elif home_local == 3 and first_training <= 1: #Pratice skills    
                    home_local_training = 1
                    while home_local_training == 1:
                        if first_training <= 1: #Can't pratice so much, get exausted.
                            print(first_training)    
                            print(" _________________________________ ")
                            print("|                                 |")
                            print("|   What skill to pratice today?  |")
                            print("|   1 - Attack.                   |")
                            print("|   2 - Magic.                    |")
                            print("|   3 - Defense.                  |")
                            print("|   0 - Stop Training.            |")
                            print("|_________________________________|")
                            print("")
                            home_local3 = int(input(""))
                            if home_local3 == 1 and first_training <= 1: #Attack
                                first_training += 1
                                training_instance.training_loop(home_local3, player)
                            elif home_local3 == 2 and first_training <= 1: #Magic
                                first_training += 1
                                training_instance.training_loop(home_local3, player)
                            elif home_local3 == 3 and first_training <= 1: #Defense
                                first_training += 1
                                training_instance.training_loop(home_local3, player)
                            elif home_local3 == 0: #Leave
                                print("")
                                print("You just decide to not pratice now.")
                                print("")
                                home_local_training = 0 #Leave pratice option, and go to home options.
                            else:
                                print("")
                                print("Please chose a valid skill to pratice.")
                                print("")
                        elif first_training > 1:#Can't pratice so much, get exausted.
                            print("")
                            print("You're exausted now, try to rest and pratice later.")
                            print("")
                            home_local_training = 0 #Leave pratice option, and go to home options.
                elif home_local == 3 and first_training > 1:
                    print("")
                    print("You're exausted now, try to rest and pratice later.")
                    print("")
                elif home_local == 4: #Get out home
                    print("")
                    print("You open the door and feel the wind of nature...")
                    print("")
                    local = 0 #Leave home options and open menu again.
                    menu = True #To open Menu again
                    first_enter = True #Makes enter in House/Tavern/Dungeon/Forest the "first time message" show again.
                elif home_local == 0: #Leave game
                    local = 0 
                    running = False #Break the running to stop game run.
                else: #Invalid output
                    print("")
                    print ("Please chose a valid action to do.")
                    print("")
                    
            while local == 2: #Way to Tavern
                if first_enter: #First entering the Tavern
                    print("")
                    print("You hear the sound of music and people talking...")
                    print("open an old wooden door and see the bigger tavern you've ever seen.")
                    print("")
                    first_enter = False
                print(" _______________________________ ")
                print("|                               |")
                print("|   What do you do in Tavern?   |")
                print("|   1 - Take a beer.            |")
                print("|   2 - Take a pork pie.        |")
                print("|   3 - Time to Leave.          |")
                print("|   0 - Exit Game.              |")
                print("|_______________________________|")
                print("")    
                tavern_local = int(input(""))
                if tavern_local == 1: #Take a beer
                    if drunk == 3: #If get much beer you'll pass out drunk
                        tavern_local = 3 #To Leave Tavern
                        local = 1 #Direct to House.
                        home_local = 1 #Direct to bed.
                        break 
                    print("")
                    print("Nothing better than a beer!!!")
                    print(".")
                    print(".")
                    print(".")
                    print("You feel little drunk.")
                    print("")
                    drunk += 1 #Increase drunk state
                elif tavern_local == 2: #Get a Food
                    if first_food == False: #Can't eat so much.
                        print("")
                        print("You are full and can't eat more..")
                        print("")
                    else:
                        print("")
                        print("The smell of pork pie is incredible, you eat it only in few bites.")
                        print(".")
                        print(".")
                        print(".")
                        print("The best pie of the region.")
                        print("")
                elif tavern_local == 3: #Just leave Tavern
                    print("")
                    print("You paid for your items and leave.")
                    print("")
                    local = 0
                    menu = True
                    first_enter = True
                    break
                elif tavern_local == 0: #Leave Game
                    local = 0
                    running = False
                else: #Invalid output
                    print("")
                    print("Please chose a valid item from menu.")
                    print("")

            while local == 3: #Way to Dungeon
                if first_enter: #First entering the dungeon
                    print("")
                    print("... ... ... ...")
                    print("You see a huge way inside the mountais, there is no light, the sound of your steps echoes trough the wet stone walls")
                    print("")
                    first_enter = False
                print(" __________________________ ")
                print("|                          |")
                print("|   Chose a way:           |")
                print("|   1 - Go deep.           |")
                print("|   0 - Leave this cave.   |")
                print("|__________________________|")
                print("")
                dungeon_local = int(input(""))
                if dungeon_local == 1: #Go deep inside Dungeon.
                    test = random.randint(1,10) #Check to Fight.
                    if test <= 6:
                        print("")
                        print("A terrible creature emerges from the shadows and attacks you...")
                        print("")
                        fight_turns.fight_loop(difficult, player)
                        if fight_turns.PW_HP <= 0 or fight_turns.PM_HP <= 0:
                            running = False
                            break
                    else:
                        print("You go deeper and feel the heavy atmosphere, the cold in your bones, some scratches on the mountain rocks... you feel a shiver and...")
                elif dungeon_local == 0: #Leave this place for monsters
                    print("Better leave this dreadfull place...")
                    local = 0
                    menu = True
                    first_enter = True

                else:
                    print("Please chose a valid option.")      

    if local == 0: #Exit Game
            print("Goodbye, come back latter to more adventures.")
            running = False
    elif local < 0 and local > 4: #Invalid Menu Output
            print("Please chose a valid location to go.")