import random
import math
import hero
import sys
class Enemy:
    """敵のクラス"""
    def __init__(self,name,hp,n_attack):
        self.name=name
        self.max_hp=hp
        self.hp=hp
        self.n_attack=n_attack
        self.power=1
        self.power_turn=0
        self.cri_up_turn=0
        self.poison=0
        self.mahi=0
        self.blood=0
#情報を見せる
    def show(self):
        print("\n名前:{} |hp:{}/{}".format(self.name,self.hp,self.max_hp))
#死んだ時の関数
    def die(self):
        return True

##hpの変動
#減る
    def remaing_hp(self,damage):
        self.hp-=damage
        print("\n{}は{}のダメージをうけた\n".format(self.name,damage))
        if self.hp<=0:
            print("敵を倒した")
            sys.exit()

#増える
    def charge_hp(self,care_hp):
        if self.hp<self.max_hp:
            self.hp+=care_hp
            print("\n{}は\nhpを{}回復した\n".format(self.name,care_hp))
            if self.hp>self.max_hp:
                self.hp=self.max_hp
        else:
            print("これ以上回復できない")

#攻撃
    def base_attack(self,trick):
        #強化か弱体か
        self.power_status(self.power_turn)
        #クリティカル関係
        # self.critical(self.cri_up_turn)
        if self.cri_up_turn>0:
            self.cri=random.randint(1,10)
            if self.cri>3:
                print("クリティカル！")# DEBUG:
                self.cri_rate=1.4
            else:
                self.cri_rate=1
            self.cri_up_turn-=1
            print("[ene_cri_up_turn:{}]".format(self.cri_up_turn))# DEBUG:
        else:
            self.cri=random.randint(1,10)
            if self.cri>8:
                print("クリティカル")# DEBUG:
                self.cri_rate=1.4
            else:
                self.cri_rate=1
        attack_value=math.floor(trick*self.cri_rate*self.power)
        hero.man2.remaing_hp(attack_value)
         # DEBUG:print("[attack {}]\n".format(math.floor(trick*self.cri_rate*self.power))) # DEBUG:

    def power_status(self,power_turn):
        self.power_turn=power_turn
        if self.power_turn>0:
            self.power=1.5
            self.power_turn-=1
            print("[ene_power_status:{}]".format(self.power)) # DEBUG:
            print("[ene_power_turn:{}]\n".format(self.power_turn)) # DEBUG:
        elif self.power_turn<0:
            self.power=0.5
            self.power_turn+=1
            print("[ene_power_status:{}]".format(self.power)) # DEBUG:
            print("[ene_power_turn:{}]\n".format(self.power_turn)) # DEBUG:
        else:
            self.power=1
            print("\n[ene_power_status:{}]".format(self.power)) # DEBUG:

    def do_power_up(self):
        self.power_status(5)
        print("ene 強化した\n")

    def week(self):
        hero.man2.power# DEBUG:status(-5)
        print("ene 弱体化した")

    def poison_attack(self):
        hero.man2.receive_poison(3)
        print("ene 毒攻撃")

    def enemy_do(self):
    #普通の攻撃　強化　弱体化　毒　回復　強攻撃
        if self.hp>(self.max_hp/2):
            do=random.randint(1,100)
            if do<=40:
                self.base_attack(self.n_attack)
                print("ene 攻撃")# DEBUG:
                print(do)# DEBUG:
            elif 40<do<=60:
                strong=self.n_attack*2
                self.base_attack(strong)
                print("ene 強攻撃")# DEBUG:
                print(do)# DEBUG:
            elif 60<do<=70:
                self.do_power_up()
                print(do)# DEBUG:
            elif 70<do<=80:
                self.week()
                print(do)# DEBUG:
            elif 80<do<=90:
                if self.hp<100:
                    self.charge_hp(50)
                    print(do)# DEBUG:
                else:
                    self.enemy_do()
            else:
                self.poison_attack()
                print(do)# DEBUG:
        else:
            do=random.randint(1,100)
            if do<=30:
                self.base_attack(self.n_attack)
                print("ene 攻撃")# DEBUG:
                print(do)# DEBUG:
            elif 30<do<=60:
                strong=self.n_attack*2
                self.base_attack(strong)
                print("ene 強攻撃")# DEBUG:
                print(do)# DEBUG:
            elif 60<do<=70:
                self.do_power_up()
                print(do)# DEBUG:
            elif 70<do<=80:
                self.week()
                print(do)# DEBUG:
            elif 80<do<=90:
                if self.hp<100:
                    self.charge_hp(50)
                    print(do)# DEBUG:
                else:
                    self.base_attack(self.n_attack)
                    print("ene 攻撃")# DEBUG:
                    print(do)# DEBUG:
            else:
                self.poison_attack()
                print(do)# DEBUG:

ene=Enemy("ene1",300,30)
