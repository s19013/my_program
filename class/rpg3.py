import random
class human:
    """大体共通するクラス"""
    def __init__(self,name,hp,mp,n_attack,power_up):
        self.name=name
        self.hp=hp
        self.mp=mp
        self.n_attack=n_attack
        self.power_up=power_up
#ステータスを取る
    def getname(self):
        return self.name
    def gethp(self):
        return self.hp
    def getmp(self):
        return self.mp
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
#行動
        #後々調整
    def base_attack(self,trick,cri=0):
        self.critical(self.cri_up)
        if self.cri_up>0:
            self.cri=random.randint(1,10)
            if self.cri>3:
                print("クリティカル！")
                self.cri_rate=1.4
            else:
                self.cri_rate=1
            self.cri_up-=1
            # DEBUG: print(self.cri_up)
        else:
            self.cri=random.randint(1,10)
            if self.cri>8:
                print("クリティカル")# DEBUG:
                self.cri_rate=1.4
            else:
                self.cri_rate=1
        #return trick*self.cri_rate
        print("attack {}".format(trick*self.cri_rate))

    def critical(self,cri_up):
        self.cri_up=cri_up
        try:
            pass
        except :
            cri_up=0
        # if self.cri_up==None or self.cri_up==0:
        #     self.cri_up=0
        # else:
        #     pass
        # if self.cri_up>0:
        #     self.cri=random.randint(1,10)
        #     if self.cri>4:
        #         print("cri!") #DEBUG:
        #         self.cri_rate=1.4
        #     else:
        #         self.cri_rate=1
        #     self.cri_up-=1
        #     # DEBUG: print(self.cri_up)
        # else:
        #     self.cri=random.randint(1,10)
        #     if self.cri>8:
        #         print("cri")# DEBUG:
        #         self.cri_rate=1.4
        #     else:
        #         self.cri_rate=1



    def do(self):
        dolist=[None,self.base_attack(30),self.item(),self.special()]
        while True:
            try:
                self.do=int(input("1:攻撃　2:アイテム　3:特技\n"))
                if self.do>3:
                    print("入力し直し")
                else:
                    break;
            except:
                print("入力し直し")
        dolist[self.do]

    def item(self):
        pass
    # def cri(self,base,up_cri):
    #     self.base=base
    #     self.up_cri=up_cri
    #     if up_cri!=1:
    #         cri=0
    #         num=random.randint(1,10)
    #         if num>=8:
    #             print("クリティカル！")
    #             cri=1.5
    #         else:
    #             cri=1
    #     else:
    #         cri=1.5
    #     return self.base*cri

class info:
    def show_info(self,name,hp,mp):
        self.name=name
        self.hp=hp
        self.mp=mp
        print("""{}
HP:{}
MP:{}""".format(self.name,self.hp,self.mp))
class man(human):
    def special(self):
        pass
        #speciallist={1:"a"}

man2=man("man",100,100,30,1)
#woman=human("woman",90,110)
#info().show_info(man.getname(),man.gethp(),man.getmp())
