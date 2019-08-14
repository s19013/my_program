import random
class human:
    """大体共通するクラス"""
    def __init__(self,name,hp,mp,n_attack,health):
        self.name=name
        self.hp=hp
        self.mp=mp
        self.n_attack=n_attack
        self.health=health
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

        #後々調整
    def base_attack(self,trick):
        self.trick=trick
        return self.trick

    def do(self):
        dolist=[None,base_attack(30),item(),special()]
        while True:
            self.do=input("1:攻撃　2:アイテム　3:特技\n")
            if self.do!=int:
                print(入力し直し)
            elif:self.do>3:
                print(入力し直し)
            else:
                break
        if 

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
        speciallist=[1:""]

man2=man("man",100,100,30,good)
#woman=human("woman",90,110)
#info().show_info(man.getname(),man.gethp(),man.getmp())
