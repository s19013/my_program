import random
import math
import sys
from time import sleep

class Human:
    """主要キャラのベース"""
    def __init__(self,name,job,hp,mp,attack_base):
        self.name = name
        self.job = job
        self.max_hp = self.hp = hp
        self.max_mp = self.mp = mp
        self.max_attack_base = self.attack_base = attack_base
        self.power_level = 1
        self.power_turn = 0
        self.defe_level = 0
        self.defe_turn = 0
        self.cri_level = 0
        self.cri_turn = 0
        self.poison_turn = 0
        self.mahi_turn = 0
        self.bleeding_turn = 0
        self.live = True
        self.die = 1
        self.attack_d = 0 # DEBUG:

    def show(self):
        print("\n名前:{} | 職業:{} | hp:{}/{} | mp:{}/{} |".format(self.name,self.job,self.hp,self.max_hp,self.mp,self.max_mp))

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
        elif self.live != True:
            print("死んでいるからいみがない")
        else:
            print("これ以上回復できない")

    def recovery_mp(self,care_mp):
        if self.mp < self.max_mp and self.live==True:
            self.mp += care_mp
            sleep(0.5)
            print("\n{}は{}mp回復した".format(self.name,care_mp))
            if self.mp > self.max_mp:
                self.mp = self.max_mp
        elif self.live != True:
            print("\n死んでいるからいみがない")
        else:
            print("\nこれ以上回復できない")

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
                print("{}は死んでしまった".format(self.name))
                self.die += 1
        else:
            pass
        # 後で死亡に関するいろいろをかく
    def defence_turn
##状態系
    def check(self):
        # 毒
        if self.poison_turn > 0:
            self.hp -= 30
            sleep(0.5)
            print("\n{}は毒で{}のダメージ".format(self.name,30))
            self.poison_turn -= 1
        else:
            pass
        # 出血
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
        # クリティカル
        if self.cri_turn > 0:
            self.cri_turn-=1
        else:
            pass
#攻撃
    def base_attack(self):
        ##仮書き　後ほど編集
        a = self.attack_base * self.critical() * self.power_rate
        self.attack_d = round(a)

    def critical_turn(self,turn):
        self.cri_turn += turn
        if self.cri_turn > 20:
            self.cri_level = 4
        elif self.cri_turn > 15:
            self.cri_level = 3
        elif self.cri_turn > 10:
            self.cri_level = 2
        elif self.cri_turn >5:
            self.cri_level = 1
        else:
            self.cri_level = 0

    def critical(self):
        cri = random.randint(1,100)
        if self.cri_level == 4:
                print("クリティカル")
                return 1.8
        elif self.cri_level >3:
            if cri > 20:
                print("クリティカル")
                return 1.5
        elif self.cri_level >2:
            if cri >40:
                print("クリティカル")
                return 1.5
        elif self.cri_level >1:
            if cri > 60:
                print("クリティカル")
                return 1.5
        elif self.cri_level >0:
            if cri > 80:
                print("クリティカル")
                return 1.5
        else:
            return 1
