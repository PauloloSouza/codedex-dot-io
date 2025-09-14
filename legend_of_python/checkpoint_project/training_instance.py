#Training Instance
import stats_player_monster

running = True
menu = True
first_enter = True
first_food = True
first_training = True
first_login = True
is_fighting = True
is_training = True

atk_power = 0
mag_power = 0
def_power = 0
flee_attempt = 0
drunk = 0
local = 0
home_local_training = 1


PW_HP = stats_player_monster.PW_HP
PM_HP = stats_player_monster.PM_HP
ME_HP = stats_player_monster.ME_HP
MH_HP = stats_player_monster.MH_HP

def dummy_war_atk(): #Training attack power of Warrior
    global first_training, first_food, home_local_training, drunk, is_training, atk_power, mag_power, def_power, upgrade_atk
    atk_power += 1
    print("")
    print("You get your sword and perform hits with precision on your training dummy.")
    print("")
    if atk_power <= 3: #Increase the attack power
        upgrade_atk = stats_player_monster.PW_attack * 0.7
    elif atk_power >3 and atk_power <= 10:
        upgrade_atk = stats_player_monster.PW_attack * 0.5
    else:
        upgrade_atk = stats_player_monster.PW_attack * 0.3

    stats_player_monster.player_warrior[2] += upgrade_atk
    stats_player_monster.PW_attack += upgrade_atk

    stats_player_monster.stats_warrior = stats_player_monster.PW_CombatStats(
        stats_player_monster.PW_level,
        stats_player_monster.PW_attack,
        stats_player_monster.PW_magic
    )

    stats_player_monster.warrior = stats_player_monster.warrior_dmg(stats_player_monster.stats_warrior)
    #print(stats_player_monster.warrior[1])
    
    is_training = False #This makes stop training loop.
    first_training = False #This makes not training more than once.
    first_food = True #This makes you hungry again
    drunk = 0 #This makes you're not drunk anymore
    home_local_training = 0 #This makes leave home_local3 for pratice.

def dummy_war_mag(): #Training magic power of Warrior
    global first_training, first_food, home_local_training, drunk, is_training, atk_power, mag_power, def_power, upgrade_mag
    mag_power += 1
    print("")
    print("You read some spellbooks and meditade, getting focus and concentration.")
    print("")
    if mag_power <= 3: #Increase the magic power
        upgrade_mag = stats_player_monster.PW_magic * 0.3
    elif mag_power >3 and mag_power <= 10:
        upgrade_mag = stats_player_monster.PW_magic * 0.05
    else:
        upgrade_mag = stats_player_monster.PW_magic * 0.01

    stats_player_monster.player_warrior[3] += upgrade_mag
    stats_player_monster.PW_magic += upgrade_mag

    stats_player_monster.stats_warrior = stats_player_monster.PW_CombatStats(
        stats_player_monster.PW_level,
        stats_player_monster.PW_attack,
        stats_player_monster.PW_magic
    )

    stats_player_monster.warrior = stats_player_monster.warrior_dmg(stats_player_monster.stats_warrior)
    #print(stats_player_monster.warrior[1])

    is_training = False
    first_training = False
    first_food == True
    drunk = 0
    home_local_training = 0

def dummy_war_def(): #Training defense power of Warrior
    global first_training, first_food, home_local_training, drunk, is_training, atk_power, mag_power, def_power, upgrade_def
    def_power += 1
    print("")
    print("You go to soldier's training center and pratice with another members, getting hits to your armor and shield, hardening your skin.")
    print("")
    if def_power <= 3: #Increase the defense power
        upgrade_def = stats_player_monster.PW_defense * 0.5
    elif def_power >3 and def_power <= 10:
        upgrade_def = stats_player_monster.PW_defense * 0.4
    else:
        upgrade_def = stats_player_monster.PW_defense * 0.3
    
    stats_player_monster.player_warrior[4] += upgrade_def
    stats_player_monster.PW_defense += upgrade_def

    #print(stats_player_monster.player_warrior[4])

    is_training = False
    first_training = False
    first_food == True
    drunk = 0
    home_local_training = 0

def dummy_mage_atk(): #Training attack power of Mage
    global first_training, first_food, home_local_training, drunk, is_training, atk_power, mag_power, def_power, upgrade_atk
    atk_power += 1
    print("")
    print("You get your rapier and perform hits with precision on your training dummy.")
    print("")
    if atk_power <= 3:
        upgrade_atk = stats_player_monster.PM_attack * 0.3
    elif atk_power >3 and atk_power <= 10:
        upgrade_atk = stats_player_monster.PM_attack * 0.05
    else:
        upgrade_atk = stats_player_monster.PM_attack * 0.01
    
    stats_player_monster.player_mage[2] += upgrade_atk
    stats_player_monster.PM_attack += upgrade_atk

    stats_player_monster.stats_mage = stats_player_monster.PM_CombatStats(
        stats_player_monster.PM_level,
        stats_player_monster.PM_attack,
        stats_player_monster.PM_magic
    )

    stats_player_monster.mage = stats_player_monster.mage_dmg(stats_player_monster.stats_mage)
    #print(stats_player_monster.mage[1])

    is_training = False
    first_training = False
    first_food == True
    drunk = 0
    home_local_training = 0

def dummy_mage_mag(): #Training magic power of Mage
    global first_training, first_food, home_local_training, drunk, is_training, atk_power, mag_power, def_power, upgrade_mag
    mag_power += 1
    print("")
    print("You read some spellbooks and meditade, getting focus and concentration to unlesh more spells.")
    print("")
    if mag_power <= 3:
        upgrade_mag = stats_player_monster.PM_magic * 1.0
    elif mag_power >3 and mag_power <= 10:
        upgrade_mag = stats_player_monster.PM_magic * 0.5
    else:
        upgrade_mag = stats_player_monster.PM_magic * 0.1
    
    stats_player_monster.player_mage[3] += upgrade_mag
    stats_player_monster.PM_attack += upgrade_mag

    stats_player_monster.stats_mage = stats_player_monster.PM_CombatStats(
        stats_player_monster.PM_level,
        stats_player_monster.PM_attack,
        stats_player_monster.PM_magic
    )

    stats_player_monster.mage = stats_player_monster.mage_dmg(stats_player_monster.stats_mage)
    #print(stats_player_monster.mage[1])

    is_training = False
    first_training = False
    first_food == True
    drunk = 0
    home_local_training = 0

def dummy_mage_def(): #Training defense power of Mage
    global first_training, first_food, home_local_training, drunk, is_training, atk_power, mag_power, def_power, upgrade_def
    def_power += 1
    print("")
    print("You go to fight gym and practice with another members.")
    print("")
    if def_power <= 3:
        upgrade_def = stats_player_monster.PM_defense * 0.3
    elif def_power >3 and def_power <= 10:
        upgrade_def = stats_player_monster.PM_defense * 0.2
    else:
        upgrade_def = stats_player_monster.PM_defense * 0.1
    
    stats_player_monster.player_mage[4] += upgrade_def
    stats_player_monster.PM_defense += upgrade_def

    #print(stats_player_monster.player_mage[4])
    
    is_training = False
    first_training = False
    first_food == True
    drunk = 0
    home_local_training = 0

def training_loop(home_local3, player):
    global is_training, first_training, home_local_training, drunk, is_training, atk_power, mag_power, def_power, upgrade_atk
    if home_local3 == 1 and player == 1:
        dummy_war_atk()
    elif home_local3 == 2 and player == 1:
        dummy_war_atk()
    elif home_local3 == 3 and player == 1:
        dummy_war_atk()
    elif home_local3 == 1 and player == 2:
        dummy_mage_atk()
    elif home_local3 == 2 and player == 2:
        dummy_mage_mag()
    elif home_local3 == 3 and player == 2:

        dummy_mage_def()

