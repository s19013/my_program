from hero_base import Human
import random
import math
import sys
from time import sleep

class Slime(Human):
    def __init__(self,name,tag,job,hp,mp,attack_base,want_do = 0):
        super(Slime, self).__init__(name,tag,job,hp,mp,attack_base)
        self.want_do_setter = want_do

    def next_do(self):
        do = random.randint(1,100)
        if do > 20:
            self.want_do_setter = 1
            self.attack(self.attack_base)
        elif do > 0:
            self.want_do_setter = 2
            self.guard()
        # print("comming soon")
        # ran = random.randint(1.10)
        # if ran>8:
