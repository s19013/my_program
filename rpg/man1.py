from hero_base import Human
import random
import math
import sys
from time import sleep

class Fighter(Human):
    """docstring for ."""
    def __init__(self,name,tag,job,hp,mp,attack_base,set_skill = 0):
        super(Fighter, self).__init__(name,tag,job,hp,mp,attack_base)


    def skill(self):
        print("[0:戻る","1:集中","2:毒","3:強切り]\n")
        want_skill=int(input())
        if want_skill == 0:
            self.skill_setter("back")
        elif want_skill == 1:
            self.skill_setter("buf")
            self.receive_critical_turn(5)
            self.use_mp(10)
            print("集中")
        elif want_skill == 2:
            pass
        elif want_skill == 3:
            self.skill_setter("single_attack",150)
            self.use_mp(15)


    def skill_setter(self,want_do_skill,damage=0):
        self.set_skill = want_do_skill
        self.skill_damage = damage
