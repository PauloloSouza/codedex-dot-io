#Fight Turns

import random
import stats_player_monster

global running
is_fighting = True
flee_attempt = 0

PW_HP = stats_player_monster.PW_HP
PM_HP = stats_player_monster.PM_HP
ME_HP = stats_player_monster.ME_HP
MH_HP = stats_player_monster.MH_HP

def reset_MHP(): #Reset Monsters HP (Easy and Hard) 
    global ME_HP, MH_HP
    ME_HP = stats_player_monster.ME_HP
    MH_HP = stats_player_monster.MH_HP

def reset_PHP(): #Reset Players HP (Mage and Warrior)
    global PW_HP, PM_HP
    PW_HP = stats_player_monster.PW_HP
    PM_HP = stats_player_monster.PM_HP

def atk_war_vs_me(): #Attack Instance (Warrior versus Monster Easy)
    global ME_HP, MH_HP, PW_HP, PM_HP, is_fighting, fight, flee_attempt
    
    #Calculate damage
    damage_war = random.randint(stats_player_monster.warrior[0], stats_player_monster.warrior[1])
    #damage_mage = random.randint(stats_player_monster.mage[0], stats_player_monster.mage[1])
    damage_me = random.randint(stats_player_monster.monster_e[0], stats_player_monster.monster_e[1])
    #damage_mh = random.randint(stats_player_monster.monster_h[0], stats_player_monster.monster_h[1])
    
    #Apply Player Damage
    ME_HP -= damage_war
    #ME_HP -= damage_mage
    #MH_HP -= damage_war
    #MH_HP -= damage_mage

    #Apply Monster Damage
    PW_HP -= damage_me
    #PW_HP -= damage_mh
    #PM_HP -= damage_me
    #PM_HP -= damage_mh

    #Print results
    print("")
    print(damage_war)
    print(f"You deal {damage_war} damage, to monster.")
    print(f"Monster's life {ME_HP}")
    print("")
    if ME_HP > 0:
        print(damage_me)
        print(f"You recive {damage_me} damage")
        print(f"Your life {PW_HP}")
        print("")

    if ME_HP <= 0:
        PW_HP += damage_me
        print(f"{ME_HP}, monster died.")
        is_fighting = False
        fight = False
        flee_attempt = 0
    else:
        print("Monster's life: " + str(ME_HP))
    if PW_HP <= 0:
        print(f"{PW_HP}, you died... game over!")
        is_fighting = False
        fight = False
        running = False
    else:
        print("Player's life: " + str(PW_HP))

def atk_war_vs_mh(): #Attack Instance (Warrior versus Monster Hard)
    global ME_HP, MH_HP, PW_HP, PM_HP, is_fighting, fight, flee_attempt
    
    #Calculate damage
    damage_war = random.randint(stats_player_monster.warrior[0], stats_player_monster.warrior[1])
    #damage_mage = random.randint(stats_player_monster.mage[0], stats_player_monster.mage[1])
    #damage_me = random.randint(stats_player_monster.monster_e[0], stats_player_monster.monster_e[1])
    damage_mh = random.randint(stats_player_monster.monster_h[0], stats_player_monster.monster_h[1])
    
    #Apply Player Damage
    #ME_HP -= damage_war
    #ME_HP -= damage_mage
    MH_HP -= damage_war
    #MH_HP -= damage_mage

    #Apply Monster Damage
    #PW_HP -= damage_me
    PW_HP -= damage_mh
    #PM_HP -= damage_me
    #PM_HP -= damage_mh

    #Print results
    print("")
    print(damage_war)
    print(f"You deal {damage_war} damage, to monster.")
    print(f"Monster's life {MH_HP}")
    print("")
    if MH_HP > 0:
        print(damage_mh)
        print(f"You recive {damage_mh} damage")
        print(f"Your life {PW_HP}")
        print("")

    if MH_HP <= 0:
        PW_HP += damage_mh
        print(f"{MH_HP}, monster died.")
        is_fighting = False
        fight = False
        flee_attempt = 0
    else:
        print("Monster's life: " + str(MH_HP))
    if PW_HP <= 0:
        print(f"{PW_HP}, you died... game over!")
        is_fighting = False
        fight = False
        running = False
    else:
        print("Player's life: " + str(PW_HP))

def atk_mag_vs_me(): #Attack Instance (Mage versus Monster Easy)
    global ME_HP, MH_HP, PW_HP, PM_HP, is_fighting, fight, flee_attempt
    
    #Calculate damage
    #damage_war = random.randint(stats_player_monster.warrior[0], stats_player_monster.warrior[1])
    damage_mage = random.randint(stats_player_monster.mage[0], stats_player_monster.mage[1])
    damage_me = random.randint(stats_player_monster.monster_e[0], stats_player_monster.monster_e[1])
    #damage_mh = random.randint(stats_player_monster.monster_h[0], stats_player_monster.monster_h[1])
    
    #Apply Player Damage
    #ME_HP -= damage_war
    ME_HP -= damage_mage
    #MH_HP -= damage_war
    #MH_HP -= damage_mage

    #Apply Monster Damage
    #PW_HP -= damage_me
    #PW_HP -= damage_mh
    PM_HP -= damage_me
    #PM_HP -= damage_mh

    #Print results
    print("")
    print(damage_mage)
    print(f"You deal {damage_mage} damage, to monster.")
    print(f"Monster's life {ME_HP}")
    print("")
    if ME_HP > 0:
        print(damage_me)
        print(f"You recive {damage_me} damage")
        print(f"Your life {PM_HP}")
        print("")

    if ME_HP <= 0:
        PM_HP += damage_me
        print(f"{ME_HP}, monster died.")
        is_fighting = False
        fight = False
        flee_attempt = 0
    else:
        print("Monster's life: " + str(ME_HP))
    if PM_HP <= 0:
        print(f"{PM_HP}, you died... game over!")
        is_fighting = False
        fight = False
        running = False
    else:
        print("Player's life: " + str(PM_HP))

def atk_mag_vs_mh(): #Attack Instance (Mage versus Monster Hard)
    global ME_HP, MH_HP, PW_HP, PM_HP, is_fighting, fight, flee_attempt
    
    #Calculate damage
    #damage_war = random.randint(stats_player_monster.warrior[0], stats_player_monster.warrior[1])
    damage_mage = random.randint(stats_player_monster.mage[0], stats_player_monster.mage[1])
    #damage_me = random.randint(stats_player_monster.monster_e[0], stats_player_monster.monster_e[1])
    damage_mh = random.randint(stats_player_monster.monster_h[0], stats_player_monster.monster_h[1])
    
    #Apply Player Damage
    #ME_HP -= damage_war
    #ME_HP -= damage_mage
    #MH_HP -= damage_war
    MH_HP -= damage_mage

    #Apply Monster Damage
    #PW_HP -= damage_me
    #PW_HP -= damage_mh
    #PM_HP -= damage_me
    PM_HP -= damage_mh

    #Print results
    print("")
    print(damage_mage)
    print(f"You deal {damage_mage} damage, to monster.")
    print(f"Monster's life {MH_HP}")
    print("")
    if MH_HP > 0:
        print(damage_mh)
        print(f"You recive {damage_mh} damage")
        print(f"Your life {PM_HP}")
        print("")

    if MH_HP <= 0:
        PM_HP += damage_mh
        print(f"{MH_HP}, monster died.")
        is_fighting = False
        fight = False
        flee_attempt = 0
    else:
        print("Monster's life: " + str(MH_HP))
    if PM_HP <= 0:
        print(f"{PM_HP}, you died... game over!")
        is_fighting = False
        fight = False
        running = False
    else:
        print("Player's life: " + str(PM_HP))

def def_war_vs_me(): #Defense Instance (Warrior versus Monster Easy)
    global ME_HP, MH_HP, PW_HP, PM_HP, is_fighting, fight, flee_attempt

    defense = random.randint(1,3)
    if defense == 1: #Defense Successful
        print("")
        print("You raise your shield and block incoming atack!")
        print("")
    elif defense == 2: #Hit in armor
        print("")
        print("You didn't have enough reflexes and get hit in your armor...")
        print("")
        #Calculate hit damage
        damage_me = random.randint(stats_player_monster.monster_e[0], stats_player_monster.monster_e[1])
        block_damage = damage_me / stats_player_monster.PW_defense
        PW_HP -= block_damage
        PW_HP = round(PW_HP, 0)
        print("")
        print(f"You recived {block_damage}")
        print(f"Your life {PW_HP}")
        print("")

        if PW_HP <= 0:
            print("")
            print(f"{PW_HP}, you died... game over!")
            print("")
            is_fighting = False
            fight = False
        else:
            print("Player's life: " + str(PW_HP))
            print("")
    else: #Defense unsuccessful
        print("")
        print("The creature walks in the shadowns and hit your back... you don't know how it can be so fast....")
        damage_me = random.randint(stats_player_monster.monster_e[0], stats_player_monster.monster_e[1])
        PW_HP -= damage_me
        print("")
        print(f"You recived {damage_me}")
        print(f"Your life {PW_HP}")
        print("")
        if PW_HP <= 0: #Player's HP = 0, game over.
            print("")
            print(f"{PW_HP}, you died... game over!")
            print("")
            is_fighting = False
            fight = False
        else:
            print("Player's life: " + str(PW_HP))
            print("")

def def_war_vs_mh(): #Defense Instance (Warrior versus Monster Hard)
    global ME_HP, MH_HP, PW_HP, PM_HP, is_fighting, fight, flee_attempt

    defense = random.randint(1,3)
    if defense == 1: #Defense Successful
        print("")
        print("You raise your shield and block incoming atack!")
        print("")
    elif defense == 2: #Hit in armor
        print("")
        print("You didn't have enough reflexes and get hit in your armor...")
        print("")
        #Calculate hit damage
        damage_mh = random.randint(stats_player_monster.monster_h[0], stats_player_monster.monster_h[1])
        block_damage = damage_mh / stats_player_monster.PW_defense
        PW_HP -= block_damage
        PW_HP = round(PW_HP, 0)
        print("")
        print(f"You recived {block_damage}")
        print(f"Your life {PW_HP}")
        print("")

        if PW_HP <= 0:
            print("")
            print(f"{PW_HP}, you died... game over!")
            print("")
            is_fighting = False
            fight = False
        else:
            print("Player's life: " + str(PW_HP))
            print("")
    else: #Defense unsuccessful
        print("")
        print("The creature walks in the shadowns and hit your back... you don't know how it can be so fast....")
        damage_mh = random.randint(stats_player_monster.monster_h[0], stats_player_monster.monster_h[1])
        PW_HP -= damage_mh
        print("")
        print(f"You recived {damage_mh}")
        print(f"Your life {PW_HP}")
        print("")
        if PW_HP <= 0: #Player's HP = 0, game over.
            print("")
            print(f"{PW_HP}, you died... game over!")
            print("")
            is_fighting = False
            fight = False
        else:
            print("Player's life: " + str(PW_HP))
            print("")

def def_mag_vs_me(): #Defense Instance (Mage versus Monster Easy)
    global ME_HP, MH_HP, PW_HP, PM_HP, is_fighting, fight, flee_attempt

    defense = random.randint(1,3)
    if defense == 1: #Defense Successful
        print("")
        print("You raise your shield and block incoming atack!")
        print("")
    elif defense == 2: #Hit in armor
        print("")
        print("You didn't have enough reflexes and get hit in your armor...")
        print("")
        #Calculate hit damage
        damage_me = random.randint(stats_player_monster.monster_e[0], stats_player_monster.monster_e[1])
        block_damage = damage_me / stats_player_monster.PM_defense
        PM_HP -= block_damage
        PM_HP = round(PM_HP, 0)
        print("")
        print(f"You recived {block_damage}")
        print(f"Your life {PM_HP}")
        print("")

        if PM_HP <= 0:
            print("")
            print(f"{PM_HP}, you died... game over!")
            print("")
            is_fighting = False
            fight = False
        else:
            print("Player's life: " + str(PM_HP))
            print("")
    else: #Defense unsuccessful
        print("")
        print("The creature walks in the shadowns and hit your back... you don't know how it can be so fast....")
        damage_me = random.randint(stats_player_monster.monster_e[0], stats_player_monster.monster_e[1])
        PM_HP -= damage_me
        print("")
        print(f"You recived {damage_me}")
        print(f"Your life {PM_HP}")
        print("")
        if PM_HP <= 0: #Player's HP = 0, game over.
            print("")
            print(f"{PM_HP}, you died... game over!")
            print("")
            is_fighting = False
            fight = False
        else:
            print("Player's life: " + str(PM_HP))
            print("")

def def_mag_vs_mh(): #Defense Instance (Mage versus Monster Hard)
    global ME_HP, MH_HP, PW_HP, PM_HP, is_fighting, fight, flee_attempt

    defense = random.randint(1,3)
    if defense == 1: #Defense Successful
        print("")
        print("You raise your shield and block incoming atack!")
        print("")
    elif defense == 2: #Hit in armor
        print("")
        print("You didn't have enough reflexes and get hit in your armor...")
        print("")
        #Calculate hit damage
        damage_mh = random.randint(stats_player_monster.monster_h[0], stats_player_monster.monster_h[1])
        block_damage = damage_mh / stats_player_monster.PM_defense
        PM_HP -= block_damage
        PM_HP = round(PM_HP, 0)
        print("")
        print(f"You recived {block_damage}")
        print(f"Your life {PM_HP}")
        print("")

        if PM_HP <= 0:
            print("")
            print(f"{PM_HP}, you died... game over!")
            print("")
            is_fighting = False
            fight = False
        else:
            print("Player's life: " + str(PM_HP))
            print("")
    else: #Defense unsuccessful
        print("")
        print("The creature walks in the shadowns and hit your back... you don't know how it can be so fast....")
        damage_mh = random.randint(stats_player_monster.monster_h[0], stats_player_monster.monster_h[1])
        PM_HP -= damage_mh
        print("")
        print(f"You recived {damage_mh}")
        print(f"Your life {PM_HP}")
        print("")
        if PM_HP <= 0: #Player's HP = 0, game over.
            print("")
            print(f"{PM_HP}, you died... game over!")
            print("")
            is_fighting = False
            fight = False
        else:
            print("Player's life: " + str(PM_HP))
            print("")

def flee_war_vs_me(): #Flee Instance (Warrior versus Monster Easy)
    global ME_HP, MH_HP, PW_HP, PM_HP, is_fighting, fight, flee_attempt
    flee = random.randint(1,3)
    if flee == 1:
        print("")
        print("You blend into the shadows, in silent movements and flee from the presence of this creature...")
        print("")
        is_fighting = False
        fight = False
        flee_attempt = 0
    else:
        flee_attempt += 1  
        print("")
        print("The creature smells your fear, your blood, your pain... you can't flee form that... you'll need to fight!")
        print("")
        if flee_attempt > 3:
            print("")
            print("The creature run faster than you and hit your back... you feel the only way is go back to fight...")
            print("")
            damage_me = random.randint(stats_player_monster.monster_e[0], stats_player_monster.monster_e[1])
            PW_HP -= damage_me
            print("")
            print(f"You recived {damage_me}")
            print(f"Your life {PW_HP}")
            print("")
            if PW_HP <= 0:
                print("")
                print(f"{PW_HP}, you died... game over!")
                print("")
                is_fighting = False
                fight = False

def flee_war_vs_mh(): #Flee Instance (Warrior versus Monster Hard)
    global ME_HP, MH_HP, PW_HP, PM_HP, is_fighting, fight, flee_attempt
    flee = random.randint(1,3)
    if flee == 1:
        print("")
        print("You blend into the shadows, in silent movements and flee from the presence of this creature...")
        print("")
        is_fighting = False
        fight = False
        flee_attempt = 0
    else:
        flee_attempt += 1  
        print("")
        print("The creature smells your fear, your blood, your pain... you can't flee form that... you'll need to fight!")
        print("")
        if flee_attempt > 3:
            print("")
            print("The creature run faster than you and hit your back... you feel the only way is go back to fight...")
            print("")
            damage_mh = random.randint(stats_player_monster.monster_h[0], stats_player_monster.monster_h[1])
            PW_HP -= damage_mh
            print("")
            print(f"You recived {damage_mh}")
            print(f"Your life {PW_HP}")
            print("")
            if PW_HP <= 0:
                print("")
                print(f"{PW_HP}, you died... game over!")
                print("")
                is_fighting = False
                fight = False

def flee_mag_vs_me(): #Flee Instance (Mage versus Monster Easy)
    global ME_HP, MH_HP, PW_HP, PM_HP, is_fighting, fight, flee_attempt
    flee = random.randint(1,3)
    if flee == 1:
        print("")
        print("You blend into the shadows, in silent movements and flee from the presence of this creature...")
        print("")
        is_fighting = False
        fight = False
        flee_attempt = 0
    else:
        flee_attempt += 1  
        print("")
        print("The creature smells your fear, your blood, your pain... you can't flee form that... you'll need to fight!")
        print("")
        if flee_attempt > 3:
            print("")
            print("The creature run faster than you and hit your back... you feel the only way is go back to fight...")
            print("")
            damage_me = random.randint(stats_player_monster.monster_e[0], stats_player_monster.monster_e[1])
            PM_HP -= damage_me
            print("")
            print(f"You recived {damage_me}")
            print(f"Your life {PM_HP}")
            print("")
            if PM_HP <= 0:
                print("")
                print(f"{PM_HP}, you died... game over!")
                print("")
                is_fighting = False
                fight = False

def flee_mag_vs_mh(): #Flee Instance (Mage versus Monster Hard)
    global ME_HP, MH_HP, PW_HP, PM_HP, is_fighting, fight, flee_attempt
    flee = random.randint(1,3)
    if flee == 1:
        print("")
        print("You blend into the shadows, in silent movements and flee from the presence of this creature...")
        print("")
        is_fighting = False
        fight = False
        flee_attempt = 0
    else:
        flee_attempt += 1  
        print("")
        print("The creature smells your fear, your blood, your pain... you can't flee form that... you'll need to fight!")
        print("")
        if flee_attempt > 3:
            print("")
            print("The creature run faster than you and hit your back... you feel the only way is go back to fight...")
            print("")
            damage_mh = random.randint(stats_player_monster.monster_h[0], stats_player_monster.monster_h[1])
            PM_HP -= damage_mh
            print("")
            print(f"You recived {damage_mh}")
            print(f"Your life {PM_HP}")
            print("")
            if PM_HP <= 0:
                print("")
                print(f"{PM_HP}, you died... game over!")
                print("")
                is_fighting = False
                fight = False

def fight_loop(difficult, player): #Fighting
    global fight, is_fighting, flee_attempt, ME_HP, MH_HP, PW_HP, PM_HP
    is_fighting = True
    reset_MHP()

    while is_fighting:
        print("")
        print(" _____________________________ ")
        print("|                             |")
        print("|   What do you do?           |")
        print("|   1 - Attack!               |")
        print("|   2 - Defense!              |")
        print("|   3 - Flee from Battle...   |")
        print("|_____________________________|")
        print("")
        fight_instace = (int(input("")))

        if fight_instace == 1: #Attack instance
            if difficult == 1 and player == 1:
                atk_war_vs_me()
            elif difficult == 2 and player == 1:
                atk_war_vs_mh()
            elif difficult == 1 and player == 2:
                atk_mag_vs_me()
            elif difficult == 2 and player == 2:
                atk_mag_vs_mh()
        elif fight_instace == 2: #Defense instance
            if difficult == 1 and player == 1:
                def_war_vs_me()
            elif difficult == 2 and player == 1:
                def_war_vs_mh()
            elif difficult == 1 and player == 2:
                def_mag_vs_me()
            elif difficult == 2 and player == 2:
                def_mag_vs_mh()
        elif fight_instace == 3: #Flee instance
            if difficult == 1 and player == 1:
                flee_war_vs_me()
            elif difficult == 2 and player == 1:
                flee_war_vs_mh()
            elif difficult == 1 and player == 2:
                flee_mag_vs_me()
            elif difficult == 2 and player == 2:
                flee_mag_vs_mh()
        else:
            print("Choose a valid option.")
