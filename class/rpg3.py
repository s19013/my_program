import random
import math
class human:
    """大体共通するクラス"""
    def __init__(self,name,job,hp,mp,n_attack):
        self.name=name
        self.job=job
        self.hp=hp
        self.mp=mp
        self.n_attack=n_attack
        self.power=1
        self.power_up_turn=0
        self.cri_up_turn=0
        self.poison=0
        self.mahi=0
        self.blood=0

#ステータスを取る
    def getname(self):
        return self.name
    def getjob(self):
        return self.job
    def gethp(self):
        return self.hp
    def getmp(self):
        return self.mp
#情報を見せる
    def show(self):
        print("\n名前:{} ".format(self.getname()))
        print("職業:{} ".format(self.getjob()))
        print("hp:{} ".format(self.gethp()))
        print("mp:{} \n".format(self.getmp()))
##hp mpの変動
#減る
    def remaing_hp(self,damage):
        self.hp-=damage
    def remaing_mp(self,used_mp):
        self.mp-=used_mp
#増える
    def charge_hp(self,care_hp):
        self.hp+=care_hp
    def charge_mp(self,care_mp):
        self.mp+=care_mp
##行動
        #後々調整
#攻撃
    def base_attack(self,trick):
        self.power_up(self.power_up_turn)
        if self.power_up_turn>0:
            self.power=1.5
            self.power_up_turn-=1
            print("power_up:{}".format(self.power)) # DEBUG:
            print("power_up_turn:{}\n".format(self.power_up_turn)) # DEBUG:
        else:
            self.power=1
            print("power_up:{}\n".format(self.power)) # DEBUG:
        #クリティカル関係
        self.critical(self.cri_up_turn)
        if self.cri_up_turn>0:
            self.cri=random.randint(1,10)
            if self.cri>3:
                print("クリティカル！")
                self.cri_rate=1.4
            else:
                self.cri_rate=1
            self.cri_up_turn-=1
            print("cri_up_turn:{}".format(self.cri_up_turn))# DEBUG:
        else:
            self.cri=random.randint(1,10)
            if self.cri>8:
                print("クリティカル")# DEBUG:
                self.cri_rate=1.4
            else:
                self.cri_rate=1
        #return trick*self.cri_rate*self.power_up
        print("attack {}".format(math.floor(trick*self.cri_rate*self.power))) # DEBUG:

    def power_up(self,power_up_turn):
        self.power_up_turn=power_up_turn



    def critical(self,cri_up_turn):
        self.cri_up_turn=cri_up_turn
        # try:
        #     pass
        # except :
        #     cri_up_turn=0
        # if self.cri_up_turn==None or self.cri_up_turn==0:
        #     self.cri_up_turn=0
        # else:
        #     pass
        # if self.cri_up_turn>0:
        #     self.cri=random.randint(1,10)
        #     if self.cri>4:
        #         print("cri!") #DEBUG:
        #         self.cri_rate=1.4
        #     else:
        #         self.cri_rate=1
        #     self.cri_up_turn-=1
        #     # DEBUG: print(self.cri_up_turn)
        # else:
        #     self.cri=random.randint(1,10)
        #     if self.cri>8:
        #         print("cri")# DEBUG:
        #         self.cri_rate=1.4
        #     else:
        #         self.cri_rate=1



    def next_do(self):
        while True:
            try:
                do=int(input("1:攻撃　2:アイテム　3:特技　4:ステータス\n"))
                if do>4 and do<=0:
                    print("入力し直し")
                elif do>0 and do<5:
                    break
                else:
                    print("入力し直し")
            except:
                print("入力し直し")
        if do==1:
            self.base_attack(self.n_attack)
        elif do==2:
            self.item()
        elif do==3:
            self.special()
        elif do==4:
            info().show_info("man2")

    def item(self):
        pass

class info:
    def show_info(self,name):
        self.name=name
        man2.show()
        if self.name=="man2":
            man2.next_do()


class man(human):
    def do_power_up(self):
        self.remaing_mp(10)
        print("\nmp:{}".format(self.mp)) # DEBUG:
        self.power_up(5)
        print("強化した\n")
    def strong_attack(self):
        self.remaing_mp(5)
        print("\nmp:{}".format(self.mp)) # DEBUG:
        self.base_attack(50)
    def critical_up(self):
        self.remaing_mp(10)
        print("\nmp:{}".format(self.mp)) # DEBUG:
        self.critical(5)
        print("集中した\n")
    def back(self):
        self.next_do()
    def special(self):
        while True:
            try:
                do=int(input("1:強化　2:強攻撃　3:集中　4:戻る\n"))
                if do>4 and do<=0:
                    print("入力し直し")
                elif do>0 and do<5:
                    break
                else:
                    print("入力し直し")
            except:
                print("入力し直し")
        if do==1:
            self.do_power_up()
        elif do==2:
            self.strong_attack()
        elif do==3:
            self.critical_up()
        else:
            self.back()

        #speciallist={1:"a"}

man2=man("man","デバック",100,100,30)
#woman=human("woman",90,110)
#info().show_info(man.getname(),man.gethp(),man.getmp())
