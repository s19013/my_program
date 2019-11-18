import random
import math
import sys
from time import sleep

class Enemy:
    """主要キャラのベース"""
    def __init__(self,name,hp,mp,attack_base):
        self.name = name
        self.max_hp = self.hp = hp
        self.max_mp = self.mp = mp
        self.max_attack_base = self.attack_base = attack_base
        self.power_rate = 1
        self.power_turn = 0
        self.cri_rate = 1
        self.cri_turn = 0
        self.poison_turn = 0
        self.mahi_turn = 0
        self.bleeding_turn = 0
        self.live = True
        self.die = 1

    def show(self):
        print("\n名前:{} | hp:{}/{} | mp:{}/{} |".format(self.name,self.hp,self.max_hp,self.mp,self.max_mp))

    def use_mp(self,used):
        self.mp -= used

# 回復
    def recovery_hp(self,care_hp):
        if self.hp < self.max_hp and self.live==True:
            self.hp += care_hp
            sleep(0.5)
            print("\n{}は{}hp回復した".format(self.name,care_hp))
            if self.hp > self.max_hp:
                self.hp = self.max_hp
        else:
            pass

    def recovery_mp(self,care_mp):
        if self.mp < self.max_mp and self.live==True:
            self.mp += care_mp
            sleep(0.5)
            print("\n{}は{}mp回復した".format(self.name,care_mp))
            if self.mp > self.max_mp:
                self.mp = self.max_mp
        else:
            pass

# ダメージ系
    def receive_poison(self,poison_turn):
        self.poison_turn = poison_turn

    def receive_mahi(self,mahi_turn):
        self.mahi_turn = mahi_turn

    def receive_bleeding(self,bleeding_turn):
        self.bleeding_turn = bleeding_turn

    def receive_damage(self,damage):
        if self.live == True:
            self.hp-=damage
            sleep(0.5)
            print("\n{}は{}のダメージを受けた".format(self.name,damage))
            if self.hp < 0 and self.die is 0:
                print("{}を倒した".format(self.name))
                self.die += 1
        else:
            pass
        # 後で死亡に関するいろいろをかく
##状態以上系
    def check(self):
        if self.poison_turn > 0:
            self.hp -= 30
            sleep(0.5)
            print("\n{}は毒で{}のダメージ".format(self.name,30))
            self.poison_turn -= 1
        else:
            pass
        if self.bleeding_turn > 0:
            self.hp -= 40
            sleep(0.5)
            print("\n{}は出血で{}のダメージ".format(self.name,40))
            self.bleeding_turn -= 1
            if self.attack_base == self.max_attack_base:
                self.attack_base -= 40
            else:
                pass
        else:
            self.attack_base = self.max_attack_base
