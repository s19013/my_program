import random
class human:
    """大体共通するクラス"""
    def __init__(self,name,job,hp,mp,n_attack,power_up):
        self.name=name
        self.job=job
        self.hp=hp
        self.mp=mp
        self.n_attack=n_attack
        self.power_up=power_up
        self.cri_up=0
#ステータスを取る
    def getname(self):
        return self.name
    def gethp(self):
        return self.hp
    def getmp(self):
        return self.mp
    def getjob(self):
        return self.job
#情報を見せる
    def show(self):
        print("名前:{} ".format(self.getname()))
        print("職業:{} ".format(self.getjob()))
        print("hp:{} ".format(self.gethp()))
        print("mp:{} ".format(self.getmp()))
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
        # try:
        #     pass
        # except :
        #     cri_up=0
        self.cri_up=cri_up
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



    def next_do(self):
        dolist=[None,self.base_attack(self.n_attack),self.item(),self.special(),self.show()]
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
        dolist[do]
        #↓だと表示される
        #if do==1:
            #self.base_attack(self.n_attack)

    def item(self):
        pass


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

man2=man("man","デバック",100,100,30,1)
#woman=human("woman",90,110)
#info().show_info(man.getname(),man.gethp(),man.getmp())
