import random
import math
import sys
from time import sleep

class Human:
    """主要キャラのベース"""
    def __init__(self,name,tag,job,hp,mp,attack_base):

        self.name = name
        self.job = job
        self.tag = tag
        self.max_hp = self.hp = hp
        self.max_mp = self.mp = mp
#攻撃に関する変数------------------------------
        self.max_attack_base = self.attack_base = attack_base
        self.pow_level = 0
        self.power_up_turn = 0
        self.power_rate = 1
#防御に関する変数---------------------------
        self.defe = False
        self.defe_level = 0
        self.defe_turn = 0
        self.defe_rate = 1
#クリティカルに関する変数----------------------------
        self.cri_level = 0
        self.cri_turn = 0
        self.cri_rate = 1
#状態異常に関する変数-----------------------------
        self.poison_level = 0
        self.poison_turn = 0
        self.mahi_level = 0
        self.mahi_turn = 0
        self.bleeding_level = 0
        self.bleeding_turn = 0
        self.recovery_attack_base_from_bleeding = 0
        self.sleep = False
#生死に関する変数-------------------------------
        self.live = True
        self.already_die = False
#行動に関する変数-------------------------------------
        self.lest_turn = 0
        self.done = False
#geter,seterの代わり--------------------------
        self.set_attack = 0
#デバックよう-----------------------------------
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

#確認
    def check(self):
        # 出血
        self.poison()
        self.bleeding()
        self.defence()
        self.defe = False

    def use_mp(self,used):
        self.mp -= used
        if self.mp > 0:
            return True
        else:
            print("mpが足りない")
            return False


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

    def receive_damage(self,damage,type="n"):
        if self.live == True:
            if type == "n":
                if self.defe == True:
                    damage = round(damage/(1.05 * self.defe_rate))
                    # DEBUG: print(damage)
                    # DEBUG: print(self.defe_level)
                    self.hp-= damage
                    self.defe == False
                else:
                    self.hp-= damage
                sleep(0.1)
                print("\n{}は{}のダメージを受けた".format(self.name,damage))
            elif type == "p":
                self.hp-=damage
                sleep(0.1)
                print("\n{}は毒で{}のダメージを受けた".format(self.name,damage))
            elif type == "b":
                self.hp -= damage
                sleep(0.1)
                print("\n{}は出血で{}のダメージを受けた".format(self.name,damage))
        if self.hp <= 0 and self.already_die == False:
            print("{}は死んでしまった".format(self.name))
            self.already_die = True
            self.live = False
        # 後で死亡に関するいろいろをかく
###バフ　デバフ系
##デバフ
    #毒
    def receive_poison_turn(self,poison_turn):
        self.poison_turn += poison_turn
        if self.poison_turn >14:
            self.poison_level = 4
        elif self.poison_turn >9:
            self.poison_level = 3
        elif self.poison_turn > 4:
            self.poison_level = 2
        elif self.poison_turn >0:
            self.poison_level = 1
        else:
            self.poison_level = 0

    def poison(self):
        if self.poison_level == 4:
            self.receive_damage(round(self.hp*0.4)+5,"p")
        elif self.poison_level == 3:
            self.receive_damage(round(self.hp*0.3)+5,"p")
        elif self.poison_level == 2:
            self.receive_damage(round(self.hp*0.2)+5,"p")
        elif self.poison_level == 1:
            self.receive_damage(round(self.hp*0.1)+5,"p")
        self.receive_poison_turn(-1)

    #出血
    def receive_bleeding_turn(self,bleeding_turn):
        self.bleeding_turn += bleeding_turn
        if self.bleeding_turn >14:
            self.bleeding_level = 4
        elif self.bleeding_turn >9:
            self.bleeding_level = 3
        elif self.bleeding_turn > 4:
            self.bleeding_level = 2
        elif self.bleeding_turn > 0:
            self.bleeding_level = 1
        else:
            self.bleeding_level = 0
            if attack_base != max_attack_base:
                self.attack_base += self.recovery_attack_base_from_bleeding


    def bleeding(self):
        if self.bleeding_level == 4:
            self.receive_damage(round(self.hp*0.4)+10,"b")
            abd = round(self.attack_base * 0.15)
            self.attack_base -= abd
            self.recovery_attack_base_from_bleeding += abd

        elif self.bleeding_level == 3:
            self.receive_damage(round(self.hp*0.3)+10,"b")
            abd = round(self.attack_base * 0.1)
            self.attack_base -= abd
            self.recovery_attack_base_from_bleeding += abd

        elif self.bleeding_level == 2:
            self.receive_damage(round(self.hp*0.2)+10,"b")
            abd = round(self.attack_base * 0.05)
            self.attack_base -= abd
            self.recovery_attack_base_from_bleeding += abd

        elif self.bleeding_level == 1:
            self.receive_damage(round(self.hp*0.1)+10,"b")
            abd = round(self.attack_base * 0.01)
            self.attack_base -= abd
            self.recovery_attack_base_from_bleeding += abd

        if self.attack_base <=0:
            self.attack_base = 1
        self.receive_bleeding_turn(-1)
    ##睡眠
    def sleep_turn(arg):
        pass
##バフ
#防御
    def receive_defence_turn(self,defe_turn):
        self.defe_turn += defe_turn
        if self.defe_turn > 14:
            self.defe_level = 4
        elif self.defe_turn > 9:
            self.defe_level = 3
        elif self.defe_turn > 4:
            self.defe_level = 2
        elif self.defe_turn > 0:
            self.defe_level = 1
        else:
            self.defe_level = 0

    def defence():
        if self.defe_level == 4:
            self.defe_rate = 2
        elif self.defe_level == 3:
            self.defe_rate = 1.8
        elif self.defe_level == 2:
            self.defe_rate = 1.5
        elif self.defe_level == 1:
            self.defe_rate = 1.2
        else:
            self.defe_rate = 1
        self.receive_defence_turn(-1)



    def guard(self):
        print(self.name+"は攻撃に備えた")
        self.defe = True

#攻撃
    def attack(self,damage):
        ##仮書き　後ほど編集
        print("{}の攻撃".format(self.name))
        self.critical()
        a = damage * self.cri_rate * self.power_rate
        sleep(0.1)
        # self.attack_d = round(a)
        self.attack_seter_func(round(a))

    def attack_seter_func(self,damage):
        self.set_attack = damage

    def receive_critical_turn(self,turn):
        self.cri_turn += turn
        if self.cri_turn > 19:
            self.cri_level = 5
        elif self.cri_turn > 14:
            self.cri_level = 4
        elif self.cri_turn > 9:
            self.cri_level = 3
        elif self.cri_turn > 4:
            self.cri_level = 2
        elif self.cri_turn > 0:
            self.cri_level = 1
        else:
            self.cri_level = 0

    def critical(self):
        cri = random.randint(1,100)
        if self.cri_level == 5:
                print("クリティカル")
                self.cri_rate = 1.8
        elif self.cri_level == 4:
            if cri > 20:
                print("クリティカル")
                self.cri_rate = 1.5
        elif self.cri_level == 3:
            if cri >40:
                print("クリティカル")
                self.cri_rate = 1.5
        elif self.cri_level == 2:
            if cri > 60:
                print("クリティカル")
                self.cri_rate = 1.5
        elif self.cri_level == 1:
            if cri > 80:
                print("クリティカル")
                self.cri_rate = 1.5
        elif self.cri_level == 0:
            if cri > 95:
                print("クリティカル")
                self.cri_rate = 1.5
        self.receive_critical_turn(-1)

    # def next_do(self):
    #     print("どうする？")
    #     try:
    #         want_do = int(input("1:攻撃 2:防御 3:必殺技 4:アイテム 5:ステータス"))
    #     except Exception as e:
    #         print("\n入力し直し")
    #         self.next_do()
    #     if 1<=want_do and want_do<=5:
    #         if want_do == 1:
    #             return
    #             # self.attack(self.attack_base)
    #         if want_do == 2:
    #             return self.guard()
    #         if want_do == 3:
    #             return print("comming soon")
    #         if want_do == 4:
    #             return print("comming soon")
    #         if want_do == 5:
    #             return self.show()
    #     else:
    #         print("\n入力し直し")
    #         self.next_do()
