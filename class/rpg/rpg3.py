import random
import math
class human:
    """大体共通するクラス"""
    def __init__(self,name,job,hp,mp,n_attack):
        self.name=name
        self.job=job
        self.max_hp=hp
        self.hp=hp
        self.max_mp=mp
        self.mp=mp
        self.n_attack=n_attack
        self.power=1
        self.power_turn=0
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
        print("")
        print("名前:{} ".format(self.getname()))
        print("職業:{} ".format(self.getjob()))
        print("hp:{}/{} ".format(self.gethp(),self.max_hp))
        print("mp:{}/{}".format(self.getmp(),self.max_mp))
        print("")
##hp mpの変動
#減る
    def remaing_hp(self,damage):
        self.hp-=damage
    def remaing_mp(self,used_mp):
        self.mp-=used_mp
#増える
    def charge_hp(self,care_hp):
        if self.hp<self.max_hp:
            self.hp+=care_hp
            print("\n{}は\n{}回復した\n".format(self.name,care_hp))
        else:
            print("これ以上回復できない")
    def charge_mp(self,care_mp):
        self.mp+=care_mp
##行動
        #後々調整
#攻撃
    def base_attack(self,trick):
        #強化か弱体か
        self.power_status(self.power_turn)
        #クリティカル関係
        self.critical(self.cri_up_turn)
        if self.cri_up_turn>0:
            self.cri=random.randint(1,10)
            if self.cri>3:
                print("クリティカル！")# DEBUG:
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
        #return trick*self.cri_rate*self.power_status
        print("attack {}\n".format(math.floor(trick*self.cri_rate*self.power))) # DEBUG:

    def power_status(self,power_turn):
        self.power_turn=power_turn
        if self.power_turn>0:
            self.power=1.5
            self.power_turn-=1
            print("power_status:{}".format(self.power)) # DEBUG:
            print("power_turn:{}\n".format(self.power_turn)) # DEBUG:
        elif self.power_turn<0:
            self.power=0.5
            self.power_turn+=1
            print("power_status:{}".format(self.power)) # DEBUG:
            print("power_turn:{}\n".format(self.power_turn)) # DEBUG:
        else:
            self.power=1
            print("\npower_status:{}".format(self.power)) # DEBUG:

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


#行動選択
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
            Item().choice_item(self.name)
        elif do==3:
            self.special()
        elif do==4:
            show_status().show_info(self.name)

    def back(self):
        self.next_do()

class show_status:
    def show_info(self,name):
        self.name=name
        man2.show()
        if self.name=="man":
            self.name=man2
        self.name.next_do()

class Item:
    def __init__(self):
        self.hp_recover=10
        self.mp_recover=10
        self.gedoku=10
        self.siketu=10
        self.itamidome=10
    def choiced_hp_recover(self):
        self.name.charge_hp(50)
    def choiced_mp_recover(self):
        pass
    def choiced_gedoku(self):
        pass
    def choiced_siketu(self):
        pass
    def choiced_itamidome(self):
        pass
    def choice_item(self,name):
        if name=="man":
            self.name=man2
        choice=int(input("1:hp回復薬 {}　2:mp回復薬 {}　3:解毒剤 {}　4:止血剤 {}　5:痛み止め {}　6:戻る\n".format(self.hp_recover,self.mp_recover,self.gedoku,self.siketu,self.itamidome)))
        if choice==1:
            self.choiced_hp_recover()



class man(human):
    def do_power_up(self):
        self.remaing_mp(10)
        print("\nmp:{}".format(self.mp)) # DEBUG:
        self.power_status(5)
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
#show_status().show_info(man.getname(),man.gethp(),man.getmp())
