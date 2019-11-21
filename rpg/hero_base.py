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

        self.pow_level = 0
        self.power_up_turn = 0
        self.power_rate = 1
        self.defe_level = 0
        self.defe_turn = 0
        self.cri_level = 1
        self.cri_turn = 0

        self.poison_level = 0
        self.poison_turn = 0
        self.mahi_level = 0
        self.mahi_turn = 0
        self.bleeding_level = 0
        self.bleeding_turn = 0
        self.recovery_attack_base_from_bleeding = 0

        self.live = True
        self.already_die = True
        self.lest_turn = 0

        self.attack_d = 0 # DEBUG:

    def show(self):
        box=[]
        #毒
        if self.poison_level==1:
            box.append("毒Lv1")
        elif self.poison_level==2:
            box.append("毒Lv2")
        elif self.poison_level==3:
            box.append("毒Lv3")
        #出血
        if self.bleeding_level==1:
            box.append("出血Lv1")
        elif self.bleeding_level==2:
            box.append("出血Lv2")
        elif self.bleeding_level==3:
            box.append("出血Lv3")

        print("\n" + self.name)
        print("職業:{job} | hp:{hp}/{m_hp} | mp:{mp}/{m_mp}".format(job=self.job,hp=self.hp,m_hp=self.max_hp,mp=self.mp,m_mp=self.max_mp))
        print("防御Lv:{} | 攻撃力レベル:Lv{} | クリティカルレベル:Lv{}".format(self.defe_level,self.pow_level,self.cri_level))
        if box == []:
            print("状態異常:なし")
        else:
            print("状態異常:{}".format(box))


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
    def receive_mahi_turn(self,mahi_turn):
        self.mahi_turn += mahi_turn

    def receive_damage(self,damage,type):
        if self.live == True:
            if type == "n":
                self.hp-=damage
                sleep(0.5)
                print("\n{}は{}のダメージを受けた".format(self.name,damage))
            elif type == "p":
                self.hp-=damage
                sleep(0.5)
                print("\n{}は毒で{}のダメージを受けた".format(self.name,damage))
            elif type == "b":
                self.hp -= damage
                sleep(0.5)
                print("\n{}は出血で{}のダメージを受けた".format(self.name,damage))
        if self.hp <= 0 and self.already_die == 0:
            print("{}は死んでしまった".format(self.name))
            self.already_die = False
            self.live = False
        # 後で死亡に関するいろいろをかく
##状態系
    #毒
    def receive_poison_turn(self,poison_turn):
        self.poison_turn += poison_turn
        if self.poison_turn >14:
            self.poison_level = 3
        elif self.poison_turn >9:
            self.poison_level = 2
        elif self.poison_turn > 4:
            self.poison_level = 1
        else:
            self.poison_level = 0

    def poison(self):
        if self.poison_level>0:
            if self.poison_level == 3:
                self.receive_damage(round(self.hp*0.3)+5,"p")
            elif self.poison_level == 2:
                self.receive_damage(round(self.hp*0.2)+5,"p")
            elif self.poison_level == 1:
                self.receive_damage(round(self.hp*0.1)+5,"p")
            self.poison_turn -= 1
        if self.poison_turn<=0:
            self.poison_turn = 0

    #出血
    def receive_bleeding_turn(self,bleeding_turn):
        self.bleeding_turn += bleeding_turn
        if self.bleeding_turn >14:
            self.bleeding_level = 3
        elif self.bleeding_turn >9:
            self.bleeding_level = 2
        elif self.bleeding_turn > 4:
            self.bleeding_level = 1
        else:
            self.bleeding_level = 0

    def bleeding(self):
            if self.bleeding_turn > 0:
                if self.bleeding_level == 3:
                    self.receive_damage(round(self.hp*0.4)+10,"b")
                    abd = round(self.attack_base * 0.15)
                    self.attack_base -= abd
                    self.recovery_attack_base_from_bleeding += abd

                elif self.bleeding_level == 2:
                    self.receive_damage(round(self.hp*0.3)+10,"b")
                    abd = round(self.attack_base * 0.1)
                    self.attack_base -= abd
                    self.recovery_attack_base_from_bleeding += abd

                elif self.bleeding_level == 1:
                    self.receive_damage(round(self.hp*0.2)+10,"b")
                    abd = round(self.attack_base * 0.05)
                    self.attack_base -= abd
                    self.recovery_attack_base_from_bleeding += abd

                self.bleeding_turn -= 1
            if self.bleeding_turn<=0:
                self.bleeding_turn = 0
                self.attack_base += self.recovery_attack_base_from_bleeding
#確認
    def check(self):
        # 出血
        self.poison()
        self.bleeding()
        # クリティカル
        if self.cri_turn > 0:
            self.cri_turn-=1
        else:
            pass
#攻撃
    def attack(self,damage):
        ##仮書き　後ほど編集
        a = damage * self.critical() * self.power_rate
        print("{}の攻撃".format(self.name))
        sleep(0.5)
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
            return 1
        else:
            return 1
