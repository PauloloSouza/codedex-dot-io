#Stats Players and Monsters
import math
import random

#Player Warrior
player_warrior = [1, 100, 10, 5, 10, 0]
PW_level = player_warrior[0]
PW_HP = player_warrior[1]
PW_attack = player_warrior[2]
PW_magic = player_warrior[3]
PW_defense = player_warrior[4]
PW_experience = player_warrior[5]

#Player Mage
player_mage = [1, 80, 5, 15, 5, 0]
PM_level = player_mage[0]
PM_HP = player_mage[1]
PM_attack = player_mage[2]
PM_magic = player_mage[3]
PM_defense = player_mage[4]
PM_experience = player_mage[5]

#Monster Easy
monster_easy = [1, 30, 10, 5, 5, 50]
ME_level = monster_easy[0]
ME_HP = monster_easy[1]
ME_attack = monster_easy[2]
ME_magic = monster_easy[3]
ME_defense = monster_easy[4]
ME_experience = monster_easy[5]

#Monster Hard
monster_hard = [3, 80, 20, 10, 10, 200]
MH_level = monster_hard[0]
MH_HP = monster_hard[1]
MH_attack = monster_hard[2]
MH_magic = monster_hard[3]
MH_defense = monster_hard[4]
MH_experience = monster_hard[5]

#Multiplier
warrior_level = 2.5
warrior_attack = 1.5
warrior_magic = 0.1
warrior_defense = 1.4

mage_level = 2.5
mage_attack = 0.1
mage_magic = 2.0
mage_defense = 0.5

max_warrior_dmg = 1.5
max_mage_dmg = 2.0

monster_level = 1.5
monster_attack = 1.1
monster_magic = 1.1
monster_defense = 1.1

max_monster_easy_dmg = 1.5
max_monster_hard_dmg = 2.5

#Initializing objects and assign values
class PW_CombatStats:
    def __init__(self, PW_level, PW_attack, PW_magic):
        self.PW_level = PW_level
        self.PW_attack = PW_attack
        self.PW_magic = PW_magic

class PM_CombatStats:
    def __init__(self, PM_level, PM_attack, PM_magic):
        self.PM_level = PM_level
        self.PM_attack = PM_attack
        self.PM_magic = PM_magic

class ME_CombatStats:
    def __init__(self, ME_level, ME_attack, ME_magic):
        self.ME_level = ME_level
        self.ME_attack = ME_attack
        self.ME_magic =  ME_magic

class MH_CombatStats:
    def __init__(self, MH_level, MH_attack, MH_magic):
        self.MH_level = MH_level
        self.MH_attack = MH_attack
        self.MH_magic =  MH_magic

#Damage Base + Multiplier for Warriors, Mages and Monsters
def warrior_dmg(stats):
    base = (
        math.sqrt(stats.PW_level) * warrior_level +
        math.sqrt(stats.PW_attack) * warrior_attack +
        math.sqrt(stats.PW_magic) * warrior_magic
        )
    return int(base), int(base * max_warrior_dmg)

def mage_dmg(stats):
    base = (
        math.sqrt(stats.PM_level) * mage_level +
        math.sqrt(stats.PM_attack) * mage_attack +
        math.sqrt(stats.PM_magic) * mage_magic
        )
    return int(base/2), int(base * max_mage_dmg)

def me_dmg(stats):
    base = (
        math.sqrt(stats.ME_level) * monster_level +
        math.sqrt(stats.ME_attack) * monster_attack +
        math.sqrt(stats.ME_magic) * monster_magic
        )
    return int(base), int(base * max_monster_easy_dmg)

def mh_dmg(stats):
    base = (
        math.sqrt(stats.MH_level) * monster_level +
        math.sqrt(stats.MH_attack) * monster_attack +
        math.sqrt(stats.MH_magic) * monster_magic
    )
    return int(base), int(base * max_monster_hard_dmg)

#Calling classes and define values
stats_warrior = PW_CombatStats(PW_level, PW_attack, PW_magic)
stats_mage = PM_CombatStats(PM_level, PM_attack, PM_magic)
stats_me = ME_CombatStats(ME_level, ME_attack, ME_magic)
stats_mh = MH_CombatStats(MH_level, MH_attack, MH_magic)

warrior = warrior_dmg(stats_warrior)
mage = mage_dmg(stats_mage)
monster_e = me_dmg(stats_me)
monster_h = mh_dmg(stats_mh)

#Calculate random damage from base to maximum damage possible.
damage_warrior = random.randint(warrior[0], warrior[1])
damage_mage = random.randint(mage[0], mage[1])
damage_me = random.randint(monster_e[0], monster_e[1])
damage_mh = random.randint(monster_h[0], monster_h[1])